# Imports random
import random

# Variables
Q_FORMAT = "{}\n A. {} \n B. {} \n C. {} \n D. {}\n Answer Here:"

Q_RIGHT = ["\nYou're Right!", 
           "\nAwesome Job!", 
           "\nFantastic!"]

Q_ELIF = ["\nMake sure to type something next time?" 
          "\nSorry, but you're Wrong!", 
          "\nYou really need to type a real answer."]

Q_WRONG = ["\nSorry, but you're Wrong!", 
           "\n Unfortunately, you're Incorrect.", 
           "\nClose guess! You're wrong though."]

QUESTIONS = ["Who has won 7 World Championship Titles?",
            "Who stole Lewis Hamilton's 8th World Championship Title?",
            "How many years has Rookie Fernando Alonso been racing in Formula One?",]

L_OPTIONS = [[" Max Verstappen", " Lewis Hamilton", " Kimi Raikkonen", " Mick Shumacher"],
           [" Valteri Bottas", " Sebastian Vettel", " Lance Stroll", " Max Verstappen"],
            ["21", "17", "20", "19"]]
S_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [2,4,3]
play = "yes".lower()

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
        print("\nOk, you will have {} attempts!".format(tries))
        break
    except:
        print("\nThat's not a valid number, try again.")


while play == "yes".lower():
    score = 0
    question_attempts = tries
    while question_attempts > 0:
        # Asks Question 1 
        answer = input(Q_FORMAT.format(QUESTIONS[0], L_OPTIONS[0][0],
                                        L_OPTIONS[0][1], L_OPTIONS[0][2], L_OPTIONS[0][3])).lower()

        # Shows Answer 1

        if answer == "Lewis Hamilton".lower() or answer == " Lewis Hamilton".lower():
            print(random.choice(Q_RIGHT))
            score+= 5
            break
        elif answer == " ".lower():
            print (random.choice(Q_ELIF))

        else:
            print (random.choice(Q_WRONG))


        question_attempts -= 1
        while question_attempts <= 0:     
            print("\nThe Correct Answer was Lewis Hamilton!")
            break


    while question_attempts > 0:
        # Asks Question 2 
        answer = input(Q_FORMAT.format(QUESTIONS[1], L_OPTIONS[1][0],
                                        L_OPTIONS[1][1], L_OPTIONS[1][2], L_OPTIONS[1][3])).lower()

        # Shows Answer 2

        if answer == "Max Verstappen".lower() or answer == " Max Verstappen".lower():
            print(random.choice(Q_RIGHT))
            score+= 5
            break
        elif answer == " ".lower():
            print (random.choice(Q_ELIF))

        else:
            print (random.choice(Q_WRONG))


        question_attempts -= 1 
        while question_attempts <= 0: 
            print("\nThe Correct Answer was Max Verstappen!")
            break

        # Asks Question 3 
    while question_attempts > 0: 
        a = "21"
        b = "17"
        c = "20"
        d = "19"

        answer = input(Q_FORMAT.format(question, a, b, c, d)).lower()

        # Shows Answer 3

        if answer == c or answer == "c".lower() or answer == " c".lower():
            print(random.choice(Q_RIGHT))
            score+= 5
            break
        else:
            print(random.choice(Q_WRONG))

            
        question_attempts -= 1 

        while question_attempts <= 0:
            print("\nThe Correct Answer was C. 20 Years")
            break

    # Quiz Ends
    print("In total, {} managed to accumalate {} points".format(name, score))
    if score == 15:
        print ("\nWow!")
            
    if score < 10:
        print ("\nWelp,")
            
    elif score < 15:
        print ("\nNice!")
    question_attempts = -1  

     # Asks user if they want to play the Quiz again
    play = input("Do you want to play again?")
    if play == "yes".lower():
        print ("\nAlright, let's do the quiz One more time!")
    

    
# End of Quiz
print("\n\nThis is the end of the Quiz, hope you enjoyed.")