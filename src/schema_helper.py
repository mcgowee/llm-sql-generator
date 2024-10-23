from sqlalchemy import inspect


def get_schema(engine):
    inspector = inspect(engine)
    schema_info = {}

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema_info[table_name] = [col['name'] for col in columns]

    return schema_info
