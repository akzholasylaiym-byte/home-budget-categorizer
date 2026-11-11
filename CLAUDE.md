# Project instructions for Claude Code

Project: Smart Home Budget & Expense Categorizer (Python).

## Stack
Python 3.11+, pandas, SQLite, pdfplumber, Streamlit, pytest. LLM via a configurable provider (Gemini/Groq/Ollama) in `src/llm`.

## Rules
- Unified transaction schema: `date, amount, description, balance` (+ `category`, `merchant`).
- Mask personal data (names, account numbers) BEFORE any LLM call.
- Categorization is hybrid: rules first, then batched LLM calls returning JSON only, cached by merchant.
- Anomaly detection is statistical (median/MAD or IQR). The LLM only explains results, never decides.
- Do all arithmetic in code, not in the LLM.
- Write a pytest test for every new function. Run `pytest` before finishing a task.
- Small, focused changes; one module per task. Type hints and short docstrings.
- Never commit `.env`, API keys or real bank statements. Use synthetic data in `data/sample`.
- Each team member owns one area (see README); keep modules independent.
