# Smart Home Budget & Expense Categorizer: Proposal

CSS4007 Final Project. Group: [Name 1], [Name 2], [Name 3].

## 1. Problem and idea
Most people do not know where their money goes. Bank statements arrive as CSV or PDF files full of cryptic merchant strings, and manual categorization is tedious. We build a personal finance assistant: the user uploads a statement, and the system categorizes every transaction, flags unusual spending and proposes a next-month budget with a short explanation.

## 2. Core features
1. **Ingestion.** Parse CSV and PDF statements (Kaspi, Halyk, generic CSV) into one schema: date, amount, description, balance. Personal data is masked before any LLM call.
2. **Hybrid categorization.** Rules (merchant-to-category dictionary) first; unknown merchants go in batches to an LLM that returns JSON; results cached by merchant.
3. **Anomaly detection.** Per-category median/MAD or IQR, new-merchant and duplicate-charge checks. The LLM only explains flagged items.
4. **Budget recommendation.** Recurring payments separated from variable spending; limits from the 3-month median with an LLM justification.
5. **Web UI.** Streamlit: upload, charts, anomaly list, budget table.

## 3. AI component
- LLM with structured output for categorization and explanations.
- Tool-use style pipeline: the LLM calls deterministic functions instead of doing arithmetic.
- Model: free-tier API (Gemini or Groq) or local Ollama, configurable.

## 4. Evaluation plan
| Component | Method | Metric |
|---|---|---|
| Categorization | 200-300 hand-labeled transactions; rules vs LLM vs hybrid | Accuracy, macro-F1, LLM calls saved |
| Anomaly detection | Inject synthetic anomalies | Precision, recall |
| Budget | Backtest month N+1 from earlier months | MAPE vs naive baseline |

## 5. Tech stack and agentic tool
Python, pandas, SQLite, pdfplumber, Streamlit, pytest. Built with **Claude Code** (paid, Claude Pro). CLAUDE.md defines stack, structure and testing rules. Each member reviews the agent-written code of their module.

## 6. Team roles
| Member | Responsibility |
|---|---|
| [Name 1] | Ingestion, parsers, database, masking |
| [Name 2] | Categorization, LLM integration, its evaluation |
| [Name 3] | Anomaly, budget, UI, their evaluation |

## 7. Timeline
| Date | Milestone |
|---|---|
| By 16 Nov | Checkpoint: end-to-end CSV flow with basic UI |
| 17-30 Nov | PDF parsing, hybrid categorizer, evaluation datasets |
| 1-5 Dec | Evaluation runs, README, EVALUATION.md, polish |
| 6 Dec | Code freeze, tag v1.0 |
| 7-19 Dec | Defense preparation |

## 8. Risks and mitigations
- **Privacy:** mask before LLM calls; demo with synthetic data only.
- **Messy PDFs:** CSV first, PDF for one or two banks.
- **LLM limits/errors:** cache by merchant, fall back to rules.
- **Little labeled data:** generate synthetic statements, label a subset manually.
