import random
ANSWERS = ["Lexus", "Mercedes", "Jaguar", "Chevrolette", "Mclaren", "Audi", "Aston Martin", "BMW", "Lotus", "Porsche"]

score = 0
MAX_TURNS = 10
# ---- FUNCTIONS ----


# -- Intro --
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


# -- Attempts --
def getAttempts():
        while True:
            Attempts = input("\nHow many attempts would you like to have? ")
            try:
                Attempts = int(Attempts)
                if Attempts >= 0 and Attempts <= MAX_TURNS:
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
def isCorrect(answer, list):
     if answer in list:
          return True
     else:
          return False
# ---- MAIN CODE ----

intro()
Attempts = getAttempts()
# -- Main Game --
score = 0
while Attempts > 0: 
    answer = input("\nName one of the Top 10 most popular car brands based off popularity rankings. ")

    if isCorrect(answer,ANSWERS).lower():
        print("Nice! That's one of them.")
        score += 1
    else:
        print("Nice try! Try naming a popular sports car brand like Porsche?")
        Attempts -= 1

print("Good job! You managed to name {}/10 of the brands!".format(score))
        