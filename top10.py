import random
ANSWERS = ["Ferrari", "Mercedes", "Alpine", "Red Bull", "Mclaren", "Kick Sauber", "Aston Martin", "Williams", "Visa CashApp Racing Bulls", "Haas"]
guesses = []
score = 0
MAX_TURNS = 10
play = "yes".lower() or " yes".lower()
# ---- FUNCTIONS ----
def name():
    name = input("What is the name of our player? ")

        #Greeting User
    print("\nWelcome {} to the quiz! This quiz is the 10 Teams of the 2024 Formula 1 WDC!!"
        .format(name))

# -- Intro --
def intro():

    #Name Input
    name()

    question = "Do you think you'll name them all? "
    skill = input(question).lower()

    # Replies to their reply
    if skill == "yes" or skill == " yes".lower():
        print("\nWell well, We'll see about that!")
    else:
        print("\nAlright! Maybe you'll do better than what you think!")


# -- Attempts --
def getAttempts():
        while True:
            Attempts = input("\nHow many attempts would you like to have? ")
            try:
                Attempts = int(Attempts)
                if Attempts >= 1 and Attempts <= MAX_TURNS:
                     print("Ok, you will have {} Attempts.".format(Attempts))
                     return Attempts
                elif Attempts >= MAX_TURNS:
                     print("Too many attempts, choose a number below 10 Attempts!")
                else:
                     print("Please choose a positive number of Attempts!")
            except:
                 print("Please choose a number of Attempts!!")
            

# -- Miscellaneous --
def scoreadd(number):
    return number + 5
def inList(answer, list):
     if answer in list:
          return True
     else:
          return False
# ---- MAIN CODE ----
# - Intro -
intro()
# -- Main Game --
while play == "yes".lower() or " yes".lower():
    Attempts = getAttempts()
    score = 0
    while Attempts > 0: 
        # - Asks the Question -
        answer = input("\nName one of the 10 Teams in Formula 1 in 2024.")

    # - Checks if right or wrong -
        if inList(answer,ANSWERS):
        # - Checks if guessed already or not-
            # Guessed Already
            if inList(answer,guesses):
                print("\nYou've already guessed that. Here's the list you've already guessed:\n {}".format(len(guesses)))
            # Correct Answer
            else:
                print("Awesome! That's one of them!")
                score += 1
                guesses.append(answer)
                print("\nYou guessed {}. \nYou have named {} of the brands so far and have {} Attempts remaining!".format(len(guesses),score,Attempts))
        # Wrong Answer
        else:
            print("\nIncorrect!")
            Attempts -= 1
            print("\nYou guessed {}. \nYou have named {} of the brands so far and have {} Attempts remaining!".format(len(guesses),score,Attempts))
    # - Checks if guessed all -
        if score >= 10:
            break

    # -- End of Quiz --
    print("\nGood job! You managed to name {}/10 of the Teams.".format(score))
    # - Wanna play again? - 
    play = input("\nWould you like to play again?")
    if play == "yes".lower() or " yes".lower():
        print("Alright, let's play again!")
    else:
        print("Thanks for playing.")
        break