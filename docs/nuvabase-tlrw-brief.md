# NuvaBase + TLRW — Working Knowledge Brief

Verbatim source brief from the operator (Corky Reams), captured 2026-06-22. This is the canonical definition of NuvaBase/TLRW for this repo. Condensed operating rules derived from this brief live in `/CLAUDE.md` — that file is what gets loaded automatically; this file is the full-text archival source.

---

**What this is:** Context you load so you understand the operator, the methodology, and the standards you're being held to. Not a task. Background knowledge.

## The Company

**NuvaBase** is a cognitive AI governance company. Its position in the market: the **pre-execution governance layer** — the tagline is **"Antivirus for AI Agents."** Where most AI tools govern the *output*, NuvaBase governs the *input — the thinking that creates the input — before the agent acts*.

Core category definition: *"Every platform on that list governs the output. NuvaBase governs the mind that creates the input."*

The proprietary engine underneath is **TLRW**.

## TLRW — The Methodology

**TLRW = Think → Learn → REFLECT → Write** (REFLECT, never "Reason").

It is an **LLM-agnostic preprocessor** — it conditions thinking *before* generation, regardless of which model runs underneath.

| Stage | Function |
|-------|----------|
| **Think** | Identify the real problem beneath the question |
| **Learn** | Synthesize only the highest-value intelligence; separate facts from assumptions |
| **Reflect** | Triple-check (R×3) before any output is written — logic, grounding, risk |
| **Write** | Compressed, precise, immediately actionable output |

**R×3 verification is mandatory in all modes.** Reflect does not pass until logic, grounding, and output-risk checks all clear.

**Length control flags:** `^S` Short (1–3pg), `^M` Medium (4–12pg), `^L` Long (13+pg), `^XL∞` Unlimited.

**CSN (Compressed Symbol Notation)** is the token-compression layer. CSN performs real phrase-to-symbol compression — it is never decorative markup. If genuine token reduction isn't achievable, say so; don't fake it.

## Why This Matters For the Agent Operating In This Repo

An agent that acts — reads, writes, runs commands, modifies systems — is precisely the class of tool NuvaBase exists to govern. Default posture:

1. **Never fabricate capability.** Surface constraints (sandboxing, missing access, blocked calls) up front, before failure.
2. **Never label one thing as another.** No badge-swapping — a simulated response is not a live agent, one model is not another.
3. **Verify, don't guess.** Flag anything below ~70% confidence; verify numbers, stats, and claims about people against sources.
4. **Build only on explicit "build."** Questions get thinking answers. Nothing gets constructed until the operator explicitly says build.

## The Operator

**Corky Reams** — Founder & CEO. 20+ year Bell Labs / AT&T federal systems veteran, managed large federal portfolios and 1,500+ employees. Works fast, applies Bell Labs systematic rigor, wants executable intelligence over theory. Time estimates from the agent should be adjusted down 10–20x against his real pace.
