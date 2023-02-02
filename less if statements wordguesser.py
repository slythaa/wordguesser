import random

#simple word guesser that gives you 5 chances and with each chance another letter of the word is given
#revised version with less if statements


def twoPlayer():

    host_Word = str(input("Enter a word player 2 needs to guess (has to be atleast 6 letters long): "))

    while len(host_Word) < 6:

        host_Word = input("Word must have 6 or more letters. Enter a new word: ")

    guess =   print(  f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"\n"
                      f"This word has", len(host_Word), "letters.")
    print(f"The first letter of this word is: {host_Word[0]}")

    for i in range(5):
        guessed_Word = input("Try to guess: ")
        if guessed_Word == host_Word:
            print(f"You got it right! The word was {host_Word}!")
            break

        print(f"Letter number {i + 2} is: {host_Word[i + 1]}")
    else:
        print(f"You ran out of guesses! The word was {host_Word}! Try again next time!")

def onePlayer():

    with open("1000randomwords.txt") as f:
        words = [word.strip() for word in f if len(word.strip()) >= 6]
        computer = (random.choice(words))

    print(f"This word has", len(computer), "letters.")
    print(f"The first letter of this word is: {computer[0]}")

    for i in range(5):
        guessed_Word = input("Try to guess: ")
        if guessed_Word == computer:
            print(f"You got it right! The word was {computer}!")
            break

        print(f"Letter number {i + 2} is: {computer[i + 1]}")
    else:
        print(f"You ran out of guesses! The word was {computer}! Try again next time!")

playing = None

while playing != "n":

    oneOrTwo = input("One or two players? (1/2): ")

    if oneOrTwo == "1":
        onePlayer()
        playing = input("Again? (y/n): ")

    elif oneOrTwo == "2":
        twoPlayer()
        playing = input("Again? (y/n): ")

    else:
        pass

if playing == "n":
    print("Thanks for playing!")








