from sqlalchemy import create_engine, text

def connect_to_db(connection_string):
    """Create a connection to the SQL database using SQLAlchemy."""
    engine = create_engine(connection_string)
    return engine

def execute_query(query, connection_string):
    """Execute the SQL query and return both column names and data."""
    engine = connect_to_db(connection_string)

    with engine.connect() as conn:
        result = conn.execute(text(query))

        # Get column names
        columns = result.keys()

        # Fetch all rows
        data = result.fetchall()

    return columns, data
