import pymysql
from db_connection import get_connection
CRED = '\033[31m'
C_green = '\033[32m'
CEND = '\033[0m'

def create_coupon(code, discount_pct, price, expiry_date):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            query = """INSERT INTO coupons(code, discount_pct, price, expiry_date)
            VALUES (%s, %s, %s, %s)"""
            
            try:
                cursor.execute(query, (code, discount_pct, price, expiry_date))
                conn.commit()
                print(f"{C_green}Coupon Code {code} created.{CEND}")
            except pymysql.IntegrityError:
                print(f'{CRED}Error: Coupon code already exists{CEND}')
