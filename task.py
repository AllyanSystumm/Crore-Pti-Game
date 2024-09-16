import random

# Questions and answers in (question, [choices], correct_index) format
## tuple
questions = [
    ("Who is the current chairman of PTI?", ["Nawaz Sharif", "Asif Ali Zardari", "Imran Khan", "Bilawal Bhutto"], 2),
    ("What is the national sport of Pakistan?", ["Hockey", "Cricket", "Football", "Kabaddi"], 0),
    ("Which year did Pakistan win the Cricket World Cup?", ["1992", "1999", "2003", "2011"], 0),
    ("Who wrote the national anthem of Pakistan?", ["Faiz Ahmed Faiz", "Allama Iqbal", "Hafeez Jalandhari", "Ahmed Faraz"], 2),
]

# Lifeline flags
# dictionary
lifelines = {
    "50-50": True,
    "Ask the Audience": True,
    "Phone a Friend": True
}

# 50-50 Lifeline
def fifty_fifty(question):
    choices = question[1]
    correct_choice = question[2]
    other_choices = [i for i in range(len(choices)) if i != correct_choice]
    wrong_choice = random.choice(other_choices)
    return [correct_choice, wrong_choice]

# Ask the Audience Lifeline (randomly generates audience percentages)
def ask_the_audience(question):
    correct_choice = question[2]
    audience_vote = [0, 0, 0, 0]
    audience_vote[correct_choice] = random.randint(50, 80)
    remaining_percentage = 100 - audience_vote[correct_choice]
    for i in range(len(audience_vote)):
        if i != correct_choice:
            audience_vote[i] = random.randint(0, remaining_percentage)
            remaining_percentage -= audience_vote[i]
    return audience_vote

# Phone a Friend Lifeline (50% chance to suggest the correct answer)
def phone_a_friend(question):
    correct_choice = question[2]
    if random.random() > 0.5:
        return f"Your friend suggests the answer is: {question[1][correct_choice]}"
    else:
        return f"Your friend is unsure, but thinks it might be: {random.choice(question[1])}"

# Display the question and options
def display_question(question, options=None):
    print(f"\nQuestion: {question[0]}")
    choices = question[1] if options is None else options
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

# Main game function
def crore_pti_game():
    reward = 0
    for i, question in enumerate(questions):
        display_question(question)
        
        print("\nLifelines available: ", ", ".join([key for key, available in lifelines.items() if available]))
        lifeline_choice = input("Do you want to use a lifeline? (yes/no): ").lower()
        
        if lifeline_choice == "yes":
            chosen_lifeline = input("Which lifeline? (50-50, Ask the Audience, Phone a Friend): ").strip()
            
            if chosen_lifeline == "50-50" and lifelines["50-50"]:
                options = fifty_fifty(question)
                display_question(question, [question[1][i] for i in options])
                lifelines["50-50"] = False
            elif chosen_lifeline == "Ask the Audience" and lifelines["Ask the Audience"]:
                audience_votes = ask_the_audience(question)
                for idx, vote in enumerate(audience_votes):
                    print(f"Option {idx + 1}: {vote}%")
                lifelines["Ask the Audience"] = False
            elif chosen_lifeline == "Phone a Friend" and lifelines["Phone a Friend"]:
                print(phone_a_friend(question))
                lifelines["Phone a Friend"] = False
            else:
                print("Lifeline unavailable or invalid choice.")
        else:
            pass
        
        try:
            answer = int(input("\nEnter your answer (1-4): ")) - 1
            if answer == question[2]:
                reward += 1000000
                print(f"Correct! You've won {reward}!")
            else:
                print("Wrong answer! Game Over.")
                break
        except:
            print("Invalid input. Game Over.")
            break

# Start the game
crore_pti_game()
