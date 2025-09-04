import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables from the .env file
load_dotenv()

# Access the connection string from the environment variable
db_connection_string = os.environ.get("DB_CONNECTION_STRING")

engine = create_engine(db_connection_string)

def load_jobs_from_db():
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