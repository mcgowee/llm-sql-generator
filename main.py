import os
import json

from sqlalchemy import false

from llm_sql import generate_sql_query, query_llm
from db_connector import execute_query, connect_to_db
from schema_helper import get_schema

def format_query_results(columns, data):
    """Converts query results (columns and data) into a structured JSON format."""
    formatted_results = [
        dict(zip(columns, row)) for row in data
    ]
    return formatted_results


def create_prompt(question, formatted_results):
    """Creates a prompt for the LLM using the user's question and query results."""
    # Convert the results to JSON for easier readability
    json_results = json.dumps(formatted_results, indent=4)

    # Create a dynamic prompt based on the user's question and query results
    prompt = f"""
    The user has asked the following question: "{question}"

    Here are the query results:
    {json_results}

    Based on these results, please provide a response.
    """
    return prompt

def main():
    # Absolute path to the SQLite database
    db_path = os.path.abspath(r"C:\Users\mcgow\PycharmProjects\llm_sql_generator_project\data\northwind.db")

    # SQLAlchemy connection string for SQLite
    connection_string = f"sqlite:///{db_path}"

    # Connect to the database and retrieve the schema
    engine = connect_to_db(connection_string)
    schema = get_schema(engine)

    while True:

        user_input = input("Enter your question: ")
        # Provide a default if the input is empty
        # if not user_input:
        #    user_input = "Which employee made the most sales?"

        sql_query = generate_sql_query(user_input, schema)
        # print(f"Generated SQL Query: {sql_query}")



        try:
            # result = execute_query(sql_query, connection_string)
            columns, data = execute_query(sql_query, connection_string)
            # print(columns)
            # print(data)
            formatted_results = format_query_results(columns, data)
            # print(formatted_results)

            # Create a dynamic prompt based on user input and results
            prompt = create_prompt(user_input, formatted_results)
            # print(prompt)

            # Send the prompt to the LLM and get a response (implement the function if needed)
            llm_response = query_llm(prompt)  # Replace with your LLM query function
            print(f"LLM Response: {llm_response}")

        except Exception as e:
            print(f"Error executing query: {e}")



if __name__ == "__main__":
    main()