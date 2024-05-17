import random

score = 0
# ---- FUNCTIONS ----


# -- INTRO --
def intro():

    #Name Input
    name = input("What is the name of our player? ")

    #Greeting User
    print("\nWelcome {} to the quiz! This quiz is the Top 10 Most popular car brands!"
          .format(name))

    question = "Do you think you'll name them all? "
    skill = input(question).lower()

    # Replies to their reply
    if skill == "yes" or skill == " yes".lower():
        print("\nWell well, We'll see about that!")
    else:
        print("\nAlright! Maybe you'll do better than what you think!")


# -- ATTEMPTS --
def getAttempts():
        while True:
            Attempts = input("\nHow many attempts would you like to have? ")
            try:
                Attempts = int(Attempts)
                if Attempts >= 0:
                     return Attempts
                else:
                     print("\nPlease choose a positive number of Attempts!")
            except:
                 print("Please choose a number of Attempts!!")
                
# ---- MAIN CODE ----

intro()
getAttempts()