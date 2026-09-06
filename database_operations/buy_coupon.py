import pymysql
from db_connection import get_connection

CRED = '\033[31m'
C_green = '\033[32m'
CEND = '\033[0m'

def buy_coupon(email, code, amount_paid):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # Fetch User and Valid Coupon
            fetch_user_from_email_query = "SELECT user_id FROM users WHERE email = %s"
            cursor.execute(fetch_user_from_email_query, (email,))
            user = cursor.fetchone()
        
            # Valid Coupons
            get_the_valid_coupon_query = """SELECT coupon_id, price FROM coupons
                    WHERE code = %s AND expiry_date >= NOW() AND is_active = TRUE"""
            cursor.execute(get_the_valid_coupon_query, (code))
            
            coupon = cursor.fetchone()
            
            if not user:
                print(f"{CRED}Transaction Failed: User not found{CEND}")
                return
            if not coupon:
                print(f"{CRED}Coupon you've entered is Invalid/Expired{CEND}")
                return
            
            # Verify Payment
            status = "SUCCESS" if float(amount_paid) >= float(coupon['price']) else "FAILED"
            
            # Record the Transaction 
            add_transaction_query = """INSERT INTO transactions (user_id, coupon_id, amount_paid, status)
                                    VALUES (%s, %s, %s, %s)"""
            cursor.execute(add_transaction_query, (user['user_id'], coupon['coupon_id'], amount_paid, status))
            conn.commit()
            
            if status == 'SUCCESS':
                print(f"{C_green}Payment Successful. You now own {code}{CEND}")
            else:
                print(f"{CRED}Payment Failed:  Insufficient Funds. Coupon costs {coupon['price']}{CEND}")

