import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        """Bagels, a deductive logic game.
     By Al Sweigart al@inventwithpython.com
    
     I am thinking of a {}-digit number with no repeated digits.
     Try to guess what it is. Here are some clues:
     When I say:    That means:
       Pico         One digit is correct but in the wrong position.
       Fermi        One digit is correct and in the right position.
       Bagels       No digit is correct.
    
     For example, if the secret number was 248 and your guess was 843, the
     clues would be Fermi Pico.""".format(
            NUM_DIGITS
        )
    )

    while True:

        secretNum = getSecretNum()
        print("I have thought up a number")
        print("You have a total of {} guesses to get it right".format(MAX_GUESSES))

        numberGuesses = 1
        while numberGuesses <= MAX_GUESSES:
            guess = ""

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}".format(numberGuesses))
                guess = input(">> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numberGuesses += 1

            if guess == secretNum:
                break
            if numberGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNum))

        print("Do want to play again? Yes or No")
        if not input(">>").lower().startswith("y"):
            break


def getSecretNum():
    """Returns a string made of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair

    Args:
        guess (_type_): User input guess
        secretNum (_type_): Target Secret Number
    """
    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
