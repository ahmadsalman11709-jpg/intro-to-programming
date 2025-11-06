# Exercise 3: Biography
# --- BASIC ---
bio = {"name": "Ahmad Khan", "hometown": "Abu Dhabi", "age": 18}
print(f"Name: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")

# --- ADVANCED ---
name = input("Enter your full name: ")  # handles multiple words
hometown = input("Enter your hometown: ")
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age (e.g., 18).")
bio = {"name": name, "hometown": hometown, "age": age}
print(f"\nName: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")