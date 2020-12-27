import random as rnd
import time

A= input("Enter your name to start the game:")
print("Welcome", A)
time.sleep(0.5)
print("You should guess the word by entering letters one by one.")

Words = ["engineer", "doctor", "teacher", "student", "policeman", "lawyer", "nurse", "dentist", "veterinary", "gardener"]
Word = rnd.choice(Words)
GuessNum = 5
Letters=[]
Word_len = len(Word)
Word_list = list('_' * Word_len)
print(' '.join(Word_list), end='\n')

while GuessNum > 0:
    x = input("Enter a letter: ")
    
    if x in Letters:
        print("Please try another letter which is different from previous.")
        continue

    elif len(x) > 1:
        print("Please enter only one number.")
        continue

    elif x not in Word:   
        GuessNum -= 1
        print("Wrong answer!. You have {} guesses".format(GuessNum))

    else:
        for i in range(len(Word)):
            if x == Word[i]:
                print("Great!")
                Word_list[i] = x
                Letters.append(x)
        print(' '.join(Word_list), end='\n')

    Answer = input("Do you want to guess whole word? ['y' or 'n'] : ")

    if Answer == "y":
        Guess = input("You can guess the whole word : ")
        if Guess == Word:
            print("Congratulations, you won!")
            break
        else:
            GuessNum -= 1
            print("Wrong answer. You have {} guesses.".format(tahminSayisi))


    if GuessNum == 0:
        print("Game Over.")
        break