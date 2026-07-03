# Agency Handoff Pack — Procurement templates ($49)

Templates for AI agencies closing client builds. Pair with the OSS
[agent-handoff](https://github.com/mastroke/agent-handoff) CLI.

**Purchase:** https://mastroke.gumroad.com/l/agency-handoff-pack

## Contents

| File | Use |
| --- | --- |
| `report-template.md` | Branded acceptance report with placeholders |
| `sow-snippet.md` | Procurement language to paste into SOW |
| `client-onboarding.md` | Runbook for baseline before handoff |

## Quickstart

```bash
pip install agent-handoff
agent-handoff run examples/agency-handoff/scenarios.yaml
agent-handoff report examples/agency-handoff/scenarios.results.json --pack -o handoff-report.md
```

Copy `sow-snippet.md` into your statement of work and attach the generated report at sign-off.
