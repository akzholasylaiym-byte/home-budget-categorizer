# Smart Home Budget & Expense Categorizer

Personal finance assistant: upload a bank statement (CSV/PDF) and get automatic expense categories, anomaly detection and a next-month budget with short explanations.

> CSS4007 Final Project. Team: [Name 1], [Name 2], [Name 3]. Built with **Claude Code** (agentic coding tool).

## Features
- CSV/PDF ingestion into one schema, with personal data masked before any LLM call
- Hybrid categorization: rules first, LLM (batched, cached) for unknown merchants
- Statistical anomaly detection (median/MAD, new merchant, duplicate charge); the LLM only explains
- Next-month budget: recurring vs variable spending, 3-month median, LLM justification
- Streamlit UI

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # add your LLM key
streamlit run app/main.py
pytest
```

## Structure
| Path | Purpose |
|---|---|
| `src/ingestion` | CSV/PDF parsers, schema, masking |
| `src/categorizer` | rules + LLM hybrid |
| `src/anomaly` | anomaly detection |
| `src/budget` | budget recommendation |
| `src/llm` | LLM client, prompts, cache |
| `app` | Streamlit UI |
| `tests` | pytest tests |
| `docs` | proposal, notes |

## Docs
- [Proposal (EN)](docs/PROPOSAL.md) / [Proposal (KK)](docs/PROPOSAL.kk.md)
- [Evaluation](EVALUATION.md)
- [Agent instructions](CLAUDE.md)

## Team and responsibilities
| Member | Part |
|---|---|
| [Name 1] | Ingestion, parsers, DB, masking |
| [Name 2] | Categorization, LLM integration, its evaluation |
| [Name 3] | Anomaly, budget, UI, their evaluation |

## Use of the agentic tool
How Claude Code was used (workflow, prompts, what we reviewed or changed): [fill in].
