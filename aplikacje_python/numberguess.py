from restricted_input import r_input
from random import randrange

def guess_number():

    # Menu 

    def menu():
        while True:
            print('Welcome to `GUESS THE NUMBER`')
            print('''
        (1) Play
        (2) Exit
            ''')
            choice = r_input('What you want to do 1/2: ', 'nothing', '12', maxlength=1)
            if choice == '1':
                play()
                break
            elif choice == '2':
                print("Goodbye!")
                break

    # Gry

    def easy():
        random_number = randrange(0, 9)
        attempts = 0
        while True:
            guess = int(r_input('Choose the number from 0-9:', 'integer', maxlength=1))
            attempts += 1
            if guess < random_number:
                print('Try Higher!!!')
            elif guess > random_number:
                print('Try Lower!!!')
            else:
                print(f'Congratulations you have won in {attempts} attempts.')
                print('''
                (1) Play Again
                (2) Exit Game
                ''')
                choice = r_input('Choose option 1/2: ', 'nothing', '12', maxlength=1)
                if choice == '1':
                    play()
                    break
                elif choice == '2':
                    return



    def medium():
        random_number = randrange(0, 99)
        attempts = 0
        while True:
            guess = int(r_input('Choose the number from 0-99:', 'integer', maxlength=2))
            attempts += 1
            if guess < random_number:
                print('Try Higher!!!')
            elif guess > random_number:
                print('Try Lower!!!')
            else:
                print(f'Congratulations you have won in {attempts} attempts.')
                print('''
                (1) Play Again
                (2) Exit Game
                ''')
                choice = r_input('Choose option 1/2: ', 'nothing', '12', maxlength=1)
                if choice == '1':
                    play()
                    break
                elif choice == '2':
                    return

    def hard():
        random_number = randrange(0, 999)
        attempts = 0
        while True:
            guess = int(r_input('Choose the number from 0-999:', 'integer', maxlength=3))
            attempts += 1
            if guess < random_number:
                print('Try Higher!!!')
            elif guess > random_number:
                print('Try Lower!!!')
            else:
                print(f'Congratulations you have won in {attempts} attempts.')
                print('''
                (1) PLay Again
                (2) Exit Game
                ''')
                choice = r_input('Choose option 1/2: ', 'nothing', '12', maxlength=1)
                if choice == '1':
                    play()
                    break
                elif choice == '2':
                    return

    def holy():
        random_number = randrange(0, 9999)
        attempts = 0
        while True:
            guess = int(r_input('Choose the number from 0-9999:', 'integer', maxlength=4))
            attempts += 1
            if guess < random_number:
                print('Try Higher!!!')
            elif guess > random_number:
                print('Try Lower!!!')
            else:
                print(f'Congratulations you have won in {attempts} attempts.')
                print('''
                (1) Play Again
                (2) Exit Game
                ''')
                choice = r_input('Choose option 1/2: ', 'nothing', '12', maxlength=1)
                if choice == '1':
                    menu()
                    break
                elif choice == '2':
                    return

    # Wybór Gry

    def play():
        while True:
            print('''
        (1) Easy
        (2) Medium
        (3) Hard
        (4) HOLY MOLY!!!
              
        (5) Exit To Menu
            ''')
    
            choice = r_input('Choose level 1/2/3/4 or quit 5: ', 'nothing', '12345', maxlength=1)

            if choice == '1':
                easy()
                break
            elif choice == '2':
                medium()
                break
            elif choice == '3':
                hard()
                break
            elif choice == '4':
                holy()
                break
            elif choice == '5':
                menu()
                break

    menu()

guess_number()



