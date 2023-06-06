from airflow.models import Connection
from airflow import settings
from airflow.hooks.base_hook import BaseHook

def create_connection_task():
    conn_id = 'pg_work_sample'
    conn_type = 'postgres'
    host = 'postgres'
    port = 5432
    login = 'airflow'
    password = 'airflow'
    schema = ''

    # Check if the connection already exists
    try:
        existing_conn = BaseHook.get_connection(conn_id=conn_id)
        if existing_conn is not None:
            print(f"Connection '{conn_id}' already exists.")
            return
    except:
        pass
    # Create the Connection object
    conn = Connection(
        conn_id=conn_id,
        conn_type=conn_type,
        host=host,
        port=port,
        login=login,
        password=password,
        schema=schema
    )

    # Add the Connection to the Airflow metadata database
    session = settings.Session()
    session.add(conn)
    session.commit()
    session.close()
