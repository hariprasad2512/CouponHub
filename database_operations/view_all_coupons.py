import pymysql
from db_connection import get_connection
from datetime import datetime
CRED = '\033[31m'
C_green = '\033[32m'
CEND = '\033[0m'

def format_expiry_date(input_str):
    dt_obj = datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")

    return dt_obj.strftime("%d %B %Y %H:%M:%S")

def view_all_coupons():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            query = """SELECT * FROM coupons
                       WHERE is_active = TRUE AND purchased_by_user_id IS NULL
                       AND NOW() < expiry_date"""
            try:
                cursor.execute(query=query)
                coupons = cursor.fetchall()
                print()
                print(f"{"Coupon Name":<30} {"Coupon Code":<15} {"Price":<8} {"Expiry Date"}")
                if not coupons:
                    print(f'{CRED}No Coupons Available Right now!{CEND}')
                for coupon in coupons:
                    expiry_date_formatted = format_expiry_date(str(coupon['expiry_date']))
                    print(
                        f"{coupon['coupon_name']:<30}{coupon['code']:<15}"
                        f"{coupon['price']:<8} {expiry_date_formatted}"
                    )
                    print()
            except Exception as e:
                print(f'{CRED}Error: ${e}{CEND}')