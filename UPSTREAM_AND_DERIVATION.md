# Upstream and Derivation Boundary

## Repository condition at branch creation

The `main` branch of `dofaromg/Mrliouhan` contains an OpenManus-based codebase and README that attributes the upstream project and contributors from FoundationAgents / MetaGPT.

This reconstruction branch does **not** erase or replace that upstream history.

## Role separation

| Layer | Role |
|---|---|
| OpenManus and its contributors | Upstream open-source framework and implementation lineage where code is reused |
| Mr.liou / MrLiouWord | MRL definitions, user-provided data, system-specific architecture, configuration, content and reconstruction decisions |
| Manus platform | External service only where hosting, execution, billing or publication actually occurred |
| AI coding agents | Implementation assistance recorded per commit or artifact |
| GitHub | Repository and collaboration infrastructure |

## Causal rule

A reused framework must retain its license and contributor attribution. Likewise, importing Mr.liou-provided materials into a framework or platform does not convert those materials into upstream or platform-owned definitions.

Every reconstructed module must state one of:

- `upstream_unmodified`
- `upstream_modified`
- `mrl_original`
- `mrliou_user_data`
- `external_platform_export`
- `generated_derivative`
- `unresolved_origin`

## Prohibited actions

- Removing valid upstream license or contributor history.
- Labeling upstream code as MRL-original without evidence.
- Labeling Mr.liou-provided definitions, files or data as platform-originated merely because a platform processed or displayed them.
- Rewriting disputed history instead of appending corrections and evidence.
- Publishing an artifact without a source path, hash or permission basis.

## Reconstruction objective

Build a self-controlled `Mrliouhan` world that can operate without Manus platform dependency, while preserving every legitimate upstream contribution and restoring the source chain of Mr.liou-provided materials.
