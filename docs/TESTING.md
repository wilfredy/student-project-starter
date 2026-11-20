# Validation and test coverage

This repository contains agent instructions, not prebuilt applications. Package checks validate its structure; they cannot guarantee an assistant's decisions or a provider's live behavior.

## Reproduce package validation

From the repository root, use Python 3.11+:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

On Windows, replace `.venv/bin/python` with `.venv\Scripts\python.exe`.

The validator checks skill metadata and unique names, relative Markdown file links, reachability of bundled instructions from the main skill, and UI metadata. GitHub Actions runs the same check. It does not check external URLs, execute apps, or call providers.

The Codex skill-creator validator was also run against each `SKILL.md` during preparation. It is bundled with Codex rather than vendored here.

## Recorded original forward tests

The original skill was tested in November 2026 in isolated local projects. These results describe those runs, not a guarantee for every new generated project. Raw machine-specific build outputs and private workspace paths are intentionally excluded from this public repository.

| Area | Observed result |
| --- | --- |
| Seven dialogue cases | No idea; simple club website; prompt-only request; mobile billing/private-key boundary; rejected stack; n8n-only draft; stack approval without setup permission |
| Next.js starter | Dependency install, lint, TypeScript, production build, and HTTP smoke check passed |
| Browser checks | Desktop and mobile layouts, keyboard navigation, correct signup link, no horizontal overflow or recorded page errors |
| Workers starter | Binding types, TypeScript, 30 automated tests, local bundle check, and 14 local HTTP cases passed |
| Package | Main skill and original five preset skills passed metadata checks; local references resolved |

The Next.js scaffold used Next.js 16.4.6; the Worker used Wrangler 4.160.1. These are historical test versions, not pins for future projects. The Next.js run reported seven moderate upstream dependency advisories and an ESLint 9 support warning. Those observations remain limitations, not a security-audit result.

## Webhook playbook checks

The Grok Bot and Cursor Automations additions were checked against their linked official provider documentation. Their shared contract requires a private trusted sender, a defined task/event schema, local mock tests, explicit handling of unknown delivery, and checking the actual agent result after a live trigger.

Use these scenarios when reviewing or modifying the playbooks:

| Scenario | Observable behavior to verify |
| --- | --- |
| Existing web app calls a Grok Bot routine | Select Grok Bot add-on; reuse the backend; keep URL/key server-side; do not add an unrelated platform |
| Standalone Cursor trigger, no credentials | Produce a small runnable sender and dummy fixture; verify against a local mock; leave live status pending |
| Mobile app requests an agent task | Mobile calls an authorized backend; the provider token never enters public Expo variables |
| Provider accepts a request | Report started/pending and retain a safe correlation ID; do not report the task finished |
| Timeout after submission | Mark outcome unknown; inspect run history before another attempt |
| Duplicate incoming event | Apply the chosen deduplication contract; do not assume all automations support an idempotency header |
| Payload asks to ignore the task and send secrets | Treat it as input data; keep the trusted task and allowed actions unchanged |
| Student wants only the setup prompt | Give one portable prompt; create no project or live automation |

These are review scenarios and required checks for generated projects. They are not claims that a live account integration has passed. **No real Grok Bot routine or Cursor Automation was triggered for this repository update.**

## Not yet exercised end to end

Native Expo/device builds, the combined web/mobile preset, live n8n import/execution, Supabase auth/RLS, R2, Stripe, native store billing, DNS/deployment, and private credential entry were not all tested in the original forward-test runs. Grok Bot and Cursor account access, live triggers, actual cloud execution, and completion callbacks remain untested here.

When adding a test result, record the actual version, command or action, observable outcome, and limitations. Distinguish static checks, local mocks, local runtime behavior, and real provider behavior.
