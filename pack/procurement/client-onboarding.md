# Client onboarding — run baseline before handoff

Use this runbook one week before client delivery.

## 1. Freeze golden scenarios

Agree with the client on 3–10 scenarios covering:

- Critical user journeys (support, billing, onboarding)
- Tool contracts the agent depends on
- Memory scoping rules (tenant isolation)
- Retrieval sources that must ground answers

Save as `scenarios.yaml`. See `examples/agency-handoff/scenarios.yaml` for structure.

## 2. Run baseline

```bash
pip install agent-handoff
agent-handoff run scenarios.yaml -o results.json
```

Exit code 0 = all layers pass. Non-zero = fix before scheduling handoff call.

## 3. Generate report

```bash
agent-handoff report results.json --pack -o handoff-report.md
```

Fill in client name and delivery date in the report header before sending.

## 4. Attach to handoff meeting

Send the report 24h before sign-off. Walk through failed layers if any remain open.

## 5. Paste SOW language

Use `sow-snippet.md` in future contracts so acceptance baseline is pre-agreed.
