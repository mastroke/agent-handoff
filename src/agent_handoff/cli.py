from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from agent_handoff.report import load_results, load_template, render_report
from agent_handoff.runner import run_scenarios


def _cmd_run(args: argparse.Namespace) -> int:
    scenarios_path = Path(args.scenarios)
    output_path = Path(args.output) if args.output else scenarios_path.with_suffix(".results.json")
    results = run_scenarios(scenarios_path)
    output_path.write_text(json.dumps(results.as_dict(), indent=2) + "\n")
    print(f"Wrote {output_path} — verdict {results.verdict.value}")
    return 0 if results.verdict.value == "PASS" else 1


def _cmd_report(args: argparse.Namespace) -> int:
    results_path = Path(args.results)
    output_path = Path(args.output) if args.output else results_path.with_suffix(".md")
    template_path = Path(args.template) if args.template else None
    if template_path is None and args.pack:
        template_path = Path(__file__).resolve().parents[2] / "pack" / "procurement" / "report-template.md"
    results = load_results(results_path)
    report = render_report(results, load_template(template_path))
    output_path.write_text(report)
    print(f"Wrote {output_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agent-handoff",
        description="Run golden-scenario baselines and emit client handoff acceptance reports.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    run_parser = sub.add_parser("run", help="Replay golden scenarios and write JSON results")
    run_parser.add_argument("scenarios", help="Path to scenarios YAML file")
    run_parser.add_argument("-o", "--output", help="Output JSON path")
    run_parser.set_defaults(func=_cmd_run)

    report_parser = sub.add_parser("report", help="Render acceptance report from JSON results")
    report_parser.add_argument("results", help="Path to results JSON from agent-handoff run")
    report_parser.add_argument("-o", "--output", help="Output markdown path")
    report_parser.add_argument(
        "--template",
        help="Custom report template with {{project}}, {{verdict}}, {{summary}}, {{scenario_table}}",
    )
    report_parser.add_argument(
        "--pack",
        action="store_true",
        help="Use the paid procurement pack report template bundled in pack/procurement/",
    )
    report_parser.set_defaults(func=_cmd_report)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
