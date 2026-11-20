# Optional integration playbooks

Read only sections selected in the approved plan. Use [environment.md](environment.md) for variables and private entry.

## Supabase: saved data and login

Create one relevant entity and version its schema in `supabase/migrations/`. For user-owned data, link ownership to the authenticated user and enable RLS with needed policies/grants. Check with two users that one cannot access the other's private rows. Public reads must be deliberate; do not leave tables open to make the demo work.

Follow current [Next.js SSR integration](https://supabase.com/docs/guides/auth/server-side/creating-a-client?queryGroups=framework&framework=nextjs) for browser/server clients and cookie/session handling, or [React Native Auth](https://supabase.com/docs/guides/auth/quickstarts/react-native) for persistence/refresh. Use trusted server auth verification for protected operations. Add login/logout only if selected. Configure actual redirect/deep-link URLs.

If realtime was selected, subscribe to the required records with access control and subscription cleanup. If Supabase Storage was chosen over R2, match bucket policies to record permissions. Apply remote migrations only after target/operation authorization. Without credentials, provide SQL and a labeled setup/demo path; record live auth/RLS checks as pending.

## R2: uploads

Authorize uploads on a trusted backend. Workers can use an R2 binding; Next.js/server code can issue short-lived [presigned S3 URLs](https://developers.cloudflare.com/r2/api/s3/presigned-urls/). Keep S3 credentials there. Validate identity, ownership, object keys, types, and upload limits. Set browser CORS for the actual origin. Keep private objects private and use authorized backend access or expiring URLs; unguessable names are not authorization.

Store object keys/ownership in the database if selected. Test an authorized upload/download and rejected unauthorized access with a small dummy file. Prepare bucket/CORS config locally; obtain missing authorization before remote changes. Report untested size enforcement rather than claiming client-only checks enforce it.

## n8n: workflow add-on

Create an importable, initially inactive workflow in `automation/` with a dummy event and approved trigger → action path. Use [n8n export/import](https://docs.n8n.io/workflows/export-import/) and current node schemas. Exports contain no real credentials, credential IDs, personal data, or active schedules. Prefer native nodes. Use the credential store and an authenticated webhook called by the app's backend.

Use n8n Cloud if its managed cost is accepted, or explicitly chosen self-hosting. Use bounded retries and deduplication where repeated triggers can repeat real actions. Explain test versus production webhook URLs. Verify dummy dry-run output; messages, paid services, and active schedules need authorization. For automation-only projects use [the n8n preset](../sub-skills/n8n-automation/SKILL.md).

## Grok Bot and Cursor Automations: agent webhook add-ons

Use [grokbot-webhook](../sub-skills/grokbot-webhook/SKILL.md) for a Bot routine and [cursor-automation-webhook](../sub-skills/cursor-automation-webhook/SKILL.md) for a Cursor cloud automation. Each uses the shared [webhook sender contract](webhook-senders.md). In a web app, call from a protected server route; a mobile app calls its trusted backend. In n8n, use an HTTP Request node with a credential, an inactive workflow, and a local mock for the first run. A standalone trusted script is enough when no app is needed.

## Stripe: eligible web/physical payments

Use [hosted Checkout](https://docs.stripe.com/checkout/quickstart) in test/sandbox mode. Create sessions server-side with server-selected prices and trusted customer identity; restrict redirect URLs. Keep the key server-side. For subscriptions define active/past-due/canceled access and include the customer portal when in scope.

Verify [webhook signatures](https://docs.stripe.com/webhooks) against raw bodies. Make fulfillment idempotent; handle delayed success/failure for supported payment methods. Redirects and client “paid” flags are not payment proof. Verify test checkout, a signed webhook, and a duplicate event; never charge a real card for setup. Without test credentials, test local logic with fixtures and mark live integration unverified.

## Mobile digital purchases

Confirm product type/storefronts against current [Apple](https://developer.apple.com/app-store/review/guidelines/#payments) and [Google Play](https://support.google.com/googleplay/android-developer/answer/9858738) rules. Use a compatible StoreKit/Play Billing integration. Extra managed billing services are choices to explain and approve, not implicit dependencies.

Follow [Expo IAP guidance](https://docs.expo.dev/guides/in-app-purchases/) for native development builds. Model product IDs, purchase/restore, pending/canceled states, and trusted entitlement verification. Use sandbox testers and record actual device/store checks. Without accounts/products, create the adapter/UI with an explicit unavailable state; never grant paid access through fake success.

## Cloudflare DNS and hosting

Prepare required records after the hosting destination is known. Show hostname, record type/value, and proxy/TLS choices. Preserve existing records, especially email. Apply only authorized changes; buying a domain, migrating nameservers, and changing a production hostname are distinct operations. Verify resolution/HTTPS after changes. Without deployment authorization, leave proposed records/instructions in the handoff.
