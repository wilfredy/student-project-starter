---
name: workers-api
description: Set up an approved Cloudflare Workers API or trusted mobile backend within Student Project Starter.
---

# Workers API preset

Use [shared setup](../../references/setup-common.md). Result: a local TypeScript Worker with a health endpoint and approved API behavior.

1. Check current [Workers setup](https://developers.cloudflare.com/workers/get-started/guide/) and generator help. Start with `npm create cloudflare@latest -- PROJECT_NAME`, select a minimal TypeScript Worker, and decline deployment. For automation, verify noninteractive flags and explicitly disable deployment. Local setup needs no hosted Worker.
2. Use generated entrypoint/Wrangler config. Add `GET /health` returning JSON plus the core endpoint. Validate inputs/status codes, verify identity/authorization for private operations, and allow only intended browser origins if CORS is needed.
3. Add approved bindings. Prefer R2 bindings over S3 credentials in Workers. Supabase operations preserve user scope; use privileged secrets only where required with explicit authorization checks. Local secrets go in `.dev.vars`, names in `.dev.vars.example`; deployed secrets use the provider store after authorization.
4. Generate binding types, type-check, and run relevant endpoint tests. Start local Wrangler with remote bindings disabled; request health/core endpoints and an invalid or unauthorized case. Use a dry-run bundle command if supported; dry run is not deployment.
5. Hand off local command/URL and an example request without credentials. Prepare deployment/binding instructions; deploy only within authorization.

Completion: local API behavior and relevant negative cases pass; remote resources/credentials are configured or precisely pending.
