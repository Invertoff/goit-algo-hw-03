from datetime import datetime, date, timedelta

def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y.%m.%d").date()
    except ValueError:
        raise ValueError("Incorrect date format, excpecting format: 'YYYY-MM-DD'")

def get_days_from_today(entered_date_str):
    try:
        # Transforming entered string object into date object
        entered_date = string_to_date(entered_date_str)

        # Receiving current date
        current_date = date.today()

        # Counting difference in days between entered date and current date.
        difference = entered_date - current_date
        difference_in_days = difference.days
        
        return difference_in_days
    except ValueError as error:
        print(error)
        return None    

entered_date_str = input("Enter the date in format YYYY.MM.DD: ")
print(get_days_from_today(entered_date_str))
