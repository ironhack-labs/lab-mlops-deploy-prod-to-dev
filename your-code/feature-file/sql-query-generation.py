# Controlling SQL using natural language
# Goal: given table "definitions" + a natural-language question, ask the LLM which tables are needed.

from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# Load OPENAI_API_KEY from a local .env file (so we don't hardcode secrets in code)
_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to call the model with a prompt and return the text response
def return_OAI(user_message):
    # Create OpenAI client using your API key
    client = OpenAI(api_key=OPENAI_API_KEY)

    # We send a single message containing the prompt (tables + question + output format instructions)
    context = [{"role": "system", "content": user_message}]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=context,
        temperature=0,  # 0 = more deterministic/repeatable responses
    )

    return response.choices[0].message.content


# Definition of the tables (metadata for the model: table name + what it contains)
import pandas as pd

data = {
    "table": ["employees", "salary", "studies"],
    "definition": [
        "Employee information, name...",
        "Salary details for each year",
        "Educational studies, name of the institution, type of studies, level",
    ],
}
df = pd.DataFrame(data)
print(df)

# Convert the table definitions into a text block to include inside the prompt
text_tables = "\n".join([f"{row['table']}: {row['definition']}" for index, row in df.iterrows()])

prompt_question_tables = """
Given the following tables and their content definitions,
### Tables
{tables}

Tell me which tables would be necessary to query with SQL to address the user's question below.
Return the table names in a json format.
### User Question:
{question}
"""

# Create the final prompt: plug in the table definitions and the user's question
pqt1 = prompt_question_tables.format(
    tables=text_tables,
    question="Return the name of the best paid employee"
)

print(return_OAI(pqt1))
