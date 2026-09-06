import pymysql
from db_connection import get_connection


CRED = '\033[31m'
C_green = '\033[32m'
CEND = '\033[0m'
# Executing Redemptions

def redeem_coupon(email, code):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # Fetch user and Coupon IDs
            fetch_user_query = "SELECT user_id FROM users WHERE email = %s"
            cursor.execute(fetch_user_query, (email,))
            user = cursor.fetchone()
            
            fetch_coupon_id_query = """SELECT coupon_id FROM coupons
                                    WHERE code = %s AND expiry_date >= NOW() AND is_active = TRUE """
            cursor.execute(fetch_coupon_id_query, (code,))
            coupon = cursor.fetchone()
            
            if not user or not coupon:
                print(f"{CRED}Redemption Failed: Invalid User or Expired Coupon{CEND}")
            
            # Verify Ownership if User bought that coupon ID or not
            
            check_transaction_query = """SELECT transaction_id FROM transactions
                                        WHERE user_id = %s AND coupon_id = %s AND status = 'SUCCESS'"""
            
            cursor.execute(check_transaction_query, (user['user_id'], coupon['coupon_id'],))
            transaction = cursor.fetchone()
            if not transaction:
                print(f"{CRED}Redemption Failed: You need to buy this Coupon first.{CEND}")
                return
            
            # Check if Already Redeemed
            redemption_id_if_redeemed_query = """SELECT redemption_id FROM redemptions WHERE user_id = %s AND coupon_id = %s"""
            cursor.execute(redemption_id_if_redeemed_query, (user['user_id'], coupon['coupon_id']))
            
            if cursor.fetchone(): # If Already Redeemed
                print(f"{CRED}Redemption Failed: Coupon Already Redeemed by User{CEND}")
                return
            
            # LOG THE REDEMPTION
            redemption_log_query = """INSERT INTO redemptions (user_id, coupon_id) VALUES (%s, %s)"""
            cursor.execute(redemption_log_query, (user['user_id'],coupon['coupon_id']))
            conn.commit()
            print(f"{C_green}Coupon Redeemed Succesfully{CEND}")
            
