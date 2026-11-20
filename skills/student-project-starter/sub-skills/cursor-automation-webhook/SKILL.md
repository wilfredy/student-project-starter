---
name: cursor-automation-webhook
description: Add an approved Cursor Automations webhook sender to a student project, or create a standalone sender for a configured cloud agent task.
---

# Cursor Automations webhook playbook

Use after the stack and local setup are approved. Read [shared setup](../../references/setup-common.md) and [webhook senders](../../references/webhook-senders.md). This starts a cloud automation; local Cursor editor hooks and outbound completion callbacks are different integrations.

1. Define one task, the triggering event, result location, and repository access if needed. An example is analyzing a submitted bug report and returning findings. Specify whether the agent may propose changes or open a draft PR; preserve existing authorization for those actions. Account access and accepted usage costs are prerequisites for a live run.
2. Recheck [Cursor Automations](https://cursor.com/docs/cloud-agent/automations). In the automation UI, configure a webhook trigger and trusted task prompt, review repository/tools permissions, and save within authorization. If the assistant lacks a management tool, guide the student through these steps. Installing this local skill does not create a cloud automation.
3. Use the saved URL and Generate auth header control. Store `CURSOR_AUTOMATION_WEBHOOK_URL` and `CURSOR_AUTOMATION_WEBHOOK_KEY` in the trusted sender. POST JSON with Bearer auth. A copied full header already contains the header name and Bearer prefix; store only its token in the key variable. Do not request a broad admin key for this beginner flow.
4. Define event fields for the task. Cursor accepts a string `context` field alongside other JSON fields; keep it server-authored and place untrusted submissions in separate fields. Implement the shared sender contract and a local mock. Treat HTTP 200 plus `backgroundComposerId` as a started agent, retain that correlation ID, and inspect the run's output before reporting completion.
5. Default to one send. Documented idempotency behavior applies to automations created by a Project; verify applicability before relying on it. For other senders, implement appropriate deduplication locally. Show sanitized actionable errors and inspect run history after an uncertain timeout.
6. With live authorization, send one benign fixture and inspect the automation's actual result. Record the tested task and what remains unverified. If completion callbacks are also requested, separately follow [Cursor's outbound webhook documentation](https://cursor.com/docs/cloud-agent/api/webhooks), including raw-body signature verification; the trigger key is not a callback signing secret.
7. Hand off the sender command/UI, configuration status, automation run history, and how to disable the automation. No live access means local sender verification only.

Completion: the sender and negative checks work; cloud execution is verified or explicitly pending. A trigger receipt alone never proves a code change, successful test suite, or completed workflow.
