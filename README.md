# CivicProof AI

Citizen Service Evidence & Accountability Platform · Team AGI

**Independent Bangladesh e-Passport re-issue preparation demo. Synthetic documents only.**

## Run

Use Node 22.x. Install the locked dependencies with `npm ci`, then `npm run dev`. `npm run build` and `npm start` use native Next.js. Vercel configuration is in `vercel.json`; see DEPLOYMENT.md. The original Sites build is preserved separately as `npm run build:sites` and requires its original manifest.

- `npm test` — 60 synthetic benchmark cases plus safety/provenance regressions; creates `public/reports/evaluation.json`.
- `npm run typecheck` — TypeScript validation.
- `npm run test:production` — verify the built Next.js server, all 11 citizen routes, and the request-checker API. Run after `npm run build`.
- `npm run build` — native Next.js production build for Vercel.

## Working features

Bangla-first interface with English toggle; 11 views; watermarked PNG/TXT samples; local image OCR using Tesseract.js eng+ben; PDF.js text extraction with first-page OCR fallback; editable field confirmation; conservative name and ISO-date comparison; 16 conditional source-linked draft mappings; bilingual keyword request retrieval; citizen-reported timeline with text evidence; editable Bangla/English clarification templates; export and explicit deletion; live documentation.

No LLM, embedding provider, government integration, legal-rule reviewer, or production case database is configured. OCR requires external CDN access. A typed fictional sample is available when downloads fail. The source registry honestly distinguishes indexed passages from directly fetched pages.

## Three reproducible demos

1. Overview → Try a guided example → Confirm & compare. Name differs by one letter, DOB agrees. Inspect original and normalized values, then save to timeline.
2. Requirements → Passport lost or stolen. R13 becomes applicable; mark the fictional GD ready. The previous-original-passport path becomes non-applicable.
3. Request checker → “A bank statement” → Check available guidance → Needs official clarification → Record & draft a letter. Create, edit, copy or download the draft. Nothing is sent.

## Architecture

Next.js 16 + React 19 + TypeScript. The standard Vercel deployment hosts the UI and `/api/evidence`; the original Vinext / Cloudflare build remains an optional separate target. A shared deterministic engine runs comparisons and conditional evaluation. The backend handles request retrieval without persistence. Case state uses sessionStorage; only UI language uses localStorage. Browser restore may preserve sessionStorage. Explicit deletion clears the case state.

## Data & evidence

See DATA_PROVENANCE.md, RESPONSIBLE_AI.md, SECURITY.md, and EVALUATION.md. All rule mappings await specialist review. No result grants legal eligibility. See `/docs` for implementation statuses. Proposed schema in `migrations/001_proposed_schema.sql` is not applied to a production database.

## Deployment

See DEPLOYMENT.md. `.openai/hosting.json` preserves Site identity. Runtime secrets are neither required nor configured. Do not make this private preview public without the owner's instruction. The Git source repository belongs to this Site; GitHub publication requires a target repository and access.

## Competition files

SUBMISSION.md, VIDEO_SCRIPT.md, DESIGN_SYSTEM.md, screenshots, test fixtures and JSON results. The downloadable submission ZIP includes the source and these documents. No YouTube or Figma publication has been fabricated.
