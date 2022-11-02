import random
import os
import csv

#mak list of words
words_list_object = open('words.txt', newline = '')
reader = csv.reader(words_list_object, delimiter=',')
words_list = []
for row in reader:
    words_list.append(row)

print(words_list)
clear_screen = print ("\n" * 100)
#choose random word
word = random.choice(words_list[0])



#set up beginnign of game
clear_screen
print("Welcome to the Hangman Game! \n")


drawing = HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
#7 pictures

lives = 7
print("")
print("You have {lives} lives.".format(lives=lives))
print("")
used_letters = []
#input("\n Enter a letter for you first guess: ")
a = True
word_dash = []
word_dash.append('_ ' * len(word))
word_dash_split = word_dash[0].split(' ')
correct_guesses = 0


while lives > 0 :
    if correct_guesses < len(word):
        print("This is the word: {word}".format(word=word_dash_split[0:-1]))
        print(drawing[-lives])
        player_guess = input("Make a letter guess: ")
        player_guess = player_guess.lower()




        if (len(player_guess) == 1 and player_guess.isalpha() == True):

            if player_guess not in used_letters:
                used_letters.append(player_guess.lower())
                if player_guess in word:
                    letter_pos_in_word = [i for i, letter in enumerate(word) if player_guess == letter]

                    for i in letter_pos_in_word:
                        word_dash_split[i] = player_guess
                    correct_guesses += len(letter_pos_in_word)
                    print("")
                    print("\n"*100)
                    print("Correct!")


                else:
                    print("\n"*100)
                    print("Your guess was WRONG!")
                    lives -= 1

            else:
                print("\n"*100)
                print("You've already guessed that letter!")


        else:
            clear_screen
            print("Your guess is invalid!")
            print("")
            print("")
    else:
        break

if lives == 0:
    print("\n"*100)
    print(drawing[6])
    print("Oh no you ran out of lives!")
    print("The word was",str(word)+".")

elif correct_guesses == len(word):
    print("\n"*100)
    print(drawing[-lives+1])
    print("Congratulations! You guessed the word!")
