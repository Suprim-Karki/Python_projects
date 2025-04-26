year = int(input("Enter a year: "))   # Here, you take the input from the user

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):   
    print(f"{year} is a leap year!!")
else:
    print("{year} is not a leap year!!")