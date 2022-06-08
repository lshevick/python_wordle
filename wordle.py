# create wordle in python
# need to have a FIVE letter word that is displayed with blanks
# users have six guesses, must display each guess to show how many already guessed and how many remain
# the users guess must be a valid word in list
# when user makes a guess, it will update one of the blank guesses with their word
# must show user what letters are in the word with yellow, and if they are not in word, grey
# if the letter is in the word and also in the correct spot in the word, it will be green

#global variables

guesses = 0
word = 'plays'
mystery = list(word)
game_table = []
guessed_words = []
blanks = []

def green_letter(l):
    return f'\033[1;30;42m {l} '

def yellow_letter(l):
    return f'\033[1;30;43m {l} '

def grey_letter(l):
    return f'\033[1;30;47m {l} '


def set_game_table(mystery):
    global guesses, game_table, blanks
    for l in range(len(mystery)):
        blanks += ' _ '
    for i in range(6):
        game_table.append(''.join(blanks)) 
        # print(game_table[i])

    return game_table

def display_game():
    global game_table
    for i in range(len(game_table)):
        print(game_table[i])

def check_guess(mystery, guess):
    global guessed_words
    submission = []

    for i, l in enumerate(guess):
        if guess[i] == mystery[i]:
            submission += green_letter(l)
        elif l in mystery:
            submission += yellow_letter(l)
        else:
            submission += grey_letter(l)
    submission_string = ''.join(submission) 
    guessed_words.append(submission_string)
    return guessed_words


def update_table(guessed_words):
    global game_table

    for n, i in enumerate(game_table):
        if n == guesses:
            game_table[n] = guessed_words[n]
        else:
            continue

    return game_table

def play_game():
    global game_table, guessed_words, mystery, submission, guesses
    set_game_table(mystery)

    while guesses < 6:
        display_game()

        guess = input('Try to guess the 5 letter word: ')
        
        if len(guess) != 5 or any(char.isdigit() for char in guess) == True:
            print('You need to guess a FIVE letter WORD')
            continue
        else:
            check_guess(mystery, guess)
            update_table(guessed_words)
            guesses += 1



play_game()  

# display_game(mystery)
# # check_guess(mystery, 'glass')
# print(game_table[0])

# print(check_guess(mystery, 'glass'))