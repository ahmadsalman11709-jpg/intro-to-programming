# Exercise 4: Primitive Quiz 


# --- ADVANCED ---
def ask_question(country, correct_capital):
    # take answer normally and make it lowercase
    answer = input("What is the capital of " + country + "? ").lower()
    if answer == correct_capital.lower():
        print("✅ Correct!")
        return True
    else:
        print("❌ Wrong! The correct answer is " + correct_capital)
        return False
# dictionary of 10 European countries
quiz = {"France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Switzerland": "Bern",
    "Sweden": "Stockholm"}
score = 0
# ask each question
for country, capital in quiz.items():
    if ask_question(country, capital):
        score += 1
print("\nYour final score:", score, "/", len(quiz))