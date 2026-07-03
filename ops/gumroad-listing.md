# Gumroad listing — Agency Handoff Pack ($49)

Paste-ready copy for https://mastroke.gumroad.com/l/agency-handoff-pack
Create the product at: https://mastroke.gumroad.com/products/new

## Product name
Agency Handoff Pack — Acceptance report templates for AI agencies

## Price
$49 (one-time)

## Short description (Gumroad card / Twitter)
Frozen-scenario acceptance report templates AI agencies attach at client
sign-off, so buyers stop asking "how do we know it won't break after deploy?"

## Full description (paste into the listing body)

You close a $10–30k agent build. The client asks the question that kills the
deal: **"how do we know it won't silently break after deploy?"**

Observability tools show traces. They don't produce a sign-off artifact buyers
will accept. This pack is that artifact.

**What's inside**

- **Acceptance report template** — a branded, buyer-ready pass/fail report
  covering the four layers that drift in production: prompt, tool, memory, and
  retrieval.
- **SOW snippet** — procurement language you paste straight into your statement
  of work, so "agent acceptance" is a contractual line item, not a vibe.
- **Client-onboarding runbook** — the baseline-before-handoff runbook so the
  frozen scenarios are locked before delivery, not after.

**How it pairs with the free OSS CLI**

The pack templates are designed to drop onto the output of the free
[agent-handoff](https://github.com/mastroke/agent-handoff) CLI:

```
pip install agent-handoff
agent-handoff run examples/agency-handoff/scenarios.yaml
agent-handoff report examples/agency-handoff/scenarios.results.json --pack -o handoff-report.md
```

Copy `sow-snippet.md` into your SOW; attach `handoff-report.md` at sign-off.

**Why now**

EU AI Act Art. 25 + the Product Liability Directive (transposition Dec 2026)
make buyers and vendors jointly liable for high-risk agentic failures. Buyers
increasingly *require* a signed acceptance pack. You're not creating demand —
you're handing them the compliance artifact they're already being asked for.

**License**

Templates are yours to use on every client engagement. The OSS CLI stays MIT.

## Tags
ai agents, agency, acceptance testing, ai governance, eu ai act, procurement, llm ops, qa

## Cover image
Use `docs/screenshots/acceptance-report.png` (TODO: render a sample
handoff-report.md to PNG) or the mermaid architecture diagram from the README.

## After listing
- Set the product **public**.
- Put the buy link in: `agent-handoff/README.md`, `agent-handoff/pack/procurement/README.md`,
  and `agent-acceptance/README.md`.
- Build the zip with: `bash agent-handoff/scripts/package_procurement_pack.sh`
  → upload `agent-handoff/dist/agency-handoff-pack.zip` as the product file.
- Add the Gumroad URL to `agent-acceptance/docs/GTM.md` week-1 checklist.
