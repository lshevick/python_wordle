# create wordle in python
# need to have a FIVE letter word that is displayed with blanks
# users have six guesses, must dispaly each guess to show how many already guessed and how many remain
# the users guess must be a valid word in list
# when user makes a guess, it will update one of the blank guesses with their word
# must show user what letters are in the word with yellow, and if they are not in word, grey
# if the letter is in the word and also in the correct spot in the word, it will be green

#global variables

guesses = 6
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


def display_game(mystery):
    global guesses, game_table, guessed_words, blanks
    for l in range(len(mystery)):
        blanks += ' _ '
    for i in range(guesses):
        game_table.append(''.join(blanks)) 
        print(game_table[i])

    return game_table




def check_guess(mystery, guess):
    global game_table, guessed_words

    for i, l in enumerate(guess):
        if guess[i] == mystery[i]:
            guessed_words += green_letter(l)
        elif l in mystery:
            guessed_words += yellow_letter(l)
        else:
            guessed_words += grey_letter(l)
    submission = ''.join(guessed_words)
    return submission

def update_table(submission):
    pass


def play_game(mystery):
    global game_table, guessed_words
    
    display_game(mystery)

    while guesses > 0:
        guess = input('Try to guess the 5 letter word: ')


    

display_game(mystery)
# check_guess(mystery, 'glass')
print(game_table[0])

print(check_guess(mystery, 'glass'))