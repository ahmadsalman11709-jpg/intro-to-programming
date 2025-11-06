# Exercise 5: Days of the Month (Basic + Advanced Combined )
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month = int(input("Enter month number (1–12): "))
if 1 <= month <= 12:
    days = months[month]
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        if leap == "yes":
            days = 29
            print("Leap year adjustment applied.")
    print(f"Month {month} has {days} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")