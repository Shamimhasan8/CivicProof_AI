# Security and privacy

## Implemented controls
- Watermarked synthetic-only document parsing; no real documents permitted by the demo.
- PNG/JPEG/PDF content signature and MIME validation; TXT files bounded; maximum 8 MB, 5 PDF pages, 40,000 extraction characters. Event notes: text/plain, 100 KB, synthetic marker, first 3,000 characters retained.
- Extracted fields require user confirmation; original raw values preserved in local text and confirmed values shown beside normalized values.
- React escapes rendered text. No execution of document instructions and no LLM tool access.
- Source URLs fixed in code to Bangladesh .gov.bd hosts; request text cannot add URLs or rules.
- Case state stored only in browser sessionStorage; explicit deletion and export. Language alone uses localStorage. Browser restore can preserve sessions.
- No API keys committed or needed. No private administrator editor in the public UI.
- JSON body and query-length bounds, structured action validation, generic parse errors, no request-body logging in application code.
- Hosting access starts private. No changes to audience during this build.

## Risks and limits
A marker is not a reliable sensitive-data classifier: a user could label a real document SYNTHETIC. Do not expose this version for real citizen processing. A future production release needs authenticated per-user storage, robust retention, secure server-side scanning, abuse/rate controls, source-review governance, OCR robustness evaluation, CSP and dependency/subresource integrity review. Browser-loaded OCR libraries and language assets come from CDNs. Browser extensions and shared devices can access local state. Platform operational logs may include request metadata; no retention guarantees are claimed for the hosting platform.

No penetration test, external security audit, Bangladesh privacy-law assessment, government approval, or compliance certification was performed. The application has no distributed rate limiter. Stateless deterministic endpoints perform bounded work and no paid model calls.
