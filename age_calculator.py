#Amin was here
#This project is completly written by Amin from 0
from datetime import date
today = date.today()
#Year selection
while True:
    try:
        birthyear = int(input("Please enter the year you were born: "))
        if today.year >= birthyear >= 0:
            break
        else:
            print("Your date of birth cannot be in the future. LoL")
    except:
        print("Please enter a valid year")
print(["1.January", "2.February", "3.March", "4.April", "5.May", "6.June", "7.July", "8.August", "9.September", "10.October", "11.November", "12.December"])
#Month selection
while True:
    try:
        birthmonth = int(input("Please enter the month you were born: "))
        if birthyear == today.year:
            if today.month >= birthmonth >= 1:
                break
            else:
                print("Your date of birth cannot be in the future. LoL")
        else:
            break
    except:
        print("Please enter a valid month")
if birthyear == today.year and birthmonth == today.month:
    days = today.day
    print(f"Enter days between: 1-{days}")
else:
    if birthmonth == 1 or birthmonth == 3 or birthmonth == 5 or birthmonth == 7 or birthmonth == 8 or birthmonth == 10 or birthmonth == 12:
        days = 31
        print(f"Enter days between: 1-{days}")
    elif birthmonth == 2:
        if birthyear%4==0 and birthyear%100!=0 or birthyear%400==0:
            days = 29
        else:
            days = 28
        print(f"Enter days between: 1-{days}")
    else:
        days = 30
        print(f"Enter days between: 1-{days}")
#Day selection
while True:
    try:
        birthday = int(input("Please enter the date you were born: "))
        if days >= birthday >= 1:
            break
        elif birthyear == today.year and birthmonth == today.month and birthday > today.day:
            print("Your date of birth cannot be in the future. LoL")
        else:
            print("Please enter a valid day")
    except:
        print("Please enter a valid day")
#Leap Year Calculator For Extra Days
leap_counter = 0
for i in range(birthyear,today.year):
    if i%4==0 and i%100!=0 or i%400==0:
        leap_counter = leap_counter+1
#Lived Year Calculation
if birthyear == today.year:
    lived_year = 0
elif birthyear == today.year-1 and birthmonth >= today.month and birthday > today.day:
    lived_year = 0
else:
    if birthmonth == today.month and birthday > today.day:
        lived_year = (today.year - birthyear)-1
    elif birthmonth > today.month:
        lived_year = today.year - birthyear-1
    else:
        lived_year = today.year - birthyear
#Lived Month Calculator
if birthmonth < today.month-1+12 and birthday > today.day:
    lived_month = today.month - birthmonth + 12-1
elif birthmonth == today.month-1+12 and birthday > today.day:
    lived_month = today.month - 1
else:
    if today.month-birthmonth == 0:
        lived_month = 0
    else:
        lived_month = today.month - birthmonth + 12
#Lived Day Calculator
if birthmonth == today.month-1+12 and birthday > today.day:
    lived_day = today.day - birthday + days
else:
    if today.day-birthday == 0:
        lived_day = 0
    elif today.month-birthmonth == 0 and birthday < today.day:
        lived_day = today.day - birthday
    else:
        lived_day = today.day - birthday + days
if lived_day >= 31:
    lived_day = lived_day - 31
print(f"You have lived for {lived_year} years, {lived_month} months and {lived_day} days.")
#Age With Considering Leap Years
if leap_counter > 0:
    while True:
        consider_leap = input("Do you want to consider leap years and extra 1 days in your age (Y to yes, N to exit)?: ")
        if consider_leap == "Y" or consider_leap == "y":
            print(f"You lived {leap_counter} days in leap years")
            if lived_day+leap_counter >= 31:
                lived_month = lived_month + 1
                lived_days_with_leap = lived_day+leap_counter - 31
                print(f"You have lived for {lived_year} years, {lived_month} months and {lived_days_with_leap} days.")
                break
            else:
                print(f"You have lived for {lived_year} years, {lived_month} months and {lived_day+leap_counter} days.")
                break
        elif consider_leap == "N" or consider_leap == "n":
            exit()
        else:
            print("Your entered option is not valid!")