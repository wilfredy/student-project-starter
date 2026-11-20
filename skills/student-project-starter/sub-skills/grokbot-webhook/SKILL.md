---
name: grokbot-webhook
description: Add an approved Grok Bot webhook routine sender to a student project, or create a standalone sender with local mock verification.
---

# Grok Bot webhook playbook

Use after the stack and local setup are approved. Read [shared setup](../../references/setup-common.md) and [webhook senders](../../references/webhook-senders.md). Here Grokbot means the Grok Bot product and its routines, not the xAI chat/completions API.

1. Identify the owning Bot, event, intended task, and expected result. An example is turning a submitted study question into a draft study plan in the Bot's conversation. Reuse an existing routine if suitable. Record whether live triggering is authorized.
2. Recheck the current [Grok Bot routine/webhook guide](https://docs.x.ai/grok-bot/skills-routines-and-automations). Ask the owning Bot to create a narrowly scoped webhook routine when that remote change is authorized. If no connected tool can manage it, give the student the task instruction to enter in Grok Bot; do not invent a routine or tool call. The trusted routine instruction should specify the payload fields, output, and allowed actions.
3. Guide private configuration from the routine's Webhook panel: its URL and secret key. Use `GROKBOT_WEBHOOK_URL` and `GROKBOT_WEBHOOK_KEY` only in the trusted sender. Send JSON by POST with `Authorization: Bearer <key>` as currently documented. Copy the actual URL; do not construct one from a Bot name or confuse the copied full header with the raw key.
4. Build the smallest sender from the shared contract, a dummy event fixture, and a mock test. A web/mobile UI shows configuration or pending/result status without receiving the provider key. With missing credentials, keep mock mode explicitly local and label the live path unconfigured.
5. When a live check is authorized, trigger once with a harmless task. HTTP 200 indicates a started run; inspect the Bot's conversation for the result. Diagnose a non-success response using the current docs and routine state instead of repeatedly triggering. A client timeout leaves the outcome unknown.
6. Hand off sender/run instructions, the owning routine, credential status, actual verification evidence, and the routine's pause control. Keep any real routine URL/key out of committed docs.

Completion: the local sender and negative checks work; the live routine result is verified or explicitly pending. Do not claim that a local mock proves Bot execution.
