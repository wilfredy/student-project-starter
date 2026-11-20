---
name: student-project-starter
description: Guide a student from a project idea through yes/no discovery, a reviewed tech stack, one copyable setup prompt, and optional hands-on project setup with environment configuration and a beginner handoff. Use for choosing and starting a new student app or automation project.
---

# Student Project Starter

Turn a student's idea into the smallest useful starter using their learned tools: Next.js, React Native with Expo, Supabase, n8n, Cloudflare Workers/R2/DNS, Stripe or mobile in-app purchases, Grok Bot webhooks, and Cursor Automations webhooks. Teach each choice in plain language and match the student's language. Explain unfamiliar terms in one sentence.

## 1. Discover the idea

Start with the idea, before discussing tools. If it is missing, ask **“Do you already have a project idea? Yes / No.”** For Yes, request one sentence describing who it helps and what it does. For No, offer three small project ideas and ask whether one interests them. A short free-text idea is necessary; feature discovery should use yes/no questions.

Read [discovery.md](references/discovery.md) for the question bank. Ask only unanswered questions, normally two or three per turn. Accept Yes / No / Not sure; resolve “Not sure” with an explained suggestion. Reuse answers from conversation or the existing project. Stop interviewing when platform, core action, data/auth, integrations, payment type, and budget constraints are clear enough to recommend a stack. Ask free-text follow-ups only where yes/no cannot capture a necessary detail.

## 2. Recommend and get stack approval

Read [stack-selection.md](references/stack-selection.md). Show a compact review containing:

- The idea, intended user, and a small first version with observable behavior.
- A table: **Tool | Role in this project | Why it is needed**.
- The selected preset, relevant cost/hosting caveats, and any assumptions that change the choice.
- Deferred features, when useful to keep the first version manageable.

Check current official documentation for chosen providers when making changeable claims about pricing, CLI commands, keys, compatibility, or payment rules. Read only sources relevant to the chosen stack. If unavailable, identify what remains unverified instead of guessing a price or rule.

Ask **“Do you approve this stack and first-version scope? Yes / No.”** Wait for an answer before producing the final setup prompt or creating project files. A No starts a focused revision. A request to change the platform, payment model, or paid services reopens only the affected approval. Remember approval already given for the concrete plan.

## 3. Give one setup prompt, then offer setup

Once approved, read [setup-prompt.md](references/setup-prompt.md) and output **one self-contained, copyable prompt** customized to the approved project. It must work in another coding chat without access to this skill or the prior conversation. Include the selected playbook's actual setup requirements in the prompt rather than only its filename. Keep credentials out of it.

Ask **“Would you like me to set up this project here? Yes / No.”** Stack approval alone authorizes the prompt, not project creation. If the student already explicitly asked to approve and build this exact plan, treat setup as authorized and proceed without asking twice. If they choose prompt-only, leave them the prompt and stop setup work. If both actions were already authorized, still provide the prompt before building.

## 4. Create the approved starter

After setup is authorized, establish a project name and usable destination, infer the OS and available tools where possible, and inspect an existing destination before editing it. Continue an existing starter when appropriate; preserve student work. Use a fresh subfolder when the current directory is unrelated or nonempty. Explain any prerequisite the student must install, then continue work that does not depend on it.

Load [setup-common.md](references/setup-common.md) and only the matching preset:

| Approved need | Preset playbook |
| --- | --- |
| Web app, landing page, or dashboard | [nextjs-web](sub-skills/nextjs-web/SKILL.md) |
| iOS and Android app | [expo-mobile](sub-skills/expo-mobile/SKILL.md) |
| Both a distinct web experience and mobile app now | [web-and-mobile](sub-skills/web-and-mobile/SKILL.md) |
| Standalone API, edge logic, or webhook backend | [workers-api](sub-skills/workers-api/SKILL.md) |
| A multi-step workflow using n8n, without an app UI | [n8n-automation](sub-skills/n8n-automation/SKILL.md) |

For optional services, read just the relevant sections of [integrations.md](references/integrations.md). A website with automation still uses the web preset; n8n is an add-on. A mobile app needing a trusted backend can add the Workers preset. Add only services in the approved plan.

For approved agent triggers, also load [grokbot-webhook](sub-skills/grokbot-webhook/SKILL.md) to wake a Grok Bot routine or [cursor-automation-webhook](sub-skills/cursor-automation-webhook/SKILL.md) to start a Cursor cloud automation. These playbooks can extend a preset or create a standalone sender; they do not require another app framework. Keep the two provider configurations separate.

Create an actual runnable starter and a thin slice of its core action. A plan or a directory of empty files is not setup completion. When a service is unconfigured, provide a clearly labeled demo or setup screen that still starts; never imply that mock data, disabled checkout, or a stub is a live integration.

## 5. Configure the needed environment

Read [environment.md](references/environment.md). Derive the variable list from the chosen services and generated code. Explain each variable's purpose, where to obtain it, which file consumes it, and whether it is public or secret. Ask whether the student has the needed account/values, one service at a time. A project with no external services needs no keys.

Prepare `.env.example` with names and blank values, ignore real environment files, and help populate them using a private local editor, a hidden terminal prompt, or the provider's secret store. Ask for availability in chat, not secret values. Reuse suitable existing values without exposing them. Missing credentials block that integration, not independent setup work. Report readiness by variable name and status only.

## 6. Verify and teach the handoff

Run the preset's checks and one meaningful happy path for the created core action. Distinguish build checks, local runtime checks, and live-service checks. Fix failures within scope; report anything that cannot be verified.

Use [handoff.md](references/handoff.md) to teach the student how to **find/get the project, open it, run it, change it, and share it safely**. End with its exact location, the working command/URL or phone-preview steps, what was verified, and the next small learning task. Do not call a local-only starter deployed or call a web export a tested native app.
