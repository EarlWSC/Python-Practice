# Ask for user's name
name = input("what's your name?")
# Greets user and introduces the Quiz
print("Welcome to the Quiz,", name)
print("This Quiz is about Formula One.")
# Asks Question
answer = input("Who has won 7 World Championship Titles?")
# Show the Answer
if answer == "Lewis Hamilton":
    print("You're Right!")
elif answer == "":
    print("Make sure to type something next time.")
    print("Sorry, but you're Wrong!")
else:
    print("Sorry, but you're Wrong!")
print("The Correct Answer was Lewis Hamilton!")
# Quiz Ends
print("This is the end of the Quiz, hope you enjoyed.")