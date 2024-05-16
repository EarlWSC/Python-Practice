# Imports random
import random

# Variables
Q_FORMAT = "{}\n A. {} \n B. {} \n C. {} \n D. {}\n Answer Here: "

PERFECT = ["\nPerfect Score! You are a True Formula 1 Fan!",
           "\nUnbelievable Stuff! You are the Ultimate Formula 1 Fan!"]
GOOD = ["\nGood Score, Almost there to being a True Formula 1 Fan.",
        "\nNice Job! You're almost there, keep going!"]
LOL = ["\nWelp, maybe it's just an inchident today?",
       "\nI am stupid - Charles Leclerc at Baku 2022."]

Q_RIGHT = ["\nYou're Right!", 
           "\nAwesome Job!", 
           "\nFantastic!"]

Q_ELSE = ["\nMake sure to type something next time?" 
          "\nSorry, but you're Wrong!", 
          "\nYou really need to type a real answer."]

Q_WRONG = ["\nSorry, but you're Wrong!", 
           "\n Unfortunately, you're Incorrect.", 
           "\nClose guess! You're wrong though."]

QUESTIONS = ["Who has won 7 World Championship Titles?",
            "Who stole Lewis Hamilton's 8th World Championship Title?",
            "How many years has Rookie Fernando Alonso been racing in Formula One?",]

L_OPTIONS = [["Max Verstappen", "Lewis Hamilton", "Kimi Raikkonen", "Mick Shumacher"],
           ["Valtteri Bottas", "Sebastian Vettel", "Lance Stroll", "Max Verstappen"],
            ["21 Years", "17 Years", "20 Years", "19 Years"]]

S_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [1,3,2]
play = "yes" or " yes".lower()

# Ask for user's name

name = input("What's your name? ")

# Greets user and introduces the Quiz

if name == " ":
    print("Where's your name lil bro?")
print("Welcome to the Quiz,", name)
print("\nThis Quiz is about Formula One!!!")

# Asks if they're ready for the Quiz
question = "Are you ready to take the quiz? "
answer = input(question).lower()

# Replies to their reply
if answer == "yes" or answer == " yes".lower():
    print("\nAlright that's good!")
else:
    print("\nToo bad!")

while True:
    try:
        tries = input("\nHow many attempts would you like?\n Choose from 1 - 3 Attempts ")
        tries = int(tries)
        print("\nOk, you will have {} attempts!".format(tries))
        break
    except:
        print("\nThat's not a valid number, try again.")


while play == "yes" or " yes".lower():
    score = 0
    for x in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            # Asks Question 1 
            # Who has won 7 World Championship Titles?
            answer = input(Q_FORMAT.format(QUESTIONS[x], L_OPTIONS[x][0],
                                            L_OPTIONS[x][1], L_OPTIONS[x][2], L_OPTIONS[x][3])).lower()

            # Shows Answer 1

            if answer == L_OPTIONS[x][ANSWERS[x]].lower() or answer == S_OPTIONS[ANSWERS[x]].lower():
                print(random.choice(Q_RIGHT))
                score+= 5
                break
            elif answer in L_OPTIONS[x] or answer in S_OPTIONS[x].lower():
                print (random.choice(Q_WRONG))

            else:
                print (random.choice(Q_ELSE))
            question_attempts -= 1
            while question_attempts <= 0:     
                print("\nThe Correct Answer was {}.".format(L_OPTIONS[x][ANSWERS[x]]))
                break

    # Quiz Ends
    print("In total, {} managed to accumalate {} points".format(name, score))
    if score == 15:
        print (random.choice(PERFECT))
            
    elif score < 10:
        print (random.choice(GOOD))
            
    elif score < 15:
        print (random.choice(LOL))
    question_attempts = -1  

     # Asks user if they want to play the Quiz again
    play = input("Do you want to play again?")
    if play == "yes" or " yes".lower():
        print ("\nAlright, let's do the quiz One more time!")

    break
    

    
# End of Quiz
print("\n\nThis is the end of the Quiz, hope you enjoyed.")