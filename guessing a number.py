print("              Welcome to the Guessing a Number Game ")
print("You have to guess a number if the number matches the random number")
print("you win the game else you will only get three chances")
name=input("Enter the user name")
import random
for i in range (1,4):
    print("Chance",i)
    r=random.randint(10,50)
    h=int(input("Guess the number between the range 10 to 50:"))
    if r>h:
        print("Guessed number is",r)
        print("The number you guessed is smaller then the number we guess.")
        print("So sorry, you are losser .")
    elif r<h:
        print("The guessed number is",r)
        print("The number you guessed is higher then the number we guess.")
        print("So sorry, you are losser .")
    else:
        print("Guessed number is",r)
        print("The number you guessed is equal to the number we guess.")
        print("You win")
