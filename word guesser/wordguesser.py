import random

#simple word guesser that gives you 5 chances and with each chance another letter of the word
#self-reminder: the len() function can be used not only to print out the number of letters a word has,
#but can also serve as an integer for a word. idk how i missed this, now that i look back its such a dumb thing
#theres probably a way to do this more cleaner and with less if statements, but it works so idk

one_Or_Two = input("One or two players? (1/2): ")

def twoPlayer():

    host_Word = str(input("Enter a word player 2 needs to guess (has to be atleast 5 letters long): "))

    while len(host_Word) < 5:

        host_Word = input("Word must have 5 or more letters. Enter a new word: ")

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
                      f"This word has", len(host_Word), "letters. Try to guess: ")

    guessed_Word = input()

    def wrongWord():
        if host_Word != guessed_Word:
            print(f"The first letter is: {host_Word[0]}")

        while guessed_Word != host_Word:

            second_Guess = input("Guess a second time: ")

            if second_Guess != host_Word:
                print(f"The second letter is: {host_Word[1]}")

            if second_Guess == host_Word:
                print(f"You got it right! The word was {host_Word}!")
                break

            third_Guess = input("Guess a third time: ")

            if third_Guess != host_Word:
                print(f"The third letter is: {host_Word[2]}")

                if third_Guess == host_Word:
                    print(f"You got it right! The word was {host_Word}!")
                    break

            fourth_Guess = input("Guess a fourth time: ")

            if fourth_Guess != host_Word:
                print(f"The fourth letter is: {host_Word[3]}")

                if fourth_Guess == host_Word:
                    print(f"You got it right! The word was {host_Word}!")
                    break

            fifth_Guess = input("Guess a fifth time (LAST CHANCE!): ")

            if fifth_Guess != host_Word:
                print(f"The fifth letter is: {host_Word[4]}")
                print(f"You ran out of guesses! The word was {host_Word}! Try again next time!")
                break

            if fifth_Guess == host_Word:
                print(f"You got it right! The word was {host_Word}!")
                break



    if host_Word == guessed_Word:
        print(f"You got it right! The word was {host_Word}!")

    elif host_Word != guessed_Word:
        wrongWord()







def onePlayer():

    with open("1000randomwords.txt") as f:
        words = [word.strip() for word in f if len(word.strip()) >= 5]
        computer = (random.choice(words))

    guess = print(f"This word has", len(computer), "letters. Try to guess: ")

    guessed_Word = input()

    while guessed_Word != computer:
        
        if guessed_Word == computer:
                print(f"You got it right! The word was {computer}!")
                break

        if guessed_Word != computer:
            print(f"The first letter is: {computer[0]}")

            second_Guess = input("Guess a second time: ")

            if second_Guess != computer:
                print(f"The second letter is: {computer[1]}")

            if second_Guess == computer:
                print(f"You got it right! The word was {computer}!")
                break

            third_Guess = input("Guess a third time: ")

            if third_Guess != computer:
                print(f"The third letter is: {computer[2]}")

            if third_Guess == computer:
                print(f"You got it right! The word was {computer}!")
                break

            fourth_Guess = input("Guess a fourth time: ")

            if fourth_Guess != computer:
                print(f"The fourth letter is: {computer[3]}")

            if fourth_Guess == computer:
                print(f"You got it right! The word was {computer}!")
                break

            fifth_Guess = input("Guess a fifth time (LAST CHANCE!): ")

            if fifth_Guess != computer:
                print(f"The fifth letter is: {computer[4]}")
                print(f"You ran out of guesses! The word was {computer}! Try again next time!")
                break

            if fifth_Guess == computer:
                print(f"You got it right! The word was {computer}!")
                break





if one_Or_Two == "2":
    twoPlayer()

elif one_Or_Two == "1":
    onePlayer()










