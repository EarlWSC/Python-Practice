Q_FORMAT = ("{}\n A. {} \n B. {} \n C. {} \n D. {}\n Answer Here:")
Q_RIGHT = ("\nYou're Right!")
Q_ELIF = ("Make sure to type something next time?" "\nSorry, but you're Wrong!")
Q_WRONG = ("\nSorry, but you're Wrong!")
play = "yes".lower()
score = 0

# Ask for user's name

name = input("what's your name?")

# Greets user and introduces the Quiz

if name == "":
    print("Where's your name lil bro?")
print("Welcome to the Quiz,", name)
print("\nThis Quiz is about Formula One!!!")

# Asks if they're ready for the Quiz
question = "Are you ready to take the quiz?"
answer = input(question).lower()

# Replies to their reply
if answer == "yes" or answer == " Yes".lower():
    print("\nAlright that's good!")
else:
    print("\nToo bad!")

while True:
    try:
        tries = input("\nHow many attempts would you like?\n Choose from 1 - 3 Attempts")
        tries = int(tries)
        break
    except:
        print("That's not a valid number, try again.")

while play == "yes".lower():
    question_attempts = tries
    while question_attempts > 0:
        # Asks Question 1 
        question = "Who has won 7 World Championship Titles?"
        answer = input(question).lower()

        # Shows Answer 1

        if answer == "Lewis Hamilton".lower() or answer == " Lewis Hamilton".lower():
            print(Q_RIGHT)
            score+= 5
        elif answer != "Lewis Hamilton".lower() and answer != " Lewis Hamilton".lower():
            print (Q_ELIF)
        else:
            print (Q_WRONG)

        question_attempts -= 1  
    print("\nThe Correct Answer was Lewis Hamilton!")

    while question_attempts > 0:
        # Asks Question 2 
        question = "Who stole Lewis Hamilton's 8th World Championship Title?"
        answer = input(question).lower()

        # Shows Answer 2

        if answer == "Max Verstappen".lower() or answer == " Max Verstappen".lower():
            print(Q_RIGHT)
            score+= 5
        elif answer != "Max Verstappen".lower() and answer != " Max Verstappen".lower():
            print (Q_ELIF)
        else:
            print (Q_WRONG)
        print("\nThe Correct Answer was Max Verstappen!")

        # Asks Question 3 

        question = "How many years has Rookie Fernando Alonso been racing in Formula One?"
        a = "21"
        b = "17"
        c = "20"
        d = "19"

        answer = input(Q_FORMAT.format(question, a, b, c, d)).lower()

        # Shows Answer 3

        if answer == c or answer == "c".lower() or answer == " c".lower():
            print(Q_RIGHT)
            score+= 5
        else:
            print(Q_WRONG)
        print("\nThe Correct Answer was C. 20 Years")

        # Quiz Ends
        print("In total, {} managed to accumalate {} points".format(name, score))
        if score == 15:
            print ("\nWow! Perfect Score!")
        if score < 10:
            print ("\nWelp, that's unfortunate, better luck next time!")
        elif score < 15:
            print ("\nNice, that's a good score!")

        # Asks user if they want to play the Quiz again
        play = input("Do you want to play again?")
        if play == "yes".lower():
            print ("\nAlright, let's do the quiz One more time!")
    
# End of Quiz
print("\n\nThis is the end of the Quiz, hope you enjoyed.")