from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import anthropic

from .stages import STAGES, Stage

MODEL = "claude-opus-4-8"
MAX_TOKENS = 8000


def _run_stage(
    client: anthropic.Anthropic,
    stage: Stage,
    prompt: str,
    *,
    effort: str,
    on_text: Callable[[str], None] | None = None,
) -> str:
    chunks: list[str] = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        thinking={"type": "adaptive"},
        output_config={"effort": effort},
        system=stage.system_prompt,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            chunks.append(text)
            if on_text:
                on_text(text)
        stream.get_final_message()
    return "".join(chunks)


def run_pipeline(
    topic: str,
    *,
    output_dir: Path,
    effort: str = "high",
    client: anthropic.Anthropic | None = None,
    on_stage_start: Callable[[Stage], None] | None = None,
    on_text: Callable[[str], None] | None = None,
) -> list[tuple[Stage, str]]:
    client = client or anthropic.Anthropic()
    output_dir.mkdir(parents=True, exist_ok=True)

    results: list[tuple[Stage, str]] = []
    previous = topic
    for index, stage in enumerate(STAGES):
        if on_stage_start:
            on_stage_start(stage)

        prompt = stage.instructions.format(topic=topic, previous=previous)
        output = _run_stage(client, stage, prompt, effort=effort, on_text=on_text)

        path = output_dir / f"{index + 1:02d}_{stage.slug}.md"
        path.write_text(f"# {stage.title}\n\n{output}\n", encoding="utf-8")

        results.append((stage, output))
        previous = output

    return results
