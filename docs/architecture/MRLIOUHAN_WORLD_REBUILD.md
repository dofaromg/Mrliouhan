# Mrliouhan World Rebuild Architecture

## Objective

Construct an independently operable Mrliouhan world that can receive, verify and use returned Mr.liou-controlled data without making an external platform the root of identity, data, execution or billing.

This repository currently contains an OpenManus-based upstream codebase. The rebuild must preserve OpenManus attribution and license while isolating MrLiouWord/MRL-specific definitions, recovered data and external-platform records.

## Layer model

### L0 — Controlled source and identity

- Mr.liou-controlled source materials and account exports.
- `MrLiouWord` origin signature where supported by source records.
- Repository identity `dofaromg/Mrliouhan` as an operational location, not proof that every file originated there.
- Upstream code and third-party materials remain separately attributed.

### L1 — Evidence and provenance registry

Stores:

- evidence classifications;
- source locations and timestamps;
- SHA-256 manifests;
- consent, license and permission records;
- actor/action/time/object audit entries;
- billing, domain and deployment correspondence;
- unresolved conflicts without forced closure.

Primary schema: `schemas/particle-transfer-record.schema.json`.

### L2 — Return and reversal engine

Implements:

- export inventory;
- integrity verification;
- transfer records;
- restore checks;
- return and rollback paths;
- deletion verification after recovery.

Initial implementation: `tools/mrliouhan_recovery.py`.

### L3 — External adapters

Every external system is optional and role-limited:

- execution platform;
- hosting provider;
- billing provider;
- model provider;
- source mirror;
- domain/DNS provider;
- storage provider.

An adapter cannot become the canonical source merely because it executes, renders, hosts, bills or displays an artifact. Disabling an adapter must not destroy the controlled source or recovery manifest.

### L4 — Agent runtime

The existing OpenManus runtime may be retained as one implementation engine. MRL-specific behavior must enter through explicit configuration, data packages or adapters rather than silently rewriting upstream authorship.

Runtime requirements:

- provider-neutral model interface;
- local or selected-provider execution;
- explicit tool permissions;
- auditable task history;
- controlled workspace paths;
- exportable state;
- external-network and destructive actions gated by approval;
- no secrets committed to Git.

### L5 — Mrliouhan services

Planned service boundaries:

- `provenance-service`: records source, evidence and derivation;
- `return-service`: manifests, verification and restore state;
- `adapter-registry`: external roles, consent and revocation paths;
- `world-runtime`: agent and workflow execution;
- `billing-ledger`: service period, usage, charge and refund correspondence;
- `domain-ledger`: registrar, DNS, deployment, canonical URL and rollback state;
- `publication-gate`: blocks publication without provenance and return paths.

The initial branch provides file-based records and CI checks. Services should be implemented only after the schemas and acceptance tests are stable.

### L6 — Domain and public projection

`Mrliouhan.ai` or another public domain is a projection of the controlled world, not the root data store.

Before any domain connection:

- save the complete DNS zone;
- record registrar and nameservers;
- identify the target deployment and operator;
- preserve canonical URL, Open Graph, site name and favicon settings;
- define rollback DNS values;
- identify expected billing and renewal responsibility.

### L7 — Closure and audit

Every external movement must end in one of these states:

- `BALANCED`: both parties' roles, consent, value and return paths are documented;
- `PENDING_RETURN`: data or control has not yet returned;
- `DISPUTED`: evidence conflicts or account records are missing;
- `IMBALANCED`: integrity, consent, billing or return requirements fail;
- `REVERSED`: controlled data has returned, external paths are revoked and evidence is preserved.

## Directory separation

```text
upstream/ or existing app/       legitimate upstream implementation
mrl/                             future MRL-specific runtime modules
data/recovered/                  returned data; normally Git-ignored or encrypted
schemas/                         provenance and transfer contracts
evidence/                        manifests and redacted records; sensitive items restricted
tools/                           recovery and verification utilities
docs/                            architecture, law, evidence and runbooks
.mrliou/                         repository governance locks
```

Do not commit payment-card data, access tokens, private conversations or unredacted personal information to a public repository.

## Missing components identified in the window review

The earlier branch had governance declarations but lacked executable return tooling, a precise processing-rights boundary, a shared evidence classification, a transfer schema, reconstruction architecture, recovery tests and a CI gate for those components. This rebuild adds those foundations.

## Acceptance criteria

1. OpenManus attribution and license remain visible.
2. Mr.liou-controlled and third-party materials are separately identifiable.
3. A directory export can be inventoried and hashed.
4. A controlled copy can be verified against its manifest.
5. A two-way transfer record can be created with return and rollback paths.
6. Platform statements, user accounts, direct evidence and inference remain distinct.
7. External adapters can be disabled without losing controlled data.
8. Publication is not treated as canonical when provenance or return paths are missing.
9. Remote deletion is never claimed without account, URL, API and written-retention verification.
10. CI tests the recovery tooling and validates required governance files.
