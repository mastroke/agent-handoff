from pathlib import Path

import pytest

from agent_handoff.models import HandoffVerdict, Layer
from agent_handoff.report import load_results, render_report
from agent_handoff.runner import load_scenarios, run_scenarios


EXAMPLES = Path(__file__).resolve().parents[1] / "examples" / "agency-handoff" / "scenarios.yaml"


def test_load_scenarios():
    project, scenarios = load_scenarios(EXAMPLES)
    assert project == "agency-demo-agent"
    assert len(scenarios) == 3


def test_run_scenarios_mixed_verdict():
    results = run_scenarios(EXAMPLES)
    assert results.project == "agency-demo-agent"
    assert len(results.scenarios) == 3
    assert results.scenarios[0].passed is True
    assert results.scenarios[1].passed is False
    assert results.scenarios[2].passed is False
    assert results.verdict == HandoffVerdict.FAIL


def test_layer_results_cover_all_layers():
    results = run_scenarios(EXAMPLES)
    for scenario in results.scenarios:
        assert {layer.layer for layer in scenario.layers} == set(Layer)


def test_render_report_includes_verdict(tmp_path):
    results = run_scenarios(EXAMPLES)
    report = render_report(results)
    assert "agency-demo-agent" in report
    assert "FAIL" in report
    assert "tool-schema-drift" in report
    assert "memory-bleed" in report


def test_results_round_trip(tmp_path):
    results = run_scenarios(EXAMPLES)
    path = tmp_path / "results.json"
    path.write_text(__import__("json").dumps(results.as_dict(), indent=2))
    loaded = load_results(path)
    assert loaded.project == results.project
    assert len(loaded.scenarios) == len(results.scenarios)


def test_cli_run_and_report(tmp_path, capsys):
    from agent_handoff.cli import main

    out_json = tmp_path / "out.json"
    code = main(["run", str(EXAMPLES), "-o", str(out_json)])
    assert code == 1
    assert out_json.exists()

    out_md = tmp_path / "report.md"
    code = main(["report", str(out_json), "-o", str(out_md)])
    assert code == 0
    text = out_md.read_text()
    assert "Agent Handoff Acceptance Report" in text

    captured = capsys.readouterr()
    assert "verdict FAIL" in captured.out


def test_pack_template_renders():
    results = run_scenarios(EXAMPLES)
    pack_template = (
        Path(__file__).resolve().parents[1] / "pack" / "procurement" / "report-template.md"
    )
    report = render_report(results, pack_template.read_text())
    assert "{{project}}" not in report
    assert "Executive summary" in report
