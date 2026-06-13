import streamlit as st
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)
from backend.query_generator import generate_sql
from backend.query_executor import execute_query
from backend.insight_generator import generate_insight

st.set_page_config(
    page_title="AI BI Assistant",
    layout="wide"
)

st.title(
    "AI-Powered Business Intelligence Assistant"
)

question = st.text_input(
    "Ask a business question"
)

if st.button("Analyze"):

    try:

        sql = generate_sql(question)

        st.subheader(
            "Generated SQL"
        )

        st.code(
            sql,
            language="sql"
        )

        columns, rows = execute_query(sql)

        st.subheader(
            "Results"
        )

        st.dataframe(
            rows,
            use_container_width=True
        )

        insights = generate_insight(
            question,
            rows
        )

        st.subheader(
            "AI Insights"
        )

        st.write(insights)

    except Exception as e:

        st.error(str(e))