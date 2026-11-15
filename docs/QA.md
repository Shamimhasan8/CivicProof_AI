# Verified implementation evidence

Build date: 15 November 2026.

## Automated
- TypeScript type checking passed.
- 60/60 developer-authored synthetic benchmark cases passed; generated results include exact scope and unmeasured metrics.
- Additional confirmation, synthetic-marker, date-validation, source allowlist and letter non-submission assertions passed.
- API handler regressions passed: registry, unknown demand, empty query, invalid action, oversized query, oversized body, conditional requirements, malformed JSON.
- Proposed 14-table SQLite schema executes in an in-memory database. It is not deployed.
- Production Worker build passed before final packaging; final build is run again with the source archive.

## Browser workflows actually observed
- Bengali default interface and English toggle.
- Guided synthetic document example: name spelling discrepancy and consistent dates after explicit confirmation.
- Actual Tesseract image OCR of watermarked synthetic-nid.png: extracted Amina Rahman, 1998-04-12, NID and watermark. No claim of general OCR accuracy.
- Actual PDF.js text extraction of synthetic-passport.pdf: extracted Amina Rahaman, 1998-04-12, Passport and watermark.
- PNG and clarification-draft downloads complete successfully. PNG downloader was changed from a data URL to a static generated asset after an automation download-event failure.
- Lost-passport checkbox makes R13 applicable, hides the ordinary-original-passport path under applicable filter, and accepts user-reported GD readiness.
- A bank statement returns Needs official clarification; no unsupported illegality conclusion.
- Record & draft creates a citizen-reported timeline event and navigates to the letter editor.
- A Bangla draft is generated from current request text; download completes.
- Manual synthetic receipt event saves with an evidence reference and unauthenticated label. Timeline export completes; test receipt deletion removes it.
- 390×844 CSS-pixel responsive preview uses a real iframe viewport, not a simulated screenshot. Mobile menu opens and navigates to Requirements, then closes. This is not physical-device touch testing.
- Source registry search filtered to SRC-02; the live technical portal displayed the actual 60/60 report.
- Case JSON export completed. Explicit deletion cleared document counts, checklist selections, timeline and draft in the tab.
- Screenshots in public/reports/screenshots are actual app captures.

## Constraints
The large raw-image language assets and PDF module require network access and can delay first extraction. No backend case storage, provider LLM, embedding service, authenticated government record or independently reviewed legal rules are present. Full accessibility and penetration testing have not been performed.

## Publication
Private Site deployment is performed after source packaging. A successful Sites deployment response is the publication evidence; judge/public access is not implied. Final URL: https://civicproof-ai-agi.adilshamim80.chatgpt.site
