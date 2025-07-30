import random
guess = [1, 2, 3, 4, 5, 6]
while True:
    num = random.choice(guess)
    print("Computer's guessed a number")
    user = int(input("Enter your guess: "))
    if user < 1 or user > 6:
        print("ohoo! Sorry you guessed wrong")
    elif user == num:
        print("You guessed it right!")
    else:
        print("Better luck next time! The computer guessed:",num)
    play2 = input("Do you want to play again? (yes/no): ").lower()
    if play2 != 'yes':
        print("Thank you for playing!")
        break
