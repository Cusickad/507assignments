import random

secret = random.randint(0, 1000)
while True:
    response = input("Enter a guess, or 'quit': ")
    if response == 'quit':
        break
    elif not response.isnumeric():
        print("Invalid input. Enter a number between 0 and 1000")
    elif not 0 <= int(response) or not 1000 >= int(response):
        print("Invalid input. Enter a number between 0 and 1000")
    else:
        if int(response) > secret:
            print("Too high! Try again.")
        if int(response) < secret:
            print("Too low! Try again.")
        if int(response) == secret:
            print("You got it!")
            break
