LittleJohn NL2SQL Bot

This project converts natural language questions into SQL queries using an LLM (Google Gemini) with support from NER and RAG techniques. it demonstrates effective prompt engineering, schema grounding, and clean design.

---

Features:-

- Uses Google Gemini API (via `google.generativeai`) for SQL generation
- Integrates Named Entity Recognition (NER) using spaCy
- Uses RAG-style examples to guide SQL generation
- Includes a clean and minimal Streamlit UI

---

Schema Context:-

The system supports a MySQL-like schema with three tables:

- customers
  - `customer_id` (INTEGER, PRIMARY KEY)
  - `registration_date` (DATE)
  - `city` (TEXT)
  - `gender` (TEXT)

- orders
  - `order_id` (INTEGER, PRIMARY KEY)
  - `customer_id` (INTEGER, FOREIGN KEY → customers.customer_id)
  - `order_date` (DATE)
  - `total_amount` (NUMERIC)
  - `status` (TEXT)

- order_items
  - `item_id` (INTEGER, PRIMARY KEY)
  - `order_id` (INTEGER, FOREIGN KEY → orders.order_id)
  - `product_name` (TEXT)
  - `quantity` (INTEGER)
  - `unit_price` (NUMERIC)

Schema details are provided in `schema.py` and passed into the Gemini prompt.

---

How to Use:-

Clone the repository and set up your environment:

```bash
git clone https://github.com/Littlejohn2003/littlejohn_nl2sql
cd littlejohn_nl2sql
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_sm
