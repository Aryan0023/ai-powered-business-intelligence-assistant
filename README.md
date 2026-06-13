# AI-Powered Business Intelligence Assistant

An AI-powered Business Intelligence Assistant that allows users to ask business questions in natural language and receive insights generated from a PostgreSQL database using Google's Gemini model.

## Features

* Natural Language to SQL conversion
* PostgreSQL database integration
* AI-generated business insights
* Streamlit web interface
* SQL validation for security

---

## Project Structure

```
project/
│
├── backend/
│   ├── config.py
│   ├── db.py
│   ├── gemini_client.py
│   ├── insight_generator.py
│   ├── load_data.py
│   ├── query_executor.py
│   ├── query_generator.py
│   └── sql_validator.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── Superstore_Dataset.csv
│
├── sql/
│   ├── create_table.sql
│   └── business_queries.sql
│
├── requirements.txt
└── README.md
```

---

## Prerequisites

Install the following:

1. Python 3.11 or later
2. PostgreSQL
3. Git

---

## Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create PostgreSQL Database

Open PostgreSQL and create a database:

```sql
CREATE DATABASE business_intelligence_assistant;
```

---

## Configure Environment

Create a file named:

```
backend/config.py
```

Update the following values:

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/business_intelligence_assistant"

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

---

## Create Database Table

Run:

```sql
CREATE TABLE superstore (
    row_id INTEGER,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(255),
    segment VARCHAR(50),
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    product_name TEXT,
    sales NUMERIC(12,2),
    quantity INTEGER,
    discount NUMERIC(5,2),
    profit NUMERIC(12,2)
);
```

---

## Load Dataset

Place the dataset in:

```
data/Superstore_Dataset.csv
```

Run:

```bash
python -m backend.load_data
```

Verify data:

```sql
SELECT COUNT(*) FROM superstore;
```

Expected result:

```
9994
```

---

## Run Application

```bash
streamlit run frontend/app.py
```

or

```bash
python -m streamlit run frontend/app.py
```

---

## Example Questions

* What are the total sales?
* What is the total profit?
* Show sales by region.
* Which category generates the highest profit?
* Top 10 products by sales.
* Which state has the highest sales?
* What is the average discount?
* Show monthly sales trend.

---

## Troubleshooting

### ModuleNotFoundError

Run modules from project root:

```bash
python -m backend.load_data
```

instead of:

```bash
python backend/load_data.py
```

### Gemini Model Not Found

Update the model name in:

```python
backend/gemini_client.py
```

to a currently supported Gemini model.

### Table Does Not Exist

Verify:

```sql
SELECT * FROM superstore LIMIT 5;
```

### No Data Returned

Verify:

```sql
SELECT COUNT(*) FROM superstore;
```

The table should contain approximately 9994 rows.

---

## Tech Stack

* Python
* Streamlit
* PostgreSQL
* SQLAlchemy
* Pandas
* Google Gemini API

---

## Author

Aryan Ingle
