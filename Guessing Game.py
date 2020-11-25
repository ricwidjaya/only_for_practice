# Create a number guessing game which runs on terminal.
# Player can input a range of numbers to start the game,
# if player couldn't guess it right then he'll keep guessing until he gets right.
# Once he hits the right answer, system will congrats him.

import sys
from random import randint

# Input 2 numbers to start the game.

while True:
    try:
        sys.argv[1] = int(input('Please input the first number.'))

    except:
        print('Please input a number.')
        continue

    else:
        while True:
            try:
                sys.argv[2] = int(input('Please input the second number.'))
                while sys.argv[2] > sys.argv[1]:
                    print('Let\' do this shit.')
                    break
                else:
                    print(f'Please input a number bigger than {sys.argv[1]}')
                    continue
            except:
                print('Please input a number.')
                continue
            break
    break

# Received the parameter I want.
# Create the answer from player's range.

answer = randint(sys.argv[1], sys.argv[2])

while True:
    try:
        guess = int(input('Guessing Time! Goodluck!'))
        if sys.argv[2] > guess > sys.argv[1]:
            if guess == answer:
                print('You are badass.')
                break
            else:
                print('Keep guessing!')
                continue
        else:
            print('Don\'t forget the range you just set.')

    except:
        print('C\'mon it\'s obviously a number.')

