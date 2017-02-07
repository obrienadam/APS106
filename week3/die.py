from random import randint

def roll_die():
    return randint(1, 6)

def display_die(num):
    if num == 1:
        print('   \n * \n   ')
    elif num == 2:
        print('*  \n   \n  *')
    elif num == 3:
        print('*  \n * \n  *')
    elif num == 4:
        print('* *\n   \n* *')
    elif num == 5:
        print('* *\n * \n* *')
    elif num == 6:
        print('* *\n* *\n* *')
    else:
        print('Bad die!')

if __name__ == '__main__':
    display_die(roll_die())