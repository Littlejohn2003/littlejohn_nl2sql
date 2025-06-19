"""
littlejohn_bot.py
Author: Little John Saroniya
Description: Converts natural language queries into SQL using LLMs with schema + RAG + NER.
"""

import google.generativeai as genai
from schema import SCHEMA_DEF
from rag_examples import RETRIEVED_CONTEXT
from ner_module import extract_entities

# Configure Gemini API
genai.configure(api_key="AIzaSyCefRkrp8bYZw8z7iDB0GnfzmHxGQWe1Jo")
model = genai.GenerativeModel("gemini-2.5-flash")

def nl2sql(nl_query: str) -> str:
    """
    Convert a natural language query into a valid SQL query using Gemini, NER, and schema context.
    """
    # Extract named entities from user input
    entities = extract_entities(nl_query)
    entity_info = "\n".join([f"{label}: {value}" for label, value in entities]) or "None"

    # Construct prompt with schema, examples, and NER context
    prompt = f"""
You are a SQL generation assistant.

Given the following:
1. Database schema:
{SCHEMA_DEF}

2. Example queries (RAG):
{RETRIEVED_CONTEXT}

3. Named Entities detected in user input:
{entity_info}

Translate this user question into a syntactically correct SQL query:
"{nl_query}"

Only output the SQL query.
"""

    # Get LLM response
    response = model.generate_content(prompt)
    return response.text.strip()

# Test queries
if __name__ == "__main__":
    queries = [
        "give me sells that placed in last quarter.",
        "give me nsme of whom frecuently bay",
        "total sell of prodcut with name apple",
        "orders from pune last week"
    ]

    for q in queries:
        print(f"\nNL: {q}")
        print("SQL:")
        print(nl2sql(q))
