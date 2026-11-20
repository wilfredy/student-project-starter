# Configure only what the code uses

Show a short checklist, then ask “Do you already have a [service] account/project? Yes / No” and “Are its required values ready? Yes / No.” Guide acquisition with the links below. Explain that an environment variable is a setting read outside the code.

These names are starter conventions; adapt to existing code. In a multi-app project, put each variable in the app that reads it. Do not collect every key in this table.

| Feature | Variables/settings | Acquisition | Exposure and destination |
| --- | --- | --- | --- |
| Supabase in Next.js | `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY` | Project Connect dialog or Settings → API Keys; [key guide](https://supabase.com/docs/guides/getting-started/api-keys) | Public config in web `.env.local`. A publishable key is not a database password. |
| Supabase in Expo | `EXPO_PUBLIC_SUPABASE_URL`, `EXPO_PUBLIC_SUPABASE_PUBLISHABLE_KEY` | Same project as above | Public config in mobile `.env.local`. Pair with user auth and RLS. |
| Supabase backend | `SUPABASE_URL`, `SUPABASE_PUBLISHABLE_KEY`; `SUPABASE_SECRET_KEY` only for actual privileged operations | Same key guide | Server env or Worker secrets. User-scoped operations normally use the publishable key plus verified user auth. Legacy `anon`/`service_role` names may exist; map intentionally. |
| Separate backend address | `EXPO_PUBLIC_API_URL` or `NEXT_PUBLIC_API_URL` only if used | Verified local/deployed API URL | Public. A phone's localhost is the phone, not the laptop; use a reachable LAN URL locally. |
| R2 through a Worker | Binding such as `UPLOADS` and bucket name | [R2 binding guide](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/) | Resource binding in Wrangler config; no S3 secret needed. |
| R2 S3 API / presigned URLs | `R2_ACCOUNT_ID`, `R2_BUCKET_NAME`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY` | R2 dashboard API token/S3 credentials; [R2 tokens](https://developers.cloudflare.com/r2/api/tokens/) | Access key pair is secret, backend only, restricted to needed bucket/operations. Account/bucket IDs are config. |
| Stripe hosted Checkout | `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `STRIPE_PRICE_ID`, `APP_URL` | Test/sandbox keys, product price, webhook endpoint or CLI listener; [Stripe keys](https://docs.stripe.com/keys), [webhooks](https://docs.stripe.com/webhooks) | Key/signing secret stay server-side. Price ID/URL are config. CLI and deployed webhook signing secrets differ. |
| Stripe client SDK, only if used | `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` or `EXPO_PUBLIC_STRIPE_PUBLISHABLE_KEY` | Stripe test/sandbox publishable key | Public. Hosted Checkout redirect need not use a client SDK/key. |
| Mobile digital billing | App bundle/package ID, store product IDs, chosen SDK's documented public config; private store keys only if backend verification needs them | [Apple IAP](https://developer.apple.com/in-app-purchase/), [Play Billing](https://developer.android.com/google/play/billing), [Expo IAP](https://docs.expo.dev/guides/in-app-purchases/) | Choose exact variables after selecting SDK. Private signing/service-account keys stay in the backend/provider store. |
| App calls n8n | `N8N_WEBHOOK_URL`, `N8N_WEBHOOK_SECRET` if using header auth | Webhook node's test/production URL and credential | Backend only. Use the configured header. API keys are only needed for workflow management via API. |
| Grok Bot webhook sender | `GROKBOT_WEBHOOK_URL`, `GROKBOT_WEBHOOK_KEY` | Owning Bot → routine → Webhook; copy URL and key separately. [Grok Bot playbook](../sub-skills/grokbot-webhook/SKILL.md) | Private server/script config in `.env.local` or Worker `.dev.vars`; for n8n, keep the key in credentials. Use the key as Bearer auth. |
| Cursor Automation sender | `CURSOR_AUTOMATION_WEBHOOK_URL`, `CURSOR_AUTOMATION_WEBHOOK_KEY` | Save the webhook automation, then Generate auth header. Store only the token as the key. [Cursor playbook](../sub-skills/cursor-automation-webhook/SKILL.md) | Private server/script config or provider/n8n credential store. A webhook trigger key is distinct from an outbound callback signing secret. |
| Self-hosted n8n, if chosen | `GENERIC_TIMEZONE`, optionally `N8N_ENCRYPTION_KEY`, plus deployment settings from current docs | Student's timezone; generate a strong local encryption key if used | Keep encryption key private, stable, and backed up with persistent data; service credentials belong in n8n's credential store. |
| Deploy/DNS | Provider login/project IDs; scoped automation tokens only if required | Provider dashboard/CLI | Deployment tooling only. Vercel/Cloudflare tokens never belong in client runtime config. Local setup usually needs neither. |

## Entry and verification

1. Derive required/optional keys from implemented code. Create `.env.example` with comments and blank values; Workers use `.dev.vars.example`. No external settings means no keys to request.
2. Merge ignore rules before adding values: `.env`, `.env.*`, `!.env.example`, `.dev.vars`, `.dev.vars.*`, `!.dev.vars.example`, plus credential files actually used. Preserve existing rules. Verify examples remain trackable and real files are ignored. Existing tracked secrets require separate cleanup/rotation.
3. Prefer a private local editor or provider secret UI. Copy a template only if the destination is absent; otherwise merge missing names without overwriting values. Restrict Unix secret files to owner access. Keep secrets out of command arguments, prompts, docs, tool output, and chat. If a secret arrives in chat, do not echo it; advise replacing it and enter its replacement privately.
4. Explain where each value comes from; wait for “done” or a status response when human entry is needed. Continue unrelated checks. Guide account creation if needed; create hosted resources only with authorization.
5. Verify presence, formatting, and required connection behavior. Report `VARIABLE_NAME: set / missing / invalid`; suppress values in logs/errors. `NEXT_PUBLIC_` and `EXPO_PUBLIC_` values ship to users. Check that private keys have no path into client bundles regardless of their names.
6. Restart/reload as needed and test the integration. Separate local/preview/production values. Keep examples in sync with code.

Sources: [Next.js env](https://nextjs.org/docs/app/guides/environment-variables), [Expo env](https://docs.expo.dev/guides/environment-variables/), [Workers secrets](https://developers.cloudflare.com/workers/configuration/secrets/). Follow current framework guidance for loading/builds.

For the two agent webhook senders, neither URL nor key belongs in `NEXT_PUBLIC_` or `EXPO_PUBLIC_` variables. A standalone script must explicitly load its private environment file with a runtime-supported method; merely creating `.env.local` does not load it. Use separate names/credentials when both providers are selected.
