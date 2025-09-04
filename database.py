import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables from the .env file
load_dotenv()

# Access the connection string from the environment variable
def get_db_connection():
    db_connection_string = os.environ.get("DB_CONNECTION_STRING")
    if not db_connection_string:
        raise ValueError("DB_CONNECTION_STRING is not set in environment variables.")
    return create_engine(db_connection_string)

def load_jobs_from_db():
    engine = get_db_connection()
    with engine.connect() as conn:
        results = conn.execute(text("""
        SELECT
        *
        FROM
        jobs;
        """))

    
        jobs = []
        for row in results.all():
            jobs.append(row._mapping)

    return jobs