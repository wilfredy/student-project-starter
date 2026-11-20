---
name: expo-mobile
description: Set up the approved React Native and Expo mobile preset within Student Project Starter after stack and local setup approval.
---

# Expo mobile preset

Use [shared setup](../../references/setup-common.md). Result: a TypeScript Expo app with a working main screen/action and accurate preview steps.

1. Read [Expo project creation](https://docs.expo.dev/get-started/create-a-project/) for current Node/SDK requirements. Scaffold with `npx create-expo-app@latest PROJECT_NAME` and the appropriate documented TypeScript/router template. During SDK transitions, choose compatibility with intended Expo Go or development builds; never hardcode a stale SDK from this playbook.
2. Use generated navigation and implement the approved core action. Keep no-account local data local when sync is unnecessary. Add selected Supabase auth/data using its React Native session-storage/refresh guidance.
3. Treat the phone as an untrusted client. Upload signing, Stripe session creation, entitlement verification, and private n8n webhooks need an approved trusted backend. If none was approved, explain and get the amended architecture approved before adding it. `EXPO_PUBLIC_` values are bundled, not secret storage.
4. For digital purchases follow [the IAP integration](../../references/integrations.md). Native libraries can require a development build, not Expo Go. Do not silently add a paid billing service. For physical services verify the appropriate Stripe path.
5. Run TypeScript checks and `npx expo-doctor` if available. Run a suitable platform bundle/export check using current CLI and start Metro with `npx expo start`. Test the screen/action on an available device/simulator. If only bundling is possible, mark device behavior unverified; web export does not verify iOS/Android.
6. Hand off exact commands, QR/device or simulator steps, main screen file, and reload instructions. Explain development builds/store accounts without submitting automatically.

Completion: source/configuration are usable, available checks pass, preview steps fit the native features, and missing device/store checks are explicit.
