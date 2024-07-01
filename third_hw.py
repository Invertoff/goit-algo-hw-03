import re

def normalize_phone(phone_number):
    # Removing all symbols except digits and "+".
    phone_number = re.sub(r'[^\d+]', '', phone_number)

    # If the number starts with "+", but not with "+38", we add "+38".
    if phone_number.startswith("+"):
        if not phone_number.startswith("+38"):
            phone_number = "+38" + phone_number[1:]
    else:
        # If the number starts from "0", we add "+380".
        if phone_number.startswith("0"):
            phone_number = "+380" + phone_number[1:]
        # If the number is not starting with "380", we add "+38".
        elif not phone_number.startswith("380"):
            phone_number = "+38" + phone_number
        else:
            # If number starts with "380", we add "+".
            phone_number = "+" + phone_number
            
    return phone_number

# Telephone numbers examples
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Normalization of phone numbers
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Result printing
print("Normalized phone numbers for SMS notifications:", sanitized_numbers)