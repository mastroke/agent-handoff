# SOW snippet — agent acceptance baseline

Paste into the **Acceptance & handoff** section of your statement of work.

---

## Agent acceptance baseline

Prior to final delivery, Vendor will run a cross-layer acceptance baseline covering prompt behavior, tool-call contracts, memory scoping, and retrieval grounding against agreed golden scenarios. Vendor will deliver an acceptance report showing pass/fail by layer.

**Deliverable:** Markdown acceptance report generated from frozen golden scenarios, including scenario name, layer-level results, and overall handoff verdict.

**Pass criteria:** All golden scenarios pass across prompt, tool, memory, and retrieval layers. Any failing layer blocks handoff until remediated and re-run.

**Out of scope:** Post-production monitoring, live traffic replay, and ongoing regression scheduling unless separately scoped.

**Tooling:** Vendor uses `agent-handoff` (open source) or equivalent documented process. Client receives a copy of scenario definitions and the signed report.

---

Adjust `[Vendor]` / `[Client]` naming to match your contract template.
