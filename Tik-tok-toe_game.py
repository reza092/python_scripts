#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:12:18 2020

@author: rezaulkarim
"""

# INTRO
def intro():
    print ("*** Welcome to Tik-Tak-Toe game! ***")

# GAME BOARD DISPLAY    
pos_list = ['---',
             '  |', '  |', '   ',
             '  |', '  |', '   ',
             '  |', '  |', '   ']

def display():
    print(pos_list[1]+pos_list[2]+pos_list[3])
    print(pos_list[0]+pos_list[0]+pos_list[0])
    print(pos_list[4]+pos_list[5]+pos_list[6])
    print(pos_list[0]+pos_list[0]+pos_list[0])
    print(pos_list[7]+pos_list[8]+pos_list[9])
    
#display()

# POSITION instruction
def instruction():
    pos_list_instr = ['---',
             '1 |', '2 |', '3  ',
             '4 |', '5 |', '6  ',
             '7 |', '8 |', '9  ']

    print("\n> Following are the positions on the Gameboard\n")
    print(pos_list_instr[1]+pos_list_instr[2]+pos_list_instr[3])
    print(pos_list_instr[0]+pos_list_instr[0]+pos_list_instr[0])
    print(pos_list_instr[4]+pos_list_instr[5]+pos_list_instr[6])
    print(pos_list_instr[0]+pos_list_instr[0]+pos_list_instr[0])
    print(pos_list_instr[7]+pos_list_instr[8]+pos_list_instr[9])
#instruction()

# Game play or continue?
def gameon_choice(game_on):
    game_choice = 'wrong'
    global player
    
    while game_choice not in ['Y','N']:
        game_choice = input("Do you want to play?\nSelect Y or N : ")
        
        if game_choice not in ['Y','N']:
            print("Sorry, not a valid choice! Please select Y or N")
            
        elif game_choice == 'N':
            game_on = False
            print("Exiting")
            break
        else:
            game_on = True
            print("\nPlayer 'X' will have mark 'x' and the player 'Y' will have mark 'o'")
            if count == 0:
                player = input("Do you want to be player X or Y? : ")
            
    return game_on
#gameon_choice()
    
#Players' playing positionn on the gameboard
def position_choice():
    choice = 'Wrong'
    acceptable_range = range(1,10)
    within_range = False
    
    # DIGIT OR WITHIN RANGE == FALSE
    while choice.isdigit() == False or within_range == False:
        
        print(f'\nPlayer {player}, ')
        choice = input("Please enter your position (1-9) on the gameboard: ")
        
        if choice.isdigit() == False:
            print("That is not a valid position on the gameboard!")
        
        elif choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print("Out of acceptable range!")
        
    return int(choice)
    
#position_choice()

# Updating the gameboard with players' position
def replacement_choice(player,position):
    if player =='X':
        if position in [1,2,4,5,7,8]:
            pos_list[position] = 'x |'
        else:
            pos_list[position] = 'x '
            
    else:
        if position in [1,2,4,5,7,8]:
            pos_list[position] = 'o |'
        else:
            pos_list[position] = 'o '
        
    print (f'Here is the gameboard after player {player}\n')
    return (display())
#replacement_choice(player, position)

# Game over
def game_over(game_on):
    #global game_on
    if ('xxx' or 'ooo') in [(pos_list[1][0] + pos_list[2][0] + pos_list[3][0]),
                            (pos_list[1][0] + pos_list[5][0] + pos_list[9][0]),
                            (pos_list[1][0] + pos_list[4][0] + pos_list[7][0]),
                            (pos_list[2][0] + pos_list[5][0] + pos_list[8][0]),
                            (pos_list[3][0] + pos_list[6][0] + pos_list[9][0]),
                            (pos_list[3][0] + pos_list[5][0] + pos_list[7][0])]:
        print(f'\nHOORAY, GAME OVER! \nPlayer {player} won the game!\n')
        game_on = False
    
    return game_on

# Continue playing
def keep_playing(game_on):
    playing = 'wrong'
    
    while playing not in ['Y', 'N']:
        playing = input("Keep playing? Y or N : ")
        
        if playing not in ['Y', 'N']:
            print ("That is not a valid play choice! Please select Y or N")
            
        elif playing == 'N':
            game_on = False
            print('Exiting')
            break
        
        else:
            game_on = True
            print('Continuing the game\n')
            
    return game_on

# Players turn change
def player_change(player):
    
    if player=='X':
        player = 'Y'
    else:
        player = 'X'
    
    return player
        
## Game scheme
game_on = True
count = 0

introduction = intro()
gameboard = display()
direction = instruction()
game_on = gameon_choice(game_on)
    
while game_on == True and count < 9:
    
    position = position_choice()
    current_gameboard = replacement_choice(player, position)
    game_on = game_over(game_on)
    game_on = keep_playing(game_on)
    player = player_change(player)
    
    count += 1
     
if game_on == True and count == 9:
    print("You both are amazing! It's a tie!")
    