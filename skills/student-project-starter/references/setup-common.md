# Shared setup contract

Use after stack approval and setup authorization. Read the selected preset before scaffolding.

1. Inspect the destination, applicable repository instructions, runtimes, and lockfiles. Use the existing package manager; default to npm for a new JS/TS app. Verify scaffold help/docs and compatible stable versions. Preserve existing files and secrets. Scaffold into an empty target; adapt an existing project instead of regenerating it.
2. Make the approved starter and one demonstrable core action. Explain layer boundaries in project terms. Install only necessary dependencies. Include lockfiles in the deliverable; do not commit or push Git changes unless authorized.
3. Add selected [integrations](integrations.md). Prepare example environment files and private entry using [environment.md](environment.md). Missing credentials leave a clearly identified setup/demo state. Never weaken access control or accept real payments to make a check pass.
4. Write `docs/project-plan.md` with the idea, approved scope/stack, data flow, assumptions, and remaining setup. Write `docs/setup-prompt.md` with the filled prompt. Write a project `README.md` using [handoff.md](handoff.md). These files belong to the created project, not the skill package.
5. Run checks from actual package scripts and the preset smoke test. Add focused tests for meaningful custom logic, authorization, payment verification, or substantial integrations. Record failures and fixes; a successful scaffold command alone is insufficient.

Setup authorization covers ordinary local files, package installation, and local checks. Deployment, hosted resources, billing, DNS, existing remote databases, real messages, app submissions, repository pushes, and live charges are distinct actions unless already authorized. Prepare concrete config/migrations/workflows first, then request any missing authorization immediately before that action. Local workflow tests use dummy inputs and no real recipients.

On an unavailable dependency, failed authentication, or denied permission, explain the blocked step and continue independent work. Avoid repeated unchanged retries or substituting approved services without discussion. Mark required unverified checks as partial completion.
