from db_connection import get_connection
import pymysql

CRED = '\033[31m'
C_green = '\033[32m'
CEND = '\033[0m'

def add_user(name, email):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            try:
                cursor.execute(query, (name, email))
                conn.commit()
                print(f"{C_green} User '{name}' added successfully.{CEND}")
            except pymysql.IntegrityError:
                print(f"{CRED}Error: Email already exists.{CEND}")
