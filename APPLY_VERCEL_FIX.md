# CivicProof AI — Vercel deployment fix

The old package ran a Vinext / Cloudflare build. Vercel identified a Next.js app but received the wrong build target, which tried to load the omitted .openai/hosting.json. Adding that missing file alone would still leave the wrong Vercel build output.

## Apply using GitHub upload

1. Extract CivicProof_AI_Vercel_Fixed.zip.
2. Open your CivicProof_AI repository. Upload the CONTENTS of the extracted CivicProof_AI folder into the repository root, preserving app/, components/ and scripts/ subfolders. Do not upload the ZIP itself or add an extra outer folder.
3. Commit to main. The existing Vercel integration should trigger a new deployment.

Vercel configuration is included: framework Next.js, build command npm run build, output directory .next, Node 22.x. Keep the project Root Directory at the repository root. No API keys or .openai/hosting.json are required for this synthetic demo.

If using GitHub's editor, preserve the exact route filename app/[...slug]/page.tsx. Uploading only root configuration files will fix the build target but leave the citizen subpages missing.

## Apply with Git instead

CivicProof_Vercel_Fix.patch inside the archive changes only the deployment fix files, documentation, and production smoke test. From a clone of Shamimhasan8/CivicProof_AI:

    git apply --check CivicProof_Vercel_Fix.patch
    git apply CivicProof_Vercel_Fix.patch
    npm ci
    npm run build
    npm test
    npm run test:production
    git add package.json package-lock.json tsconfig.json vercel.json app components/civic/app.tsx scripts/verify-production.mjs README.md DEPLOYMENT.md
    git commit -m "Fix Vercel deployment with native Next.js build"
    git push origin main

Patch base: 1c2337dd0be5e39ea43be4508276693e113dc911. If main has changed, review the changes rather than forcing an older tree over new work.

## Changes

- Standard dev/build/start scripts now invoke Next.js.
- Original Sites scripts are preserved under dev:sites, build:sites, start:sites.
- vercel.json declares the supported framework and .next output.
- Node major is pinned to 22.x in package.json and the lockfile.
- Worker-only Vite configuration is excluded from the standard Next.js type check.
- The catch-all page route missing from the upload is restored.
- Remote PDF.js import is marked for both Next.js and Vite bundlers.
- Deployment instructions and live technical description reflect the new default target.
- A repeatable production-server smoke test covers primary routes and API behavior.

## Verification

The native Next.js 16.3.4 production build succeeds without any .openai directory. All 60 synthetic cases, API validation, TypeScript checks, and HTTP smoke tests for the 11 primary views and request-checker endpoint pass locally. Remote deployment remains unverified until the fix is committed to the repository and Vercel reports Ready.

The assistant could not commit these changes because the connected GitHub account has read-only access to this repository and the browser has no signed-in GitHub session. No remote commit or successful remote redeployment is claimed.
