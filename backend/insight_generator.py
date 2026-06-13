from backend.gemini_client import ask_gemini

def generate_insight(
    question,
    rows
):

    prompt = f"""
You are a Business Analyst.

Question:

{question}

Results:

{rows}

Provide:

1. Key Findings
2. Business Impact
3. Recommendation

Keep concise.
"""

    return ask_gemini(prompt)