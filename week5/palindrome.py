def is_palindrome(word):
    return word[::-1] == word

if __name__ == '__main__':
    word = input('Enter a word: ')

    if is_palindrome(word):
        print('The word "{}" is a palindrome!'.format(word))
    else:
        print('The word "{}" is not a palindrome.'.format(word))




phrase = input('What would you like to say?: ').lower()

if phrase == 'hello':
    print('Hello to you too!')
elif phrase == 'goodbye':
    print('Goodbye!')
elif phrase == 'how are you doing today?':
    print('Fine, thank you!')
else:
    print('I did not understand that phrase.')

from random import randint

num = randint(1, 10)
guess = int(input('Guess a number between 1 and 10: '))

if 1 <= guess <= 10:
    if guess == num:
        print('Good guess!')
    else:
        print('Terrible guess. The number was {}'.format(num))
else:
    print(num, 'is not between 1 and 10...')

from random import randint

num = randint(1, 10)
guess = int(input('Guess a number between 1 and 10: '))

if not 1 <= guess <= 10:
    print(num, 'is not between 1 and 10...')
else:
    if guess == num:
        print('Good guess!')
    else:
        print('Terrible guess. The number was {}'.format(num))