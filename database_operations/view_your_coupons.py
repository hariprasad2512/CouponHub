from datetime import datetime

from db_connection import get_connection


CRED = '\033[31m'
CEND = '\033[0m'


def format_expiry_date(input_str):
    dt_obj = datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")
    return dt_obj.strftime("%d %B %Y %H:%M:%S")


def view_your_coupons(email):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            fetch_user_query = "SELECT user_id FROM users WHERE email = %s"
            cursor.execute(fetch_user_query, (email,))
            user = cursor.fetchone()

            if not user:
                print(f"{CRED}User not found{CEND}")
                return

            query = """SELECT c.coupon_name, c.code, c.discount_pct, c.price, c.expiry_date
                       FROM coupons c
                       WHERE c.purchased_by_user_id = %s
                       AND NOT EXISTS (
                           SELECT 1 FROM redemptions r
                           WHERE r.user_id = %s AND r.coupon_id = c.coupon_id
                       )
                       ORDER BY c.expiry_date"""
            cursor.execute(query, (user['user_id'], user['user_id']))
            coupons = cursor.fetchall()

            print()
            print("Coupon Name\tCoupon Code\tDiscount\tPrice\tExpiry Date")
            if not coupons:
                print(f"{CRED}You have no unredeemed coupons{CEND}")
                return

            for coupon in coupons:
                expiry_date_formatted = format_expiry_date(str(coupon['expiry_date']))
                print(
                    f"{coupon['coupon_name']:<20}{coupon['code']:<15}"
                    f"{coupon['discount_pct']}%\t\t"
                    f"{coupon['price']:<8} {expiry_date_formatted}"
                )