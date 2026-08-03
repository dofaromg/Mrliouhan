# Evidence Classification and Fairness Protocol

## Purpose

This protocol prevents either a platform statement or a user allegation from being silently promoted into a verified fact. Every claim must retain its source, evidence class, timestamp and unresolved conflicts.

## Evidence classes

| Class | Meaning | Allowed use |
|---|---|---|
| `USER_ACCOUNT` | Mr.liou's first-person description of an event, intent, cancellation, use or impact | Opens an investigation and defines the user's position; not automatically a verified fact |
| `DIRECT_EVIDENCE` | Screenshot, transaction notice, file, source code, commit, DNS export, invoice, audit log, email or platform page | May establish exactly what the evidence shows; interpretation beyond the evidence must be marked separately |
| `PLATFORM_STATEMENT` | Terms, help article, support response or interface statement published by a platform | Describes the platform's stated policy or explanation; cannot override contradictory direct evidence |
| `VERIFIED_FACT` | A point supported by independent and consistent records, or by an authoritative system-of-record export | May be used as a factual finding while preserving citations and time scope |
| `INFERENCE` | A reasoned explanation connecting known evidence | Must be labeled as inference and include the evidence it relies on |
| `UNRESOLVED` | Evidence conflicts, records are missing, or responsibility cannot yet be assigned | Must remain open; no blame, closure or ownership conclusion may be stated as proven |

## Source record

Every evidence item should contain:

```yaml
evidence_id: E-0001
classification: DIRECT_EVIDENCE
captured_at: 2026-08-03T00:28:00+08:00
source_party: Mr.liou
source_location: evidence/screenshots/example.png
sha256: <64-hex>
description: What is visibly shown without interpretation
related_claims: [C-0001]
privacy: restricted
```

## Conflict handling

1. Preserve both records; do not overwrite or delete the earlier statement.
2. Mark the conflict `CONFLICT_REQUIRES_AUDIT`.
3. Separate what the image or record proves from what a party says it means.
4. Request the system-of-record evidence: invoice, order ID, usage detail, audit log, DNS zone, deployment log or export manifest.
5. Do not use public policy text to dismiss account-specific evidence.
6. Do not use account-specific evidence to claim broader misconduct without actor, action, time and authorization proof.
7. Record corrections as append-only errata with who changed the assessment, when and why.

## Responsibility threshold

A responsibility finding requires, at minimum:

- an identifiable actor or automated system;
- a specific action or omission;
- a reliable timestamp or bounded period;
- the affected object or account;
- the authority, consent or rule that applied;
- direct evidence or a verified audit trail;
- impact and remediation status.

Without these fields, use `UNRESOLVED`, not a verdict.

## Historical integrity

The investigation history is append-only. Removing an incorrect conclusion is not enough; the record must preserve the original statement, the correction, the evidence that caused the correction and the resulting change in status.
