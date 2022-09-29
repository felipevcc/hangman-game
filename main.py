from interface import *
from random import choice
from datetime import datetime
import os

# open data file from any path
FILE_PATH=os.path.dirname(__file__)

# interface organization
def interface(size, lives, word, wrong_letter, m):
    view = [dashboard[0], hangman_ascii[lives], word, wrong_letter]
    for i in view:
        print(i, '\n')

    if m != 0:
        print(m, '\n')

# normalize letters
def normalize(sentence):
    new_sentence = sentence.maketrans('ÁÉÍÓÚ', 'AEIOU')
    return sentence.translate(new_sentence)

# hidden word
def word():
    list_words = []
    with open(f"{FILE_PATH}/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            list_words.append(word)
    word = choice(list_words).upper()
    word = normalize(word)
    return word

# time
def time(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        minutes = time_elapsed.total_seconds() / 60
        minutes_format = "{:.2f}".format(minutes)
        print(f'\n~ Duración del Juego: {minutes_format} minutos ~')
    return wrapper
    
@time
def run():
    
    word_letters = [letter for letter in word() if letter != "\n"]
    HIDDEN_WORD = ''.join(word_letters)

    underscores = ["_" for i in range(len(word_letters))]

    letter_index_dict = {}
    for index, letter in enumerate(HIDDEN_WORD):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(index)

    wrong_letter = []
    message = 0
    i = 0
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # INPUT
    while True:
        os.system("clear")
        interface(0, len(wrong_letter), ' '.join(underscores), ' '.join(wrong_letter), message)
        message = 0
        #print(HIDDEN_WORD)
        
        # won
        if "_" not in underscores:
            print(won, '\nThe correct word is:', HIDDEN_WORD)
            break
        
        # you lost
        if len(wrong_letter) == 6:
            print(game_over, '\nThe correct word was:', HIDDEN_WORD)
            break

        input_letter = str(input("Input letter: ")).upper()
        input_letter = normalize(input_letter)

        # letter validation
        if input_letter not in letters:
            message = 'Other letter'
            continue

        if len(list(input_letter)) > 1:
            message = 'You can input only a letter'
            continue
        
        # letters filter
        filt = list(filter(lambda letter: input_letter==letter, letter_index_dict.keys()))
    
        # others validations && process of correct and incorrect letters
        if len(filt) > 0:
            if ''.join(filt) in underscores:
                message = 'Other letter'
            else:
                message = 'Correct'
                for i in letter_index_dict[filt[0]]:
                    underscores[i] = ''.join(filt) 
        else:
            if input_letter in wrong_letter:
                message = 'Other letter'
            else:
                message = 'Incorrect'
                wrong_letter.append(input_letter)
        
if __name__ == '__main__':
    run()


"""import os
import subprocess
from os import system """   
#system('mode con: cols=200 lines=49')

"""os.system('mode con: cols=10 lines=42')
subprocess.Popen(["mode", "con:", "cols=25", "lines=80"])
cmd = 'mode 50,20'
os.system(cmd)"""
