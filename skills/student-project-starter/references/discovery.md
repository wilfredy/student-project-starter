# Student discovery

Use these as an adaptive question bank, not a mandatory questionnaire. Ask in everyday language; map answers to tools yourself. Start with the idea as described in the parent skill. Ask the provider-specific agent questions only when the idea or automation answers suggest an agent task.

| Decision | Yes/no question | Follow-up only if needed |
| --- | --- | --- |
| First version | “Should the first version focus on [one concrete action]?” | Suggest a smaller version if the idea is too broad. |
| Mobile | “Must people install it as an iPhone/Android app?” | Which devices, if it changes testing or features. |
| Web | “Does it need its own website or browser dashboard?” | “Should public pages appear in Google search?” |
| Accounts | “Do people need to sign in?” | “Should each person see only their own records?” |
| Saved data | “Should information stay saved and sync across devices?” | Local-only data may not need a backend. |
| Realtime | “Must changes appear immediately for other users?” | Identify the actual live interaction. |
| Uploads | “Will people upload photos, videos, or documents?” | Approximate size/volume only when consequential. |
| Automation | “Should something happen automatically later or when another app sends an event?” | Ask the trigger and action; distinguish orchestration from computation. |
| Grok Bot | “Should an event ask your Grok Bot to run a task?” | If yes, identify the owning Bot, event, allowed action, and expected result; ask whether a webhook routine already exists. |
| Cursor Automations | “Should an event start a Cursor cloud agent to work on your project?” | If yes, identify the automation, repository if needed, and whether it should report findings or propose code changes. Check account access and accepted usage costs. |
| API | “Will other apps need to call your API, or do you need a separate webhook backend?” | Ordinary web APIs can stay in Next.js. |
| Payments | “Will users pay in the first version?” | “Are they buying digital features/content inside the mobile app?” then “Physical goods or real-world services?” Clarify mixed cases and target storefronts. |
| Constraints | “Is this a solo project with a small budget?” / “Would you prefer services that manage the servers for you?” | Currency/monthly ceiling, deadline, or team details only when consequential. |
| Hosting eligibility | “Will this be a commercial project?” | Check plan eligibility before calling hosting free. |
| Domain | “Do you already own a domain you want to connect?” | Domain work can wait for a hosting destination. |
| Native complexity | “Does it need offline-first behavior, Bluetooth, background location, or a custom native SDK?” | Review Expo support and development-build needs. |

For uncertainty, explain the tradeoff and suggest a default to approve, e.g. “For this classroom prototype, should we start without login? Yes / No.” Keep unknowns as unknowns until answered or explicitly accepted as assumptions.

If there is no idea, offer a study planner, club event page, or homework reminder automation with one sentence each. Then ask “Would you like to start with the study planner? Yes / No.” Let them choose or describe something else without forcing the suggestion.
