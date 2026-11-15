# Vercel deployment (GitHub checkout)

This repository now defaults to native Next.js on Vercel. `npm run build` runs `next build`, which produces `.next`; it does not import `vite.config.ts` or require `.openai/hosting.json`.

- Framework preset: Next.js
- Build command: `npm run build`
- Output directory: `.next`
- Install command: default (`npm install` / `npm ci` with the committed lockfile)
- Node.js: 22.x
- Root directory: repository root

`vercel.json` declares the framework, build command and output directory. The Node major is pinned in package.json and the lockfile. The catch-all app page restores the dashboard and all citizen routes omitted from the GitHub upload. PDF.js external loading is marked for both the Next.js and Vite bundlers.

The production build and all 11 primary HTML routes plus the real API handler passed locally on 15 November 2026. Remote Vercel deployment must be verified after these changes reach main; local success is not a claim that the remote deployment has completed.

The original Sites scripts are available as `dev:sites`, `build:sites`, and `start:sites`. They require their original Sites manifest and runtime configuration; the GitHub upload omitted that manifest. Standard Next.js type checking excludes Worker-only build configuration. Do not add a fabricated Sites project ID to fix Vercel.

## Original Sites target (separate deployment)

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
