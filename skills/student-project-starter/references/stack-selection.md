# Choose the smallest useful stack

The table is a decision aid, not a bundle to install. Respect explicit choices; explain material mismatches before proposing changes.

| Need | Recommend | Decision boundary |
| --- | --- | --- |
| Web app, SEO pages, dashboard | Next.js + TypeScript; Vercel as proposed host | Next.js handles ordinary server routes too. A static landing page needs no database or login. |
| Native iOS/Android app with JS/TS | React Native + Expo + TypeScript | Check native modules, offline behavior, and development builds. Shipping involves store setup; OTA updates cannot replace every native change. |
| Persistent relational data, login, or realtime | Supabase for the required features | Auth alone does not make data private: design row-level security. Realtime is optional. Local-only prototypes may need no hosted database. |
| Solo developer, low operations burden | The needed client(s), hosted Supabase if needed, and managed hosting | Serverless is an operating model, not three mandatory products. Use Expo only for mobile. Limits, billing, configuration, and access control remain. |
| Scheduled tasks and multi-service automation | n8n | Coordinate APIs and workflows. CPU-heavy rendering/training needs suitable compute; n8n can trigger it. Cloud and self-hosted n8n have different costs and operating work. |
| An event should wake an existing Grok Bot to perform a task | Grok Bot webhook routine | Use its owning Bot and a narrowly defined routine. An existing backend, script, or n8n can send the event. This is separate from calling the xAI model API. |
| An event should start a coding/review workflow in Cursor | Cursor Automations webhook | Trigger a configured cloud automation with a defined task and repository access where needed. It is separate from local editor hooks and completion callbacks; review account availability and usage costs. |
| File/image uploads or object storage | Cloudflare R2 when its economics or architecture fit | If Supabase is already selected and uploads are small, offer Supabase Storage as simpler. Choose one. R2 is object storage, not image/video processing. |
| Separate distributed API/webhook logic | Cloudflare Workers | Prefer existing Next.js routes for ordinary web APIs. Check runtime/CPU limits and placement near data; edge functions do not guarantee faster database requests. |
| Domain and DNS/edge routing | Cloudflare DNS when requested | DNS does not buy a domain or host the app. Proxying/TLS are separate settings. Preserve existing mail records. |
| Web SaaS billing or eligible physical purchases | Stripe | Start in test mode. Confirm account/country support and product type. Subscriptions need lifecycle handling. |
| Digital content/features purchased in a mobile app | Apple In-App Purchase / Google Play Billing, subject to current storefront rules | Ask product type and target market. Verify regional exceptions before routing to external payments. Not all mobile payments use store billing. |

Choose by product surface. `web-and-mobile` is for two distinct experiences needed now. A phone-friendly website is `nextjs-web`. An API needs no frontend; an automation needs no web framework.

For either agent webhook, select its [Grok Bot](../sub-skills/grokbot-webhook/SKILL.md) or [Cursor](../sub-skills/cursor-automation-webhook/SKILL.md) playbook. Reuse a trusted sender in the approved stack. A single trigger does not require n8n, Workers, Supabase, or a frontend. Explain who can trigger the agent, what it may change, and where the student will inspect the result.

Explain cost drivers without inventing a quote: hosting eligibility, database/storage usage, workflow executions, payment fees, and app-store accounts. State currency and date if quoting amounts. Verify [Vercel Hobby eligibility](https://vercel.com/docs/plans/hobby) before suggesting it for a commercial project; [R2 pricing](https://developers.cloudflare.com/r2/pricing/) includes storage/operation charges despite free direct egress.

## Official sources to open when relevant

- [Next.js setup](https://nextjs.org/docs/app/getting-started/installation), [Expo setup](https://docs.expo.dev/get-started/create-a-project/)
- [Supabase pricing](https://supabase.com/pricing), [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [n8n pricing](https://n8n.io/pricing/), [n8n self-hosting](https://docs.n8n.io/hosting/)
- [Grok Bot routines and webhooks](https://docs.x.ai/grok-bot/skills-routines-and-automations), [Cursor Automations](https://cursor.com/docs/cloud-agent/automations)
- [Workers limits](https://developers.cloudflare.com/workers/platform/limits/), [Cloudflare DNS](https://developers.cloudflare.com/dns/)
- [Stripe availability](https://stripe.com/global), [Stripe pricing](https://stripe.com/pricing)
- [Apple payment rules](https://developer.apple.com/app-store/review/guidelines/#payments), [Google Play payments](https://support.google.com/googleplay/android-developer/answer/9858738)

These are starting points, not cached promises about versions, prices, or policies. Recheck the relevant page during recommendation or setup.
