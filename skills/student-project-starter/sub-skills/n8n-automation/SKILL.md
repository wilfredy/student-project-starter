---
name: n8n-automation
description: Set up an approved automation-only n8n project with a dry-run workflow and student handoff within Student Project Starter.
---

# n8n automation preset

Use [shared setup](../../references/setup-common.md). Result: an importable workflow and a local or authorized hosted dry run, without unnecessary app frameworks.

1. Define trigger, input, transformation/action, expected output, and duplicate/failure behavior. Use an existing n8n instance, accepted n8n Cloud setup, or approved local Docker setup. Self-hosting is operating work, not managed serverless hosting.
2. For Docker, check current [n8n installation](https://docs.n8n.io/hosting/installation/docker/) and stable image/version. Write minimal `compose.yaml` for selected capabilities, persistent volume, localhost-bound port, and student timezone. Do not import unrelated AI/sandbox services from a broad example. Protect persisted credentials/encryption data. Validate with `docker compose config --quiet` without printing expanded secrets. If Docker is missing, prepare files and mark runtime checks pending.
3. Create `workflows/main.json` as a valid inactive importable workflow with a manual/test trigger and `fixtures/sample-input.json`. Use current node types/versions. Include intended trigger config if known; keep sending/spending/scheduling actions disabled until authorized. Use a dummy sink in the dry run.
4. Follow [n8n integration guidance](../../references/integrations.md) for auth, credentials, retries, and exports. Request only services actually called. Use n8n credentials for secrets; manual import needs no n8n API key.
5. Validate JSON, import into a local or authorized test instance, run the fixture, and compare expected output. Syntax checks do not prove import/execution. Without an instance, mark them unverified and provide exact import/run UI steps. A workflow file is not an active workflow.
6. Hand off files, startup/stop commands if applicable, instance URL, import steps, and test versus active production webhooks. Explain authorization still needed for real actions/activation.

Completion: workflow/docs are usable, dry-run evidence is recorded or explicitly pending, and activation/actions stay within scope.
