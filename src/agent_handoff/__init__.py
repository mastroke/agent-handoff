"""Golden-scenario baseline and handoff acceptance reports for AI agencies."""

from agent_handoff.models import HandoffVerdict, Layer, LayerResult, RunResults, ScenarioResult
from agent_handoff.report import render_report
from agent_handoff.runner import load_scenarios, run_scenarios

__all__ = [
    "HandoffVerdict",
    "Layer",
    "LayerResult",
    "RunResults",
    "ScenarioResult",
    "load_scenarios",
    "render_report",
    "run_scenarios",
]

__version__ = "0.1.0"
