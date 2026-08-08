# Evidence Storage Guidance

This public repository must not contain unredacted account exports, payment-card details, private conversations, access tokens, personal identifiers or confidential invoices.

Store sensitive evidence in Mr.liou-controlled encrypted storage. Commit only redacted examples, non-sensitive manifests or references containing:

- evidence ID;
- classification;
- captured timestamp;
- controlled storage location;
- SHA-256 hash;
- short factual description;
- related claim or incident ID;
- verification status.

The `.gitignore` excludes common private evidence and export paths. A file being ignored by Git does not prove that it is encrypted, backed up or access-controlled; those controls must be implemented in the selected storage environment.
