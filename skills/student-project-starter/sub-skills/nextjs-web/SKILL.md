---
name: nextjs-web
description: Set up the approved Next.js web preset within Student Project Starter after stack and local setup approval.
---

# Next.js web preset

Use [shared setup](../../references/setup-common.md). Result: a TypeScript Next.js app with one working page/action, optional approved services, and beginner docs.

1. Check the current [installation guide](https://nextjs.org/docs/app/getting-started/installation) and scaffold help. Use a supported Node LTS. Starting command, subject to current CLI support: `npx create-next-app@latest PROJECT_NAME --ts --eslint --app --src-dir --use-npm --import-alias "@/*"`. Choose Tailwind only if useful to the approved design. Replace `PROJECT_NAME` with the actual destination. Control prompts so the generator does not deploy or overwrite files.
2. Keep App Router structure. Build the home page/core interaction in the generated app directory. Public content gets metadata and semantic headings. Landing pages can use local content/links without accounts, databases, or keys.
3. Put trusted operations in route handlers/server code. Add selected Supabase auth/data using its SSR approach. Add selected R2/Stripe/n8n through [integrations](../../references/integrations.md). A Next.js backend normally makes a separate Worker unnecessary.
4. Provide `.env.example` only when settings are needed. Runtime values go in `.env.local`; public prefixes are for browser-safe values. Unconfigured services display a clear setup/demo state instead of crashing the page.
5. Run actual lint/type scripts and a production build. Do not assume an obsolete `next lint` exists. Start the local server, request the home page, and check its core link/form/action. Verify selected integrations or report them pending. Stop test servers unless leaving one running is useful and disclosed.
6. Hand off exact folder, scripts, verified URL, and a simple edit. Explain proposed Vercel deployment and check plan eligibility when discussing price. Publishing is a separate authorized action.

Completion: local page/action works, checks pass or have precise limitations, docs exist, and needed configuration is set or named as pending.
