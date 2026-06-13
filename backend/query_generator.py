from backend.gemini_client import ask_gemini

def generate_sql(question):

    prompt = f"""
You are a PostgreSQL expert.

Database schema:

Table name: superstore

Columns:
- row_id
- order_id
- order_date
- ship_date
- ship_mode
- customer_id
- customer_name
- segment
- country
- city
- state
- postal_code
- region
- product_id
- category
- sub_category
- product_name
- sales
- quantity
- discount
- profit

Generate ONLY a PostgreSQL SELECT query.

Question:
{question}
"""
    sql = ask_gemini(prompt)

    print("GEMINI OUTPUT:", sql)

    if not sql or "ERROR" in sql:
        return "SELECT 1;"

    return sql.strip().replace("```sql", "").replace("```", "")