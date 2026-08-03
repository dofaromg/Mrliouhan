import json
import tempfile
import unittest
from pathlib import Path

from tools.mrliouhan_recovery import (
    SCHEMA,
    TRANSFER_SCHEMA,
    build_manifest,
    build_transfer_record,
    verify_manifest,
)


class RecoveryManifestTests(unittest.TestCase):
    def test_inventory_and_verify_round_trip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "a.txt").write_text("MrLiouWord", encoding="utf-8")
            (root / "nested").mkdir()
            (root / "nested" / "b.bin").write_bytes(b"\x00\x01\x02")

            manifest = build_manifest(root)
            self.assertEqual(manifest["schema"], SCHEMA)
            self.assertEqual(manifest["file_count"], 2)
            self.assertEqual(
                sorted(item["relative_path"] for item in manifest["files"]),
                ["a.txt", "nested/b.bin"],
            )

            result = verify_manifest(manifest, root)
            self.assertTrue(result["ok"])
            self.assertEqual(result["missing"], [])
            self.assertEqual(result["mismatched"], [])

    def test_verify_detects_changed_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "artifact.json"
            target.write_text(json.dumps({"value": 1}), encoding="utf-8")
            manifest = build_manifest(root)

            target.write_text(json.dumps({"value": 2}), encoding="utf-8")
            result = verify_manifest(manifest, root)

            self.assertFalse(result["ok"])
            self.assertEqual(len(result["mismatched"]), 1)
            self.assertEqual(
                result["mismatched"][0]["relative_path"], "artifact.json"
            )

    def test_transfer_record_contains_return_and_rollback_paths(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "export.txt").write_text("returned", encoding="utf-8")
            manifest = build_manifest(root)

            record = build_transfer_record(
                manifest,
                from_party="external platform",
                to_party="Mr.liou",
                provider_role="execution_platform",
                consent_record="evidence/consent.pdf",
                return_path="verified export to controlled storage",
                rollback_path="restore from signed manifest and offline copy",
            )

            self.assertEqual(record["schema"], TRANSFER_SCHEMA)
            self.assertEqual(record["receiver"]["name"], "Mr.liou")
            self.assertEqual(record["return_path"]["status"], "AVAILABLE")
            self.assertEqual(record["rollback_path"]["status"], "AVAILABLE")
            self.assertEqual(record["closure_status"], "PENDING_RETURN")


if __name__ == "__main__":
    unittest.main()
