import random
from  words import  animals
import string


def get_valid_word( animals):
    word = random.choice( animals)  # a word from the list
    while '-' in word or ' ' in word:
        word = random.choice( animals)

    return word.upper()


def hangman():
    print("Adivina un animal en ingles...")
    word = get_valid_word( animals)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    #print(f'"---------"  {alphabet}')
    used_letters = set()  # what the user has guessed
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # letters usadas
        # ' '.join(['a', 'b', 'c']) --> 'a b c'
      
        print('Te quedan', lives, 'vidas y utilizaste estas letras: ', '-'.join(used_letters))

        # current word es (W - R D) 
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')

        print('Current word: ', ' '.join(word_list))# agrego a las letras mostradas (A - C D)

        user_letter = input('Ingresa una letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # resta una vida
                print('\n-->', user_letter, 'no esta en la palabra.')

        elif user_letter in used_letters:
            print('\n Ya la has utilizado. Adivina otra.')

        else:
            print('\nNo es una palabra correcta.')
    if lives == 0:
       
        print('Has perdido, la palabra era', word)
    else:
        print('Perfecto!!! Adivinaste, el animal es ', word, '!!')


if __name__ == '__main__':
    hangman()


