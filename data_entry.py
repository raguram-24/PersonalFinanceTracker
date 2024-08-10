from datetime import datetime
date_format = "%d-%m-%Y"

def get_date(prompt,allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try : 
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid Date Format. Please Enter the Date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the Amount : "))
        if amount <= 0 :
            raise ValueError("Amount must be non-negative and non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()