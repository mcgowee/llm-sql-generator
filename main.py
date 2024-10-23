import os
import json
from sqlalchemy import false
from src.llm_sql import generate_sql_query, query_llm
from src.db_connector import execute_query, connect_to_db
from src.schema_helper import get_schema

def format_query_results(columns, data):
    """Converts query results (columns and data) into a structured JSON format."""
    formatted_results = [dict(zip(columns, row)) for row in data]
    return formatted_results

def create_prompt(question, formatted_results):
    """Creates a prompt for the LLM using the user's question and query results."""
    json_results = json.dumps(formatted_results, indent=4)

    prompt = f"""
    The user has asked the following question: "{question}"

    Here are the query results:
    {json_results}

    Based on these results, please provide a response.
    """
    return prompt

def main():
    # Ensure the working directory is correctly set to the root of the project
    os.chdir(os.path.dirname(__file__))

    # Build the absolute path to the SQLite database in the 'data/' folder
    db_path = os.path.abspath(os.path.join('data', 'northwind.db'))

    # Verify the current working directory and database path for debugging
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"Database Path: {db_path}")

    # SQLAlchemy connection string for SQLite
    connection_string = f"sqlite:///{db_path}"

    # Connect to the database and retrieve the schema
    print("Connecting to the database...")
    engine = connect_to_db(connection_string)
    schema = get_schema(engine)
    print("Connection successful. Database schema loaded.")

    print("\nWelcome to the LLM SQL Generator!")
    print("You can ask questions to retrieve information from the Northwind database.")
    print("Type 'quit' to exit the program.\n")

    print("### Sample Questions ###")
    print("1. Which employee made the most sales?")
    print("2. What is the total revenue by country?")
    print("3. List the top 5 products with the highest sales.")
    print("4. How many orders were placed by customers from Germany?")
    print("5. Who are the top customers based on total purchases?\n")

    print("Reference: https://github.com/jpwhite3/northwind-SQLite3?tab=readme-ov-file\n")

    while True:
        # Prompt user for input
        print("\n\n### Sample Questions ###")
        print("1. Which employee made the most sales?")
        print("2. What is the total revenue by country?")
        print("3. List the top 5 products with the highest sales.")
        print("4. How many orders were placed by customers from Germany?")
        print("5. Who are the top customers based on total purchases?\n")
        print("Type 'quit' to exit the program.")
        user_input = input("Enter your question: ")

        # Handle quit option
        if user_input.strip().lower() == "quit":
            print("Exiting the program. Goodbye!")
            break

        if not user_input:
            print("Please enter a valid question.")
            continue

        print("\nGenerating SQL query from your input...")
        sql_query = generate_sql_query(user_input, schema)
        print(f"Generated SQL Query: {sql_query}")

        try:
            print("Executing the SQL query...")
            columns, data = execute_query(sql_query, connection_string)
            formatted_results = format_query_results(columns, data)

            print("\nQuery executed successfully. Here are the results:")
            print(json.dumps(formatted_results, indent=4))

            # Create a dynamic prompt based on user input and results
            prompt = create_prompt(user_input, formatted_results)

            print("\nSending prompt to the LLM for a response...")
            llm_response = query_llm(prompt)
            print(f"LLM Response: {llm_response}")

        except Exception as e:
            print(f"Error executing query: {e}")

if __name__ == "__main__":
    main()
