import random

max_number = 100


def game_title():
    print('-------------------------------------')
    print('WELCOME TO TURING NUMBER GUESSING GAME!')
    print('-------------------------------------')


def meeting_player():
    player_name = input('Please enter your name: ')
    print(f"Hello {player_name}, let's go")
    print('-------------------------------------')


def guessing_game():
    number = random.randint(0, max_number)
    print('Guess the number from 0 to ' + str(max_number))

    count = 1
    while True:
        try:
            guess = int(input('Your guess: '))
        except ValueError:
            print('Please enter a number')
        if guess < number:
            print('Too low.')

        elif guess > number:
            print('Too high.')

        else:
            print('Just right!!! You have guessed it in ' +
                  str(count) + ' tries. ')
            break
        count += 1


def main():
    game_title()
    meeting_player()
    again = 'y'
    while again.lower() == 'y':
        guessing_game()
        again = input('Would you like to play again? (y/n): ')
        print()
    print('Bye!')


if __name__ == '__main__':
    main()
