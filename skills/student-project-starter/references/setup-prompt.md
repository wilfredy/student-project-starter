# One portable setup prompt

Fill this template after stack approval. Replace bracketed fields with the student's choices or an explicit unresolved item. Remove inapplicable sections. Output one code block, not competing prompts or separate command blocks. The prompt authorizes local setup when the student chooses to use it; producing it does not itself authorize running it in the current chat.

```text
Act as my patient project setup mentor. Create a runnable starter for this approved project and explain the few steps I need to learn.

Project: [name and one-sentence idea]
Audience and main action: [who does what]
First version: [small list of observable behaviors]
Deferred: [features outside this setup]
Approved stack: [each tool and purpose; proposed hosting; payment mode if any]
Constraints: [OS if known, budget, commercial/personal, platforms, relevant storefronts]
Destination: [chosen directory, or ask where to create it before writing files]

Setup recipe:
[Inline the selected preset's relevant steps: scaffold, layout, core screen/endpoint/workflow, integrations and checks. For selected Grok Bot or Cursor webhooks, include the owning routine/automation, sender location, trusted task, payload contract, private auth, duplicate/timeout handling, and mock-versus-live test boundary. Make this usable without any external skill files. Resolve CLI flags and compatible versions from official docs at setup time.]

Inspect the destination and preserve existing work. Use a compatible stable runtime and official scaffold, record dependency versions in a lockfile, and build the core action above. Add only approved services. If configuration is missing, keep the starter runnable with an explicitly labeled demo or setup state.

Configuration: [exact required variable names, which app/file uses each, public versus secret, and official acquisition links; say “No external keys needed” when applicable]. Create example env files with blank values and ignore real env files. Help me enter secrets privately in a local editor or provider secret store; never ask me to paste them into chat or place them in client code. Report configuration by name/status only.

Write a beginner README explaining how to get/open/run the project, what its main folders do, remaining settings, and a small first exercise. Save the approved scope and this setup brief in the project docs.

Verify: [preset-specific build/type/lint checks and one observable runtime behavior]. Report what passed, what was not run, and what needs an account/device. Do not claim a live connection from a mock or a native test from a web-only export.

This request authorizes local files, dependency installation, and local tests. [Include additional specific actions already authorized.] Prepare deployment instructions; obtain authorization for publishing, paid resources, DNS/account changes, production database changes, repository pushes, and real payments unless I already approved the concrete action. Finish with the exact folder, launch commands, verified preview address/steps, and any remaining action for me.
```

For prompt-only requests, keep all output in chat. When setup is authorized, also save the filled prompt to `docs/setup-prompt.md` in the project.
