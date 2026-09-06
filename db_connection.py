import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_connection():
    """Establishes and returns a connection to the MySQL database."""
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Database connection failed: {e}")
        return None
