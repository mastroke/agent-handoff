from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Layer(str, Enum):
    PROMPT = "prompt"
    TOOL = "tool"
    MEMORY = "memory"
    RETRIEVAL = "retrieval"


class HandoffVerdict(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"


@dataclass(frozen=True)
class LayerCheck:
    layer: Layer
    expected: Any
    actual: Any


@dataclass
class LayerResult:
    layer: Layer
    passed: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {"layer": self.layer.value, "passed": self.passed, "reason": self.reason}


@dataclass
class ScenarioResult:
    name: str
    description: str
    layers: list[LayerResult] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(layer.passed for layer in self.layers)

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "passed": self.passed,
            "layers": [layer.as_dict() for layer in self.layers],
        }


@dataclass
class RunResults:
    project: str
    scenarios: list[ScenarioResult] = field(default_factory=list)

    @property
    def verdict(self) -> HandoffVerdict:
        if self.scenarios and all(scenario.passed for scenario in self.scenarios):
            return HandoffVerdict.PASS
        return HandoffVerdict.FAIL

    def as_dict(self) -> dict[str, Any]:
        return {
            "project": self.project,
            "verdict": self.verdict.value,
            "scenarios": [scenario.as_dict() for scenario in self.scenarios],
        }
