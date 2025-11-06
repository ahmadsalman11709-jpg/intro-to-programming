# Exercise 8: Simple Search 
# --- BASIC ---
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
if "Sam" in names:
    print("Sam found!")
else:
    print("Sam not found.")

# --- OPTIONAL ---
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_name = input("Enter a name to search: ")
if search_name in names:
    print(search_name, "found in the list!")
else:
    print(search_name, "not found.")