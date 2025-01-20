# Function to welcome the user
def welcome_user():
    print("Hello and welcome to your Workout Assistant! ")
    print("I'm here to help you with your fitness goals! ")
    print("Let's get started!")

# Function to collect the user's name and age
def get_user_info():
    name = input("What is your name? ")
    age = input(f"Nice to meet you, {name}! How old are you? ")
    return name, age

# Function to display the main menu
def show_menu():
    print("\nHow can I assist you today?")
    print("1. Get a workout plan")
    print("2. Learn about exercises")
    print("3. Get nutrition tips")
    print("4. Motivation and encouragement")
    print("5. Exit")

# Function to give a simple workout plan
def workout_plan():
    print("\nGreat! Let's create a workout plan for you!")
    print("What is your main goal?")
    print("1. Lose weight")
    print("2. Build muscle")
    print("3. Improve endurance")
    goal = input("Please choose 1, 2, or 3: ")

    if goal == "1":
        print("I recommend a combination of cardio and full-body strength training.")
    elif goal == "2":
        print("Focus on strength training with compound exercises like squats and bench press.")
    elif goal == "3":
        print("Try doing high-intensity interval training (HIIT) or running to improve your endurance.")
    else:
        print("Sorry, I didn't understand that choice.")
        
# Function to explain exercises
def learn_exercises():
    print("\nWhat kind of exercises would you like to learn about?")
    print("1. Upper body exercises")
    print("2. Lower body exercises")
    print("3. Full-body exercises")
    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        print("Upper body exercises include push-ups, bench press, and shoulder press.")
    elif choice == "2":
        print("Lower body exercises include squats, lunges, and leg press.")
    elif choice == "3":
        print("Full-body exercises include burpees, deadlifts, and kettlebell swings.")
    else:
        print("Sorry, I didn't understand that choice.")

# Function to give basic nutrition tips
def nutrition_tips():
    print("\nNutrition is important! Here are some tips:")
    print("1. Eat protein-rich foods like chicken, eggs, and beans.")
    print("2. Carbs like rice, oats, and potatoes give you energy.")
    print("3. Don't forget healthy fats like avocado, nuts, and olive oil.")
    print("4. Drink plenty of water throughout the day.")

# Function to give motivation
def motivation():
    print("\nHere's a motivational quote for you:")
    print("The only bad workout is the one that didn't happen. – Anonymous")
    print("You got this! Keep pushing towards your goals! 💪")

# Main function to run the chatbot
def main():
    welcome_user()  # Welcome the user
    name, age = get_user_info()  # Collect user's name and age
    
    # Chatbot conversation loop
    while True:
        show_menu()  # Display the menu of options
        choice = input("Please enter the number of your choice: ")  # User makes a choice

        if choice == "1":
            workout_plan()  # Provide a workout plan
        elif choice == "2":
            learn_exercises()  # Teach exercises
        elif choice == "3":
            nutrition_tips()  # Provide nutrition tips
        elif choice == "4":
            motivation()  # Give motivation
        elif choice == "5":
            print("\nThanks for chatting! Stay fit and healthy! 💪")  # Exit the chatbot
            break
        else:
            print("Sorry, I didn't understand that choice. Please choose again.")  # Invalid choice
        
        # Ask if the user wants to continue or exit
        continue_conversation = input("\nWould you like to continue? (yes/no): ")
        if continue_conversation.lower() != "yes":
            print("\nThanks for chatting! Stay fit and healthy! 💪")
            break

if __name__ == "__main__":
    main()  # Start the chatbot