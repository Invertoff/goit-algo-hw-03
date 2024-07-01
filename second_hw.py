import random

# Function generating a list of random numbers.
def get_numbers_ticket(min_value, max_value, quantity):
    random_numbers_list = [random.randint(min_value, max_value) for i in range(quantity)]
    return random_numbers_list

#-------------------------------------------------
# Function generating a list of unique random numbers.
def get_valid_unique_numbers(min_value, max_value, quantity):
    unique_numbers_set = set()
    while len(unique_numbers_set) < quantity:
        unique_numbers_set.add(random.randint(min_value, max_value))
    return list(unique_numbers_set)

#-------------------------------------------------
# Function to validate that the user input is an integer within a specified range.
def get_valid_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))  # Prompt for user input
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Value must be between {min_value} and {max_value}. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

#-------------------------------------------------

# Loop until the user provides valid minimum and maximum values.
while True:
    # Getting the minimum value from the user.
    min_value = get_valid_input("Enter a minimum number (equal or greater than 1): ", min_value=1)
    # Getting the maximum value from the user.
    max_value = get_valid_input("Enter a maximum number (equal or less than 1000): ", min_value=1, max_value=1000)

    # Check if min_value is less than or equal to max_value
    if min_value > max_value:
        print("Minimum value cannot be greater than maximum value. Please try again.")
    else:
        break

# Getting the quantity of random numbers from the user.
quantity = get_valid_input("Enter a quantity of matches (at least 1): ", min_value=1)

# Checking if the range is sufficient to generate the required quantity of unique numbers.
if max_value - min_value + 1 < quantity:
    print(f"Range is too small to generate {quantity} unique numbers. Please try again.")
else:
    # Generating unique random numbers.
    unique_random_numbers = get_valid_unique_numbers(min_value, max_value, quantity)
    unique_random_numbers.sort()
    print("Unique random numbers:", unique_random_numbers)
