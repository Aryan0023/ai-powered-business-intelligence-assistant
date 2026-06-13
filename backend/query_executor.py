from sqlalchemy import text
from backend.db import engine
from backend.sql_validator import validate_sql

def execute_query(sql):

    validate_sql(sql)

    with engine.connect() as conn:

        result = conn.execute(
            text(sql)
        )

        rows = result.fetchall()

        columns = result.keys()

        return columns, rows