# Exercise 7: Some Counting
print("Which loop would you like to run?")
print("1. Count up 0 → 50")
print("2. Count down 50 → 0")
print("3. Count up 30 → 50")
print("4. Count down 50 → 10 by 2")
print("5. Count up 100 → 200 by 5")
choice = int(input("Enter your choice (1-5): "))
if choice == 1:
    for i in range(0, 51):
        print(i)
elif choice == 2:
    for i in range(50, -1, -1):
        print(i)
elif choice == 3:
    for i in range(30, 51):
        print(i)
elif choice == 4:
    for i in range(50, 9, -2):
        print(i)
elif choice == 5:
    for i in range(100, 201, 5):
        print(i)
else:
    print("Invalid choice! Please enter a number from 1 to 5.")