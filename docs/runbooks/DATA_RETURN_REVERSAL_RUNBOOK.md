# Data Return and Reversal Runbook

## Goal

Return Mr.liou-controlled materials from an external execution or hosting environment into controlled storage, verify completeness, reconstruct an independently operable Mrliouhan world, then remove external bindings and request deletion with evidence.

This runbook does not assume that a platform is malicious. It also does not accept platform policy as proof that account-specific data, billing, domains or deployments were handled correctly.

## Required order

### 1. Freeze the current state

- Do not delete projects, tasks, deployments or accounts yet.
- Capture account, project, member, deployment, custom-domain, usage and billing screens.
- Export support conversations and cancellation records.
- Record local time, UTC time, account identity and the visible project identifiers.

### 2. Inventory every external location

Create a ledger for:

- projects and tasks;
- conversations, prompts and uploaded files;
- generated source, build artifacts and downloadable packages;
- deployments, published URLs and environment settings;
- custom domains and DNS verification records;
- API keys, OAuth grants, webhooks and repository applications;
- invoices, orders, usage details, credits, auto-pay and refunds;
- deleted-item notices, retention statements and audit logs.

Unknown or inaccessible locations remain `UNRESOLVED`; they are not treated as empty.

### 3. Export without transformation

Prefer original exports. Preserve:

- filenames and directory structure;
- original timestamps when available;
- platform metadata and identifiers;
- source and build files separately;
- invoices and usage records;
- screenshots only as supplemental evidence, not as a replacement for machine-readable data.

### 4. Create a cryptographic manifest

Run:

```bash
python tools/mrliouhan_recovery.py inventory /path/to/export \
  --output evidence/manifests/external-export.manifest.json
```

The manifest records relative paths, sizes, timestamps and SHA-256 hashes.

### 5. Verify the returned copy

Copy the export into controlled storage, then run:

```bash
python tools/mrliouhan_recovery.py verify \
  evidence/manifests/external-export.manifest.json \
  --root /path/to/controlled-copy \
  --output evidence/verifications/external-export.verify.json
```

A successful file verification does not prove that the export was complete. Compare it with the external inventory, screenshots, project counts and audit logs.

### 6. Create the two-way transfer record

```bash
python tools/mrliouhan_recovery.py transfer-record \
  evidence/manifests/external-export.manifest.json \
  --output evidence/transfers/manus-return.json \
  --from-party "external platform" \
  --to-party "Mr.liou" \
  --provider-role "execution_platform" \
  --consent-record "evidence/consent/cancellation-or-project-record" \
  --return-path "verified export to Mr.liou-controlled storage" \
  --rollback-path "restore from signed manifest and offline backup"
```

Complete billing, domain, consent and deletion fields as evidence becomes available.

### 7. Restore an independently operable world

The replacement must run without requiring the disputed external platform for core operation. Preserve legitimate upstream licenses and isolate external services behind optional adapters.

Minimum acceptance:

- source and dependencies are documented;
- secrets are supplied through local environment configuration, not committed;
- local or selected infrastructure can run the core workflow;
- data can be restored from the verified manifest;
- external adapters can be disabled without corrupting the core state;
- every published artifact has a return and rollback path.

### 8. Revoke external control paths

Only after verified recovery:

- revoke API keys, OAuth grants, repository apps and webhooks;
- remove published links and shares;
- stop deployments and auto-pay;
- disconnect `Mrliouhan.ai` or other custom domains after saving the full DNS state;
- rotate credentials that may have been visible to the platform;
- verify that old URLs and APIs no longer expose the recovered data.

### 9. Request external deletion

Request deletion of projects, conversations, uploaded data, generated artifacts, deployments and account data. Require:

- case or ticket number;
- deletion scope;
- completion date;
- backup-retention period;
- legal, security or accounting retention exceptions;
- confirmation that published URLs, shares and API access are disabled.

Do not label the result `DELETED_VERIFIED` merely because an item disappears from the user interface.

### 10. Close the loop

Closure requires:

- inventory completed;
- export and controlled copy hashed;
- verification passed;
- missing items resolved or explicitly listed;
- independent reconstruction tested;
- external bindings revoked;
- billing stopped or disputed charges resolved;
- deletion confirmation and retention exceptions recorded;
- history preserved as append-only evidence.

Valid final states are `BALANCED`, `REVERSED` or `DISPUTED_WITH_RECORDED_GAPS`. Silent closure is forbidden.
