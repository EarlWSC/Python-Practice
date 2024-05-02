score = 0
# Ask for user's name

name = input("what's your name?")

# Greets user and introduces the Quiz
if name == "":
    print("uhm what the sigma")
elif name == "":
    print("Huh, you're a non name, weird!!!")
else: 
    print("Welcome to the Quiz,", name)
print("This Quiz is about Formula One.")
answer = input("Are you ready to take the quiz?")
if answer == " yes":
    print("Alright, let's begin!")
elif answer == "":
    print("Alright, let's begin!")
else:
    print("Too bad, we're going to do the quiz anyways")

# Asks Question 1 

answer = input("Who has won 7 World Championship Titles?")

# Shows Answer 1

if answer == " Lewis Hamilton":
    print("You're Right!")
    score+= 5
elif answer == "":
    print("Make sure to type something next time?")
    print("Sorry, but you're Wrong!")
else:
    print("Sorry, but you're Wrong!")
print("The Correct Answer was Lewis Hamilton!")

# Asks Question 2 

answer = input("Who stole Lewis Hamilton's 8th World Championship Title?")

# Shows Answer 2

if answer == " Max Verstappen":
    print("You're Right!")
    score+= 5
elif answer == "":
    print("Make sure to type something next time?")
    print("Sorry, but you're Wrong!")
else:
    print("Sorry, but you're Wrong!")
print("The Correct Answer was Max Verstappen!")

# Quiz Ends

print("In total, you managed to accumalate", score)
if score == 10:
    print ("Wow! Perfect Score!")
if score < 5:
    print ("Welp, that's unfortunate, better luck next time!")
elif score < 10:
    print ("Nice, that's a good score bro!")
print("This is the end of the Quiz, hope you enjoyed.")