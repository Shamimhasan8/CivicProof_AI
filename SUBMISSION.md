# CivicProof AI — submission evidence

**Team:** AGI · **Project lead:** Adil · **Domain:** CivicSphere AI · **Challenge:** Transparent Government

## Story
Digital government portals do not remove every preparation and communication barrier. Citizens may encounter inconsistent identity fields, conditional documentation rules and unexpected requests. CivicProof makes the evidence visible: compare confirmed fields, inspect applicable official-source passages, preserve a citizen-reported journey and prepare a respectful clarification request. The initial scope is Bangladesh e-Passport re-issue.

## Proof
The source includes a functioning citizen workspace, actual local file extraction, deterministic comparison and conditional evaluation, bilingual keyword request retrieval, session-based timeline, editable Bangla/English letters, exports, deletion and a technical portal. Three reproducible judge scenarios are documented. Real evaluation results are in evaluation.json. All records shown are synthetic.

## AI-native build
The coding assistant implemented source, synthetic fixtures, tests and documentation from the user's product brief. Runtime AI consists of Tesseract OCR, with English/Bangla language models downloaded into the browser. No provider LLM or embeddings are connected. Explanations and letters are deterministic, and rules remain draft mappings awaiting specialist review. No independent legal review is claimed.

## Data lifecycle
Watermarked synthetic file → local OCR/PDF parsing → user correction and confirmation → conservative comparison / conditional checklist → optional local event → editable draft → user export or explicit deletion. Raw uploaded files and OCR stay browser-local. The request checker sends fictional request text and context to the same-origin backend without case persistence. Source registry entries retain URL, authority, date uncertainty, version and scope.

## Prompt library
PROMPT_REGISTRY.md contains the actual development brief reference, OCR configuration, current deterministic letter-template contract, and clearly labeled undeployed LLM extraction/explanation prompts. Source-grounded response schemas and uncertainty instructions are documented for future integration; no model execution or token reduction is invented.

## Build provenance
Source is versioned in the Site's Git repository. The downloadable source ZIP contains application files, locked dependencies, test suite, source registry and documentation. No artificial activity commits were requested or created. No real citizen data or secrets are included.

## Tools and IDE
ChatGPT Work coding environment, Node, Next-compatible React/TypeScript on Vinext, Cloudflare Worker hosting via Sites, Lucide icons, Tesseract.js, PDF.js, Git, Node assertions and browser interaction testing. PostgreSQL, pgvector, FastAPI, vector embeddings, Figma and fine-tuning were not used in the deployed prototype.

## MCP usage
No runtime MCP server was implemented. Development used connected source-research and hosting tools. This does not make the application itself an MCP server. The optional read-only source MCP interface is planned after the core workflow and review governance are mature.

## Evaluation
60 developer-authored synthetic cases cover document consistency, conditional applicability, unknown/sensitive/negated demands and noisy text extraction. The generated JSON reports actual results and limitations. Raw-image OCR accuracy and independently reviewed citation correctness are not established. Browser QA findings are in docs/QA.md.

## Links and access
- Site: https://civicproof-ai-agi.adilshamim80.chatgpt.site — publication and access status are recorded in docs/QA.md after deployment.
- Live documentation: open Technical docs from the live navigation.
- Evaluation / architecture / design evidence: available through the documentation portal and source ZIP.
- GitHub: not published; a writable target repository is required.
- Figma: none; the working application and actual screenshots are the design evidence.
- YouTube: not recorded or uploaded. VIDEO_SCRIPT.md supplies a 175-second target storyboard and narration.

The Site starts private. Judge access is not implied by a working owner preview. Do not submit a private link as publicly accessible without configuring the intended audience through the owner's authorized sharing workflow.

## Honest remaining work
Qualified specialist review of rules; current circular ingestion; more representative OCR and semantic evaluation; a connected LLM if justified; authenticated production case storage and rate controls; GitHub target publication; recorded YouTube video; confirmed judge access. No claims of users, partnerships, legal authority or competition outcomes are made.
