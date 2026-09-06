import database_operations
from helper import ASCII_ART, get_expiry_date


def main():
    while True:
        print(f"{ASCII_ART}")
        print()
        print("\t\t1. Add New User")
        print("\t\t2. Create New Coupon")
        print("\t\t3. Buy a Coupon")
        print("\t\t4. Redeem a Coupon")
        print("\t\t5. Exit\n\n")
        
        choice = input("Enter your Choice (1-5):  ")
        
        match choice:
           case '1':
               print("\n\t\tWelcome to CouponHub! Let's get you started! \n")
               name = input("Enter User Name:")
               email = input("Enter User Email: ")
               database_operations.add_user(name=name,email=email)
               print()
           case '2':
               print("\n\t\tLet's Create a New Coupon\n")
               code = input("Enter Coupon Code : ")
               discount = input("Enter Discount percentage: ")
               price = float(input("Enter Price: "))
               print("\nLet's Setup an Expiry Date for your Coupon Code :)\n")
               
               expiry = get_expiry_date()
               database_operations.create_coupon(code=code, discount_pct=discount, price=price, expiry_date=expiry)
               print()
           case '3':
               print("\n\t\tLet's Buy a New Coupon\n")
               email = input("Enter your email: ")
               code = input("Enter Coupon Code to buy: ")
               amount = float(input("Enter your Amount paying: "))
               print()
               database_operations.buy_coupon(email=email, amount_paid=amount, code=code)
               print()
           case '4':
               print("\n\t\tTime To Redeem your Coupon\n")
               email = input("Enter your Email : ")
               code = input("Enter Coupon Code to be Redeemed: ")
               print()
               database_operations.redeem_coupon(email=email, code=code)
               print()
           case '5':
               print("\n\t\t Exiting CouponHub, GoodBye\n")
               print(ASCII_ART)
               print("\n\t\tCouponHub ® 2026")
               print()
               break
           case _:
               print("\t\tOOPS. Invalid Input. Please enter a number from 1 to 5.") 


main()
        