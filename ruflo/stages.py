from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    slug: str
    title: str
    system_prompt: str
    instructions: str


STAGES: list[Stage] = [
    Stage(
        slug="research",
        title="Research & Discovery",
        system_prompt=(
            "You are a research analyst specializing in community-based services "
            "(mutual aid, civic programs, nonprofits, local government, neighborhood "
            "and grassroots initiatives). You investigate problems rigorously: who is "
            "affected, what already exists, where existing approaches fall short, and "
            "what constraints (funding, volunteer capacity, regulation, trust) shape "
            "what's possible. You are concrete and specific, not generic."
        ),
        instructions=(
            "Research the following community need or problem area:\n\n"
            "{topic}\n\n"
            "Produce a research brief covering:\n"
            "1. Who is affected, and how (be specific about stakeholder groups)\n"
            "2. Existing approaches/services that address this today, and their gaps\n"
            "3. Root causes and constraints (funding, trust, logistics, policy)\n"
            "4. Open questions worth validating before designing a solution\n\n"
            "Format as Markdown with headers."
        ),
    ),
    Stage(
        slug="ideation",
        title="Ideation & Strategy",
        system_prompt=(
            "You are a strategist who turns research into actionable concepts for "
            "community-based services. You favor ideas that are feasible for a small "
            "team or community organization to pilot, not ideas that require massive "
            "capital or years of lead time. You weigh impact against effort honestly."
        ),
        instructions=(
            "Given this research brief:\n\n{previous}\n\n"
            "Generate 3-5 distinct service concepts that address the gaps identified. "
            "For each concept give: a name, a one-paragraph description, who it serves, "
            "what makes it different from existing approaches, and a rough feasibility "
            "rating (low/medium/high effort to pilot). Then recommend ONE concept to "
            "carry forward, with a short justification.\n\n"
            "Format as Markdown with headers."
        ),
    ),
    Stage(
        slug="design",
        title="Spec & Design",
        system_prompt=(
            "You are a service designer who writes implementation-ready specs for "
            "community programs and tools. Your specs are concrete enough that a small "
            "team could start building or piloting from them directly."
        ),
        instructions=(
            "Given this strategy output (with its recommended concept):\n\n{previous}\n\n"
            "Write a detailed spec for the recommended concept, covering:\n"
            "1. Problem statement and target users\n"
            "2. Core features / service components (the minimum needed for a pilot)\n"
            "3. Service model: how it's delivered, by whom, and how it sustains itself "
            "(funding, volunteers, partnerships)\n"
            "4. Success metrics for a pilot phase\n"
            "5. Key risks and mitigations\n\n"
            "Format as Markdown with headers."
        ),
    ),
    Stage(
        slug="prototype",
        title="Build & Prototype",
        system_prompt=(
            "You are a builder who turns specs into a concrete first build. If the "
            "spec describes a software tool, sketch a minimal architecture and a small "
            "code scaffold for the highest-leverage piece. If the spec describes a "
            "program or service (not software), produce a concrete pilot rollout plan "
            "instead: first steps, timeline, who does what, and what 'done' looks like "
            "for week one. Choose whichever fits the spec - don't force code where it "
            "doesn't belong."
        ),
        instructions=(
            "Given this spec:\n\n{previous}\n\n"
            "Produce the first concrete build artifact for this pilot: either a minimal "
            "technical scaffold (architecture + key code, if software-shaped) or a "
            "week-one operational rollout plan (if program/service-shaped). Be specific "
            "and actionable, not aspirational.\n\n"
            "Format as Markdown with headers, including code blocks if applicable."
        ),
    ),
]
