import random
import time
import mysql.connector as mdb


def play_game():
    option = ['Rock', 'Paper', 'Scissors']
    while True:
        print("To start select below options")
        print('1.Rock\n2.Paper\n3.Scissors')  # Player selection
        player_choice = int(input())
        if player_choice == 1:
            print('you selected : Rock')
            player_choice = 'Rock'
        elif player_choice == 2:
            print('you selected : Paper')
            player_choice = 'Paper'
        elif player_choice == 3:
            print('you selected : Scissors')
            player_choice = 'Scissors'
        else:
            print("Wrong Entry")

        comp_choice = random.choice(option)
        print('Computer selected: ', comp_choice)

        if player_choice == comp_choice:
            print("Tie")

        elif player_choice == 'Rock' and ((comp_choice == 'Paper') or (comp_choice == 'Scissors')) or (
                player_choice == 'Paper' and comp_choice == 'Rock'):
            print("You Win")

        else:
            print('Computer Win')

        replay = input("DO you want to play again?\n(y/n)")

        if replay == 'y' or replay == 'Y':
            continue
        else:
            break


my_DB = mdb.connect(user="root", passwd="Parsh@123", database="my_test")
my_cursor = my_DB.cursor()
user = input("are you a new player").lower()
if user == "yes":
    # two players of of them is computer    player = input("Please enter your name")
    age = int(input("Please enter your age"))
    passwd = input("Enter password")
    #sql = "Insert into player (id, name, age , password) values (%s,%s,%s,%s)"
    #values = (2, player, age, passwd)
    my_cursor.execute("Insert INTO player() Values()")
    my_DB.commit()
    if age >= 18:
        print("you are allowed to play this game")
        play_game()

    else:
        print("you are not fit for game")
    my_cursor.close()
    my_DB.close()
