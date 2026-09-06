from datetime import datetime
ASCII_ART = """
 ███   ███  █   █ ████   ███  █   █ █   █ █   █ ████     
█     █   █ █   █ █   █ █   █ ██  █ █   █ █   █ █   █    
█     █   █ █   █ ████  █   █ █ █ █ █████ █   █ ████     
█     █   █ █   █ █     █   █ █  ██ █   █ █   █ █   █    
 ███   ███   ███  █      ███  █   █ █   █  ███  ████     
 
 """


def get_expiry_date():
    while True:
        expiry_date_input = input("Enter expiry date (for example, 25 December 2026): ").strip()
        expiry_time_input = input("Enter expiry time (for example, 12:30 PM): ").strip()

        for date_format in ("%d %B %Y", "%d %b %Y"):
            try:
                expiry_date = datetime.strptime(expiry_date_input, date_format)
                break
            except ValueError:
                continue
        else:
            print("Invalid date. Please use a format like 25 December 2026.")
            continue

        try:
            expiry_time = datetime.strptime(expiry_time_input, "%I:%M %p").time()
        except ValueError:
            print("Invalid time. Please use a format like 12:30 PM.")
            continue

        expiry_datetime = datetime.combine(expiry_date.date(), expiry_time)
        return expiry_datetime.strftime("%Y-%m-%d %H:%M:00")

