---
name: web-and-mobile
description: Set up approved distinct Next.js web and Expo mobile apps with a shared backend within Student Project Starter.
---

# Web and mobile preset

Use when both experiences are in the approved first version. A responsive website alone uses the web preset.

1. Apply [shared setup](../../references/setup-common.md). Put [Next.js](../nextjs-web/SKILL.md) in `apps/web` and [Expo](../expo-mobile/SKILL.md) in `apps/mobile`; docs go at root. Separate manifests/lockfiles are acceptable for a beginner. Avoid adding a monorepo framework merely to house two apps. If using workspaces, configure them consistently with current Expo guidance and one deliberate package-manager strategy.
2. Reuse one Supabase project for shared accounts/data if needed. Root `supabase/migrations/` owns schema changes. Share data contracts/schema; React DOM components do not automatically run in React Native. Add a shared package only for actual reusable code.
3. Pick one approved trusted backend for secrets. Next.js routes can serve both clients; use a Worker only if selected. Verify mobile user tokens and enforce authorization. Backend secrets and client public config stay separate. CORS is not authentication.
4. Implement the approved core action on both surfaces. Put env examples in each app with clear placement instructions. A physical phone uses a reachable LAN backend address, not the laptop's `localhost`.
5. Run both preset checks. If sync is selected and configured, verify a record created in one client appears for the authorized user in the other. Record missing native/service checks.
6. Hand off root README with both working-directory/start commands, shared data flow, and distinct release paths.

Completion: both apps run, backend/configuration agree, and handoff distinguishes both previews and unverified integrations.
