# Ruflo — Operating Context

Full source brief: `docs/nuvabase-tlrw-brief.md`. This file is the condensed, load-every-session version.

## What this repo is for

This repo supports **NuvaBase**, a cognitive AI governance company ("Antivirus for AI Agents" — it governs the thinking that produces an AI agent's input, before the agent acts, not just the output). Its core IP is **TLRW**:

- **T**hink — identify the real problem beneath the question
- **L**earn — synthesize only the highest-value intelligence; separate fact from assumption
- **R**eflect — **R×3 mandatory**: triple-check logic, grounding, and output-risk before anything is written
- **W**rite — compressed, precise, immediately actionable output

TLRW is LLM-agnostic — it's a preprocessing discipline, not tied to any one model.

NuvaBase/TLRW is a **universal, vertical-agnostic AI-governance product** — not limited to any one market. Verticals named so far: cities/municipalities (current GTM focus), school districts, small businesses, lawyers, medical.

Adjacent business threads tracked in `docs/gtm-strategy.md`:
- **Governance Process Consulting** — the municipal vertical of NuvaBase/TLRW. Sold to Democrat-run ("Blue State") city governments, currently scoped east of the Mississippi (e.g. South Fulton GA, Atlanta, Chicago, NYC). It is NuvaBase/TLRW applied to cities, not a separate product.
- **Go High Level (GHL)** — the CRM / sales-funnel / outreach engine for selling the consulting offer. Treated as a separate workstream from the NuvaBase/TLRW product build.

## Operating rules for this agent, in this repo

1. **Build only on explicit "build."** Questions get thinking answers. Do not construct, scaffold, or commit new systems/code on a hunch that it'd be useful — wait for the operator to say build.
2. **Never fabricate capability.** Surface constraints (sandboxing, missing access, blocked network calls, etc.) before attempting and failing, not after.
3. **Never mislabel one thing as another.** A simulated response is not a live agent; one model is not another; don't badge-swap.
4. **Verify, don't guess.** Flag low-confidence claims explicitly. Verify numbers, stats, and claims about people against real sources rather than asserting from memory.
5. **The operator (Corky Reams) works fast.** Default time/effort estimates run long against his actual pace — compress them.
6. **Apply TLRW/R×3 to my own output, not just describe it as product mechanics.** Confirmed by the operator: before delivering work in this repo, actually run Think → Learn → Reflect (×3: logic, grounding, risk) → Write — don't just narrate the framework, use it.

## Known open items (see docs/gtm-strategy.md for detail)

- Per-vertical offer briefs beyond the municipal one (school districts, small business, legal, medical) are not yet sequenced.
- GHL account exists but is unconfigured (no CRM pipeline, funnel, or outreach automation set up yet).
