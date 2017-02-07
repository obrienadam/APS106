def is_palindrome(word):
    return word[::-1] == word

if __name__ == '__main__':
    word = input('Enter a word: ')

    if is_palindrome(word):
        print('The word "{}" is a palindrome!'.format(word))
    else:
        print('The word "{}" is not a palindrome.'.format(word))