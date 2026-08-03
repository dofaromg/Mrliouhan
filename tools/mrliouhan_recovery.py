#!/usr/bin/env python3
"""Inventory, verify and record the return of externally processed data.

This tool uses only the Python standard library. It does not log in to external
platforms or delete remote data. It creates verifiable local evidence before
any external binding or copy is removed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

SCHEMA = "MrLiouhan.RecoveryManifest.v1"
TRANSFER_SCHEMA = "MrLiouhan.ParticleTransferRecord.v1"


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def timestamp_utc(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat().replace(
        "+00:00", "Z"
    )


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file_handle:
        while True:
            chunk = file_handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"expected JSON object in {path}")
    return payload


def build_manifest(source_root: Path, output_path: Path | None = None) -> dict[str, Any]:
    source_root = source_root.expanduser().resolve()
    if not source_root.exists() or not source_root.is_dir():
        raise ValueError(f"source root is not a directory: {source_root}")

    output_resolved = output_path.expanduser().resolve() if output_path else None
    files: list[dict[str, Any]] = []
    total_bytes = 0

    for path in sorted(item for item in source_root.rglob("*") if item.is_file()):
        resolved = path.resolve()
        if output_resolved and resolved == output_resolved:
            continue
        stat = path.stat()
        relative_path = path.relative_to(source_root).as_posix()
        entry = {
            "relative_path": relative_path,
            "size_bytes": stat.st_size,
            "modified_utc": timestamp_utc(stat.st_mtime),
            "sha256": sha256_file(path),
        }
        files.append(entry)
        total_bytes += stat.st_size

    return {
        "schema": SCHEMA,
        "generated_at": now_utc(),
        "source_root": str(source_root),
        "file_count": len(files),
        "total_bytes": total_bytes,
        "files": files,
        "return_state": {
            "status": "PENDING_RETURN",
            "verified": False,
            "restored": False,
            "external_deletion_verified": False,
        },
    }


def verify_manifest(manifest: dict[str, Any], root: Path) -> dict[str, Any]:
    if manifest.get("schema") != SCHEMA:
        raise ValueError(f"unsupported manifest schema: {manifest.get('schema')!r}")

    root = root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"verification root is not a directory: {root}")

    expected = {
        entry["relative_path"]: entry
        for entry in manifest.get("files", [])
        if isinstance(entry, dict) and entry.get("relative_path")
    }
    actual_paths = {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file()
    }

    missing: list[str] = []
    mismatched: list[dict[str, Any]] = []

    for relative_path, expected_entry in expected.items():
        path = actual_paths.get(relative_path)
        if path is None:
            missing.append(relative_path)
            continue
        actual_size = path.stat().st_size
        actual_hash = sha256_file(path)
        if (
            actual_size != expected_entry.get("size_bytes")
            or actual_hash != expected_entry.get("sha256")
        ):
            mismatched.append(
                {
                    "relative_path": relative_path,
                    "expected_size": expected_entry.get("size_bytes"),
                    "actual_size": actual_size,
                    "expected_sha256": expected_entry.get("sha256"),
                    "actual_sha256": actual_hash,
                }
            )

    unexpected = sorted(set(actual_paths) - set(expected))
    ok = not missing and not mismatched
    return {
        "schema": "MrLiouhan.RecoveryVerification.v1",
        "verified_at": now_utc(),
        "root": str(root),
        "ok": ok,
        "missing": sorted(missing),
        "mismatched": mismatched,
        "unexpected": unexpected,
        "closure_status": "PENDING_RETURN" if ok else "IMBALANCED",
    }


def build_transfer_record(
    manifest: dict[str, Any],
    from_party: str,
    to_party: str,
    provider_role: str,
    consent_record: str,
    return_path: str,
    rollback_path: str,
) -> dict[str, Any]:
    file_hashes = "\n".join(
        entry.get("sha256", "") for entry in manifest.get("files", [])
    ).encode("utf-8")
    aggregate_hash = hashlib.sha256(file_hashes).hexdigest()
    generated_at = manifest.get("generated_at") or now_utc()

    return {
        "schema": TRANSFER_SCHEMA,
        "record_id": f"PTR-{uuid4()}",
        "artifact_id": f"recovery-manifest:{aggregate_hash}",
        "source": {
            "source_type": "external_export",
            "source_location": manifest.get("source_root", "unknown"),
            "source_timestamp": generated_at,
            "derived_from": [],
            "license_or_permission": None,
        },
        "sender": {"name": from_party, "role": "source_or_external_holder", "account_or_identity": None},
        "receiver": {"name": to_party, "role": "return_recipient", "account_or_identity": None},
        "intermediaries": [],
        "transfer": {
            "purpose": "verified data return and independent reconstruction",
            "started_at": generated_at,
            "completed_at": None,
            "provider_role": provider_role,
            "published_locations": [],
            "domain_bindings": [],
        },
        "consent": {
            "status": "DISPUTED" if not consent_record else "EXPLICIT",
            "record_location": consent_record or None,
            "scope": None,
            "withdrawn_at": None,
        },
        "integrity": {
            "algorithm": "SHA-256",
            "source_hash": aggregate_hash,
            "returned_hash": None,
            "verification_status": "PENDING",
        },
        "billing": {
            "status": "UNRESOLVED",
            "amount": None,
            "currency": None,
            "service_period": None,
            "invoice_or_order_id": None,
            "usage_record_location": None,
            "refund_or_reversal_record": None,
        },
        "return_path": {
            "status": "AVAILABLE" if return_path else "MISSING",
            "method": return_path or "not documented",
            "evidence_location": None,
            "verified_at": None,
        },
        "rollback_path": {
            "status": "AVAILABLE" if rollback_path else "MISSING",
            "method": rollback_path or "not documented",
            "evidence_location": None,
            "verified_at": None,
        },
        "evidence": [
            {
                "classification": "DIRECT_EVIDENCE",
                "location": "recovery manifest",
                "description": "File inventory, sizes and SHA-256 hashes generated from the returned export.",
                "captured_at": now_utc(),
            }
        ],
        "closure_status": "PENDING_RETURN",
        "notes": [
            "This record does not prove remote deletion or settle disputed responsibility.",
            "Remote deletion must occur only after local recovery and verification."
        ],
    }


def command_inventory(args: argparse.Namespace) -> int:
    output = Path(args.output)
    manifest = build_manifest(Path(args.source), output)
    write_json(output, manifest)
    print(f"manifest={output}")
    print(f"files={manifest['file_count']}")
    print(f"bytes={manifest['total_bytes']}")
    return 0


def command_verify(args: argparse.Namespace) -> int:
    result = verify_manifest(load_json(Path(args.manifest)), Path(args.root))
    if args.output:
        write_json(Path(args.output), result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


def command_transfer_record(args: argparse.Namespace) -> int:
    record = build_transfer_record(
        load_json(Path(args.manifest)),
        from_party=args.from_party,
        to_party=args.to_party,
        provider_role=args.provider_role,
        consent_record=args.consent_record,
        return_path=args.return_path,
        rollback_path=args.rollback_path,
    )
    write_json(Path(args.output), record)
    print(f"transfer_record={args.output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create evidence for data return, integrity and two-way closure."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inventory = subparsers.add_parser("inventory", help="Hash an export directory.")
    inventory.add_argument("source")
    inventory.add_argument("--output", required=True)
    inventory.set_defaults(func=command_inventory)

    verify = subparsers.add_parser("verify", help="Verify files against a manifest.")
    verify.add_argument("manifest")
    verify.add_argument("--root", required=True)
    verify.add_argument("--output")
    verify.set_defaults(func=command_verify)

    transfer = subparsers.add_parser(
        "transfer-record", help="Create a two-way particle transfer record."
    )
    transfer.add_argument("manifest")
    transfer.add_argument("--output", required=True)
    transfer.add_argument("--from-party", required=True)
    transfer.add_argument("--to-party", default="Mr.liou")
    transfer.add_argument("--provider-role", default="external_platform")
    transfer.add_argument("--consent-record", default="")
    transfer.add_argument("--return-path", required=True)
    transfer.add_argument("--rollback-path", required=True)
    transfer.set_defaults(func=command_transfer_record)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
