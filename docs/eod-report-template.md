# EOD Report — Reusable Template

Structural template only. Copy the layout/format below; do not carry over example content from any prior report when filling it in. Populate every report from that day's actual, verifiable work (commits, docs touched, decisions confirmed, open items) — not invented metrics, fictitious agent swarms, or unverified claims about third parties.

---

```
[REPORT TITLE]
[Subject/Workstream]  |  [Source — e.g. "This Session"]  |  [Tier/Tag, if any]
[Date]  |  [Time + Timezone]  |  Commander: [Name]  |  Governor: [Name/Model]
[OVERALL STATUS LINE — e.g. N COMMITS | N DOCS TOUCHED | N OPEN ITEMS]

I. EXECUTIVE SUMMARY — THE SESSION
[What happened, when, scope, and the 2-3 headline outcomes. State plainly what's
done vs. still open — don't inflate completion or certainty.]

CRITICAL FINDING / OUTCOME | STATUS | NEXT ACTION
[finding/outcome]          | [status tag] | [next action, or "none — closed"]
...

II.–N. WORKSTREAM BLOCKS (one per initiative/lane actually worked)
Status: [done / in progress / blocked / open]. [1-3 sentence summary, grounded
in what actually happened — cite the file/commit if useful.]

[Sub-table 1 — e.g. decisions confirmed this session]
[ITEM] | [DECISION/RESOLUTION] | [SOURCE]
...

[Sub-table 2 — e.g. ranked items produced, if applicable]
RANK | [ITEM] | [SUPPORTING DETAIL]
...

⚑ OPEN or ⚑ BLOCKED callout — one sentence per workstream still pending,
naming exactly what's missing before it can move.

[Repeat workstream blocks for each thing actually worked: strategy decisions,
docs drafted, research/lists produced, contacts verified, code/scaffolding
added, blockers hit.]

FINAL SECTION — NEXT ACTIONS
# | ACTION | WHY | WHO | WHEN
1 | ...
...

[CLOSING STAMP]
[Status line — e.g. "session complete," any gating condition before next action]
Commander: [Name]  |  Governor: [Name]  |  Executor: [who/what actually did the work]
[Org name]  |  [Location, if relevant]
```

## Rules for filling this in

1. **Ground every line in something real** — a commit, a file, a confirmed decision from this session. If it didn't happen today, it doesn't go in today's report.
2. **No fabricated capability.** Don't claim a multi-agent swarm, a research pass, or a verification step that didn't actually run. If one agent (this session) did the work, say so.
3. **Confidence/status tags reflect actual certainty.** Carry over the confidence/verification levels already on record in the source docs (e.g. `gtm-strategy.md`) rather than inventing new scores.
4. **Open items stay open.** Don't mark something "done" to make the report look cleaner than the work actually is.
