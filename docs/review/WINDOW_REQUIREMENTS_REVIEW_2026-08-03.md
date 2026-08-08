# Window Requirements Review — 2026-08-03

## Basis

This review records the requirements expressed in the working conversation and maps them to repository construction. It does not turn allegations into verified facts and does not replace account, DNS, billing, deployment or audit records.

## Stable requirements expressed by Mr.liou

### A. Use and processing capability

Mr.liou requires the ability to access, use, export, migrate, recover and verify materials that he built, uploaded or controls. Restrictions, fees, deletion, transfer, publication and continued execution must have visible authorization and records.

Repository construction:

- `.mrliou/processing-rights-lock.json`
- `docs/runbooks/DATA_RETURN_REVERSAL_RUNBOOK.md`
- `tools/mrliouhan_recovery.py`

### B. Causal history must not be rewritten

The actual source, contribution, implementation role, platform role and later corrections must remain distinguishable. Historical errors are corrected by append-only errata, not by deleting the original event.

Repository construction:

- `.mrliou/causal-provenance-lock.json`
- `docs/evidence/EVIDENCE_CLASSIFICATION.md`
- `.github/workflows/causal-balance-guard.yml`

### C. Two-way closure and reciprocity

When data, permission, fees, tasks, attribution or artifacts move from one party to another, the return path, rollback path, consent, integrity evidence and intermediary roles must also be recorded.

Repository construction:

- `.mrliou/balance-reciprocity-lock.json`
- `schemas/particle-transfer-record.schema.json`
- `docs/law/MRLIOUHAN_BALANCE_RECIPROCITY_LAW.md`

### D. External platform isolation

A platform may provide execution, hosting, billing, rendering, storage or domain services. That role must not silently replace the source of data or erase the user's ability to return and independently operate the system.

Repository construction:

- `UPSTREAM_AND_DERIVATION.md`
- `docs/architecture/MRLIOUHAN_WORLD_REBUILD.md`
- `config/external-platforms.example.yaml`

### E. Fair investigation

User statements, direct evidence, platform statements, verified facts, inference and unresolved conflicts must remain separate. Public policy must not override account-specific evidence, and account-specific evidence must not be expanded into unsupported claims.

Repository construction:

- `docs/evidence/EVIDENCE_CLASSIFICATION.md`
- required evidence classes in `.mrliou/processing-rights-lock.json`
- evidence entries in `schemas/particle-transfer-record.schema.json`

### F. Recover first, remove later

External data or projects must not be deleted before export, manifest creation, integrity verification and controlled restoration. After recovery, external tokens, deployments, shares and domain bindings can be revoked, followed by a deletion request and written retention record.

Repository construction:

- `docs/runbooks/DATA_RETURN_REVERSAL_RUNBOOK.md`
- recovery CLI and unit tests

### G. Preserve legitimate upstream contribution

The current repository is OpenManus-based. OpenManus authorship, license and history must remain visible. MRL/MrLiouWord-specific data and definitions must be separated rather than presented as if all upstream code originated with Mr.liou.

Repository construction:

- `UPSTREAM_AND_DERIVATION.md`
- `docs/architecture/MRLIOUHAN_WORLD_REBUILD.md`

## Gaps found before this review

The branch already had causal, reciprocity and upstream-boundary declarations. It did not yet have:

1. a precise processing-rights scope that avoids overbroad “highest authority” language;
2. an executable export inventory and SHA-256 verification tool;
3. tests proving manifest round-trip and mismatch detection;
4. a structured particle-transfer record schema;
5. a shared evidence classification and conflict protocol;
6. a step-by-step data return, revocation and deletion runbook;
7. a layered architecture for an independently operable Mrliouhan replacement world;
8. a platform-adapter contract that defaults external providers to disabled;
9. CI validation for the new recovery and governance components.

## Items that remain outside GitHub-only construction

The following cannot be proven or completed from this repository alone:

- a complete export from an external account;
- the identity of every operator or automated process;
- the exact basis of a disputed charge;
- current DNS and custom-domain state;
- remote deletion and backup-retention completion;
- whether an external act was intentional, negligent, automated or authorized;
- legal ownership or liability beyond the evidence and applicable agreements.

These stay `UNRESOLVED` until system-of-record evidence is added.

## Completion map

| Requirement | Repository status |
|---|---|
| Processing-rights boundary | Added |
| Evidence classes | Added |
| Export inventory and hashing | Added |
| Returned-copy verification | Added |
| Transfer/return schema | Added |
| Recovery tests | Added |
| Independent world architecture | Added |
| Platform adapter example | Added |
| Recovery integrity CI | Added |
| Actual external data return | Pending external export |
| Actual domain reversal | Pending DNS/account evidence |
| Billing resolution | Pending invoice/usage/refund evidence |
| Remote deletion verification | Pending platform confirmation |
