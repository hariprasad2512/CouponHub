import database_operations
from helper import ASCII_ART, get_expiry_date


def main():
    print(f"{ASCII_ART}")
    while True:
        
        print()
        print("\t\t1. Add New User")
        print("\t\t2. Create New Coupon")
        print("\t\t3. View All Available Coupons")
        print("\t\t4. View Your Coupons")
        print("\t\t5. Buy a Coupon")
        print("\t\t6. Redeem a Coupon")
        print("\t\t7. Exit\n\n")
        
        choice = input("Enter your Choice (1-7):  ")
        
        match choice:
           case '1':
               print("\n\t\tWelcome to CouponHub! Let's get you started! \n")
               name = input("Enter User Name:")
               email = input("Enter User Email: ")
               database_operations.add_user(name=name,email=email)
               print()
           case '2':
               print("\n\t\tLet's Create a New Coupon\n")
               coupon_name = input("Enter Coupon Name : ")
               code = input("Enter Coupon Code : ")
               discount = input("Enter Discount percentage: ")
               price = float(input("Enter Price: "))
               print("\nLet's Setup an Expiry Date for your Coupon Code :)\n")
               
               expiry = get_expiry_date()
               database_operations.create_coupon(coupon_name=coupon_name, code=code, discount_pct=discount, price=price, expiry_date=expiry)
               print()
           case '3':
               print("\n\t\t AVAILABLE COUPONS in the Market Right Now \n")
               database_operations.view_all_coupons()
                
           case '4':
               print("\n\t\t Your Available Coupons (Unredeemed) \n")
               email = input("Enter your email: ")
               database_operations.view_your_coupons(email=email)
               print()
           
           case '5':
               print("\n\t\tLet's Buy a New Coupon\n")
               email = input("Enter your email: ")
               code = input("Enter Coupon Code to buy: ")
               amount = float(input("Enter your Amount paying: "))
               print()
               database_operations.buy_coupon(email=email, amount_paid=amount, code=code)
               print()
           case '6':
               print("\n\t\tTime To Redeem your Coupon\n")
               email = input("Enter your Email : ")
               code = input("Enter Coupon Code to be Redeemed: ")
               print()
               database_operations.redeem_coupon(email=email, code=code)
               print()
           case '7':
               print("\n\t\t Exiting CouponHub, GoodBye\n")
               print(ASCII_ART)
               print("\n\t\tCouponHub ® 2026")
               print()
               break
           case _:
               print("\t\tOOPS. Invalid Input. Please enter a number from 1 to 7.") 


main()
        