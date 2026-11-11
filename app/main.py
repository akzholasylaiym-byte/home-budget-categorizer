import streamlit as st

st.title("Smart Home Budget & Expense Categorizer")
uploaded = st.file_uploader("Upload bank statement (CSV/PDF)", type=["csv", "pdf"])
if uploaded:
    st.write("TODO: parse -> categorize -> anomalies -> budget")
