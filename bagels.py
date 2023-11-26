import random
num_digits = 3
max_guesses = 10
def main():
    print("I'm thinking of a %s-digit number. Try to guess what it is." % (num_digits))
    print("The clues I give are:")
    print("Pico if one digit is correct but in the wrong position")
    print("Fermi if one digit is correct and in the right position")
    print("Bagels if no digits are correct")
    while True:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have %s guesses to get it." % (max_guesses))
        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess #%s: " % (numGuesses))
                guess = input()
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print("You ran out of guesses. The answer was %s." % (secretNum))
        print("Do you want to play again? (yes or no)")
        if not input().lower().startswith("y"):
            break
def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
if __name__ == '__main__':
    main()