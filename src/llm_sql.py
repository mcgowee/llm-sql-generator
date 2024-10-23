import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Please ensure it's set in the .env file.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def generate_sql_query(prompt, schema_info):
    """Generate an SQL query from a natural language prompt and schema."""

    # Construct the prompt with the schema information
    schema_text = f"The database schema is:\n{schema_info}\n"
    # Ensure table and column names with spaces are enclosed in quotes
    full_prompt = schema_text + """
    Please generate an SQL query for the following request, ensuring that any table or column names that contain spaces are enclosed in double quotes (e.g., "table name" or "column name").
    """ + prompt

    # Use the ChatCompletion endpoint to get the query
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an assistant that generates SQL queries based on user input."},
            {"role": "user", "content": full_prompt}
        ],
        model="gpt-4",
        max_tokens=500,
        temperature=0  # Set temperature to 0 for more deterministic output (optional)
    )

    # Extract the SQL query from the response content
    content = response.choices[0].message.content.strip()
    sql_start = content.find("```sql")
    sql_end = content.find("```", sql_start + 1)

    if sql_start != -1 and sql_end != -1:
        return content[sql_start + len("```sql"):sql_end].strip()
    else:
        # Return the full content if no SQL query is found
        return content

def query_llm(prompt):
    """Use the LLM to generate a response based on the provided prompt."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides information based on data."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500  # Adjust max tokens as needed
    )

    return response.choices[0].message.content.strip()
