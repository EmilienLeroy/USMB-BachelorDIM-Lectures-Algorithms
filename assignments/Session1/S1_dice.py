# -*- coding: utf-8 -*-
"""
@author : Emilien Leroy, LP DIM
@brief : a dice game against the computer
"""
#Random processing lib
from random import *

#Dice Game
def dice_game():
    
    #init variable
    user = 0;
    PC = 0;
    dice = randint(1,6); 
    endgame = False;
    turn = 1
    input_user = "";
    
    #Start of the Game
    while (user <= 100) and (PC <= 100) and (endgame !=True):
        #Indicated the number of turn
        print "Turn number:",turn
        
        #roll the dice
        dice = randint(1,6); 
        
        #User play
        while dice != 1 and (endgame !=True):
            #Write the current score
            print "Score USER:",user,"Score PC:",PC;
            
            #if the user has a score better than 100
            if user > 100:
                #the game is finish
                endgame=True;
            #else
            else:
                #the user can roll the dice or not
                input_user = raw_input("Do you want roll the dice? (y)")
                if input_user == "y":
                    #score up
                    user = user + dice;
                    dice = randint(1,6);
                else:
                    #PC turn
                    dice = 1;
        #roll the dice
        dice = randint(1,6);    
        
        #PC play
        while (dice != 1) and (endgame !=True):
            #Write the current score
            print "Score USER:",user,"Score PC",PC;
            #if the PC has a score better than 100
            if PC > 100:
                #the game is finish
                endgame=1;
            else:        
                #score up
                PC = PC + dice;
                dice = randint(1,6);
        #New turn
        turn = turn + 1;
    #Check the result of the game
    #if the user win
    if user > 100:
        print "USER is the winner with",user,"and PC",PC
    #if the PC win
    if PC > 100:
        print "PC is the winner with",PC,"and USER",user

#launch the game
dice_game();


