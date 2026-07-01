# Agent Handoff Acceptance Report

**Client:** {{client_name}}
**Project:** {{project}}
**Delivery date:** {{delivery_date}}
**Overall verdict:** {{verdict}}

---

## Executive summary

{{summary}}

This report documents cross-layer baseline checks across **prompt**, **tool**, **memory**, and **retrieval** behavior. It is intended for client sign-off at project handoff, not post-production monitoring.

## Scenario results

{{scenario_table}}

## Acceptance criteria

Handoff proceeds when:

1. All golden scenarios pass across all four layers.
2. Failed layers are remediated and re-run before client delivery.
3. Client approver acknowledges scope limits (mock replay baseline; live-agent hook is a future integration).

## Procurement attestation

The delivery team attests that baseline scenarios were executed against the agreed golden fixtures and results are attached to this report.

| Role | Name | Date | Signature |
| --- | --- | --- | --- |
| Agency delivery lead | | | |
| Client technical approver | | | |
| Client business approver | | | |

---
Generated with [agent-handoff](https://github.com/mastroke/agent-handoff) + Agency Handoff Pack.
