score = 0
# Ask for user's name

name = input("what's your name?")

# Greets user and introduces the Quiz
if name == "":
    print("Where's your name lil bro?")
print("Welcome to the Quiz,", name)
print("\nThis Quiz is about Formula One.")
answer = input("Are you ready to take the quiz?").lower()
if answer == "Yes" or answer == " Yes".lower():
    print("\nAlright, let's begin!")
elif answer == "":
    print("\nYou're emo aren't you? Anyways, let's begin")
else:
    print("\nToo bad, we're going to do the quiz anyways")

# Asks Question 1 

answer = input("Who has won 7 World Championship Titles?").lower()

# Shows Answer 1

if answer == "Lewis Hamilton" or answer == " Lewis Hamilton".lower():
    print("\nYou're Right!")
    score+= 5
elif answer == "":
    print("Make sure to type something next time?")
    print("\nSorry, but you're Wrong!")
else:
    print("\nSorry, but you're Wrong!")
print("\nThe Correct Answer was Lewis Hamilton!")

# Asks Question 2 

answer = input("Who stole Lewis Hamilton's 8th World Championship Title?").lower()

# Shows Answer 2

if answer == "Max Verstappen" or answer == " Max Verstappen".lower():
    print("\nYou're Right!")
    score+= 5
elif answer == "":
    print("Make sure to type something next time?")
    print("\nSorry, but you're Wrong!")
else:
    print("\nSorry, but you're Wrong!")
print("\nThe Correct Answer was Max Verstappen!")

# Asks Question 3 
question = "How many years has Rookie Fernando Alonso been racing in Formula One?"
a =21
b =17
c =20
d =19

answer = input("{}\n A.{} \n B.{} \n C.{} \n D.{}\n Answer Here:".format(question, a, b, c, d)).lower()

# Shows Answer 3
if answer == c or answer == "c" or answer == " c".lower():
    print("\nYou're right!")
    score+= 5
else:
    print("\nSorry, but you're Wrong!")
print("\nThe Correct Answer was C. 20 Years")
# Quiz Ends

print("In total, {} managed to accumalate {} points".format(name, score))
if score == 15:
    print ("\nWow! Perfect Score!")
if score < 10:
    print ("\nWelp, that's unfortunate, better luck next time!")
elif score < 15:
    print ("\nNice, that's a good score bro!")
print("\n\nThis is the end of the Quiz, hope you enjoyed.")