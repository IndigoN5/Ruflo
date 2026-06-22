from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

from .pipeline import run_pipeline
from .stages import Stage


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "run"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ruflo",
        description=(
            "Run a 4-stage AI agent pipeline (research, ideation, spec, prototype) "
            "for a community-based service idea or problem."
        ),
    )
    parser.add_argument("topic", help="The community need, problem, or idea to develop.")
    parser.add_argument(
        "--effort",
        choices=["low", "medium", "high", "max"],
        default="high",
        help="Thinking effort per stage (default: high).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory to write stage outputs to (default: runs/<timestamp>-<slug>/).",
    )
    args = parser.parse_args(argv)

    output_dir = args.output_dir or Path("runs") / dt.datetime.now().strftime(
        f"%Y%m%d-%H%M%S-{_slugify(args.topic)}"
    )

    def on_stage_start(stage: Stage) -> None:
        print(f"\n\n=== Stage: {stage.title} ===\n", file=sys.stderr)

    def on_text(text: str) -> None:
        print(text, end="", flush=True)

    run_pipeline(
        args.topic,
        output_dir=output_dir,
        effort=args.effort,
        on_stage_start=on_stage_start,
        on_text=on_text,
    )

    print(f"\n\nSaved stage outputs to {output_dir}/", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
