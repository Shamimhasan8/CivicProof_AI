# Deployment

## Current supported target
Sites hosting: Cloudflare Worker ES module built by Vinext. The project ID is preserved in .openai/hosting.json. No D1 or R2 binding is enabled. No paid infrastructure or secrets are required.

1. `npm ci`
2. `npm test`
3. `npm run typecheck`
4. `node /home/agent/.codex/plugins/cache/openai-curated-remote/sites/1.1.6/scripts/build-site.mjs` in this managed environment, or `npm run build` elsewhere.
5. Push the exact source commit using the Sites workflow helper; package dist/ with the tracked manifest.
6. Save and deploy the matching version through Sites. Preserve private audience.

## Runtime environment
No API key is configured. .env.example documents only that fact. Future LLM integration requires provider selection, user-owned credentials, data disclosure review, structured-output validation and evaluation. Never paste secrets into source, the hosting manifest or browser code.

## GitHub
The connected GitHub API did not expose repository creation, no CivicProof repository was found under the supplied account, and gh is not authenticated. Source is versioned in the Site repository and included in the downloadable source archive. A GitHub URL must be added only after a real target repository is created or supplied.

## Rollback
Deploy a previously saved Site version through Sites; do not replace the project ID. Browser case data has no server schema migration. Export before changes that affect session state shape.
