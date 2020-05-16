# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:56:45 2020

@author: juanc
"""

import pygame as pg
import numpy as np
import time

# lets create game display
pg.init() 
# game display  settings 
width, height = 1000, 1000 
#screen efective creation
screen = pg.display.set_mode((height, width))
# RGB color of display
bg = 25,25,25 

screen.fill(bg)

#number and size of cels
nxC, nyC = 25, 25
dimCw, dimCh = width/nxC , height/nyC

# Estado de las celdas. Vivas = 1; muertas = 0 
gameState = np.zeros( (nxC, nyC) )

def fill_automat(positions):
    for pos in positions:
        gameState[pos[0],pos[1]] = 1
    

#Automates
stick_pos = [[5,3],[5,4],[5,5]]
movil_automat = [[21,21],[22,22],[22,23],[21,23],[20,23]]

fill_automat(movil_automat)

# execution
keep_going = True
while keep_going:
    # pg.event.pump()
    
    new_game_state = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)
    #evolving screen
    for y in range(0, nxC):
        for x in range(nyC):
            
            n_neigh = gameState[ (x-1) % nxC , (y-1)  % nyC] + \
                      gameState[ ( x ) % nxC , (y-1)  % nyC] + \
                      gameState[ (x+1) % nxC , (y-1)  % nyC] + \
                      gameState[ (x-1) % nxC , ( y )  % nyC] + \
                      gameState[ (x+1) % nxC , ( y )  % nyC] + \
                      gameState[ (x-1) % nxC , (y+1)  % nyC] + \
                      gameState[ ( x ) % nxC , (y+1)  % nyC] + \
                      gameState[ (x+1) % nxC , (y+1)  % nyC]
                      
                      
            ######## RULES 
            # Rule 1: Any live cell with two or three live neighbours 
            # survives.
            if gameState[x, y] == 1 and (n_neigh <2 or n_neigh >3):
                new_game_state[x, y] = 0
            
            
            # Rule 2: Any dead cell with three live neighbours
            # becomes a live cell.
            elif gameState[x, y] == 0 and n_neigh ==3:
                new_game_state[x, y] = 1
                
            
            # Rule 3: All other live cells die in the next generation.
            # Similarly, all other dead cells stay dead.
                
            
            
            
            poly = [(   x   * dimCw,   y   * dimCh ),
                    ( (x+1) * dimCw,   y   * dimCh ),
                    ( (x+1) * dimCw, (y+1) * dimCh ),
                    (   x   * dimCw, (y+1) * dimCh )]
            
            
            # 
            if new_game_state[x, y] == 0:
                pg.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                pg.draw.polygon(screen, (255,255,255), poly, 0)
    
    # Actualize gameState
    gameState = np.copy(new_game_state)            
    pg.display.flip()
            
    

#### THINGS TO DO
# n_neight with for
#
# makes them evolve hehe color change
# 3d implement
# Rules class
# food sourcing
# starting state class
# ramdonize startin positions and define numbers of automats
#
