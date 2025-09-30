for number in range(1, 11, 3): # Prints 1-10, in increments of 3
    print(number)

number = 7
while True:
    play = input("Would you like to play? (Y/n) ")

    if play == "n":
        break  # Exit the WHILE loop

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")