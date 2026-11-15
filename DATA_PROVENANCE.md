# Data provenance

Retrieved 15 November 2026. This is a limited official-source collection for a synthetic prototype. No independent specialist has reviewed the rule mappings.

| ID | Official source | Version / date | Access and limitations |
|---|---|---|---|
| SRC-01 | https://www.epassport.gov.bd/landing/notices/160 | Checklist updated 21 October 2024 | Search-index passages; direct page client-rendered. Later instructions may change applicability. |
| SRC-02 | https://dip.gov.bd/pages/static-pages/6922e033933eb65569e25f86 | Charter snapshot retrieved 15 November 2026 | Search-index passage; direct fetch 502. References correction circular dated 18 February 2025; full circular not ingested. |
| SRC-03 | https://www.epassport.gov.bd/api/v1/registrations/download-offline-form | Form snapshot retrieved 15 November 2026 | Indexed PDF text; publication date not established. |
| SRC-04 | https://www.grs.gov.bd/ | Guidance retrieved 15 November 2026 | Public page directly retrieved; grievance exclusions apply. No passport eligibility rules derived. |
| SRC-05 | https://www.mygov.bd/ | Link-only record | Fetch timed out. No passage or rule derived. |

`public/reports/source-registry.json` stores the ingested passages and SHA-256 hashes of the ingested excerpt records, not hashes of complete official documents. IDs and clause references are stable within release 0.1.

## Review governance
Every rule has draft status and requires qualified review before production use. The application never describes these as independently expert-reviewed. The 2024 discrepancy undertaking is not enforced as sufficient correction evidence: R14 holds correction cases for official clarification because the charter references newer circular guidance. Lost-passport and ordinary-original-passport paths are separated. Newer publication alone is not treated as universally overriding older source scope.

## Synthetic data
Amina Rahman / Amina Rahaman and DEMO-* identifiers are fictional. Sample images are drawn by code, without official seals, flags, machine-readable zones or realistic ID numbers. They carry SYNTHETIC — NOT A REAL GOVERNMENT DOCUMENT. No external citizen datasets, scraped personal records or private government APIs are used.

## Lifecycle
Create fictional file → local parsing → human confirmation → rule preview → local timeline / draft → explicit export or deletion. Only request checker text/context reaches the backend; there is no server-side case persistence. Uploaded receipts are always citizen-reported and unauthenticated.
