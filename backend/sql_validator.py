import re

BLOCKED_KEYWORDS = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE"
]


def validate_sql(sql):

    if not sql:
        raise Exception("Empty SQL generated")

    # Remove markdown formatting if Gemini returns it
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    print("FINAL SQL =", repr(sql))

    sql_upper = sql.upper()

    # Only SELECT allowed
    if not sql_upper.startswith("SELECT"):
        raise Exception("Only SELECT statements allowed")

    # Block dangerous keywords
    for keyword in BLOCKED_KEYWORDS:
        if re.search(rf"\b{keyword}\b", sql_upper):
            raise Exception(
                f"Blocked keyword detected: {keyword}"
            )

    # Check for multiple statements
    semicolon_count = sql.count(";")

    if semicolon_count > 1:
        raise Exception(
            "Multiple statements not allowed"
        )

    if semicolon_count == 1 and not sql.endswith(";"):
        raise Exception(
            "Multiple statements not allowed"
        )

    return True