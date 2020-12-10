import shelve
from cave_initialise import initialize
import random

def main():
    initialize()
    restart = 'YES'
    while True:
        if restart == 'YES':
            game(str(random.randint(1,6)))
        restart = input('Would you like to restart the game?').upper()
        if restart == 'NO':
            break
        elif restart == "YES":
            continue
        else:
            print("Two options: Yes or No! ")

def game(level):
    location = shelve.open('location_menu')
    vocabulary = shelve.open('vocabulary')
    current_location = location.get(level)
    while True:
        print(current_location.get('desc'))
        options = current_location.get('exits')

        user_input = input('At current moment you have following options: {}'.format(list(options.keys()))).upper()

        for items in user_input.split():
            if items in vocabulary.keys():
                user_input = vocabulary[items]

        if user_input == 'Q':
            print(location['0'].get('desc'))
            break

        if user_input in options:
            wanting_location = str(options[user_input])
            current_location = location[wanting_location]
        else:
            print('The options you have chosen is not available. \nPlease choose between {}'.format(list(options.keys())))

    location.close()
    vocabulary.close()


if __name__ == "__main__":
    main()