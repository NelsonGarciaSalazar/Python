day = int(input("Input day of month"))
month = int(input("Input month of year"))
year = int(input("Input number of year"))

# Calculate number day
if 1 <= day <= 30:
    day = day + 1
    print(f"{day}/{month}/{year}")
else:
    if day == 30:
        day = 1
        month = month + 1
        if month < 12:
            month = month
        else:
            month = 1
            yaer = year + 1
        print(f"{day}/{month}/{year}")
    else:
        print("Date no valid")