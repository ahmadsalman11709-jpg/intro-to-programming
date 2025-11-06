# Exercise 6: Brute Force Attack
# --- BASIC ---
password = "12345"  # correct password
# Keep asking until the user enters the right one
while True:
    guess = input("Enter password: ")
    if guess == password:
        print("Access Granted ✅")
        break
    else:
        print("Wrong password, try again.")

# --- ADVANCED ---
password = "12345"
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    guess = input("Enter password: ")
    if guess == password:
        print("Access Granted ✅")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempt(s) left.")
        else:
            print("Maximum attempts reached! Authorities alerted 🚨")