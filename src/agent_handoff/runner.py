from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from agent_handoff.models import HandoffVerdict, Layer, LayerResult, RunResults, ScenarioResult


def load_scenarios(path: Path) -> tuple[str, list[dict[str, Any]]]:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise ValueError("scenarios file must be a mapping")
    project = str(data.get("project", path.stem))
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError("scenarios file must include a non-empty scenarios list")
    return project, scenarios


def _check_layer(layer: Layer, spec: dict[str, Any]) -> LayerResult:
    expected = spec.get("expected")
    actual = spec.get("actual")
    if expected == actual:
        return LayerResult(layer=layer, passed=True, reason="matches golden fixture")
    return LayerResult(
        layer=layer,
        passed=False,
        reason=f"expected {expected!r}, got {actual!r}",
    )


def _run_scenario(raw: dict[str, Any]) -> ScenarioResult:
    name = str(raw.get("name", "unnamed"))
    description = str(raw.get("description", ""))
    layers_spec = raw.get("layers")
    if not isinstance(layers_spec, dict):
        raise ValueError(f"scenario {name!r} must define a layers mapping")

    results: list[LayerResult] = []
    for layer in Layer:
        if layer.value not in layers_spec:
            results.append(
                LayerResult(layer=layer, passed=False, reason="layer not defined in scenario")
            )
            continue
        layer_data = layers_spec[layer.value]
        if not isinstance(layer_data, dict):
            raise ValueError(f"scenario {name!r} layer {layer.value} must be a mapping")
        results.append(_check_layer(layer, layer_data))

    return ScenarioResult(name=name, description=description, layers=results)


def run_scenarios(path: Path) -> RunResults:
    project, raw_scenarios = load_scenarios(path)
    scenarios = [_run_scenario(raw) for raw in raw_scenarios]
    return RunResults(project=project, scenarios=scenarios)


def summarize_verdict(results: RunResults) -> HandoffVerdict:
    return results.verdict
