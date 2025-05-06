''' Age calculator '''

from datetime import date

# Get today's date
today = date.today()

# Get user input
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day: "))

# Create a birthdate object
birth_date = date(birth_year, birth_month, birth_day)

# Calculate age
age = today.year - birth_date.year

# Adjust if birthday hasn't happened yet this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"You are {age} years old.")
