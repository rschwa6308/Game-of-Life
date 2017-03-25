#requires pygame module
from time import sleep
from math import floor
from random import randint
import pygame, os, sys
from pygame.locals import *
from pygame import *
pygame.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"

black = (0,0,0)
white = (255,255,255)

font = pygame.font.SysFont("monospace",20)





fps = 15

gens = 1000

global board
board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
         [0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


#fill board with empty cells
def create_empty_board():
    global board
    board = []
    for y in range(80):
        z = []
        for x in range(120):
            z.append(0)
        board.append(z)

#create_empty_board()


pixel_size = 8


#set up display
display_width = len(board[0])*pixel_size-pixel_size
display_height = len(board)*pixel_size-pixel_size
screen = pygame.display.set_mode((display_width,display_height))

pygame.draw.line(screen,black,(10,10),(10,200),3)



#input board function
def input_board():
    display(board)
    done = False
    write = False
    kill = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    write = True
                elif event.button == 3:
                    kill = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    write = False
                elif event.button == 3:
                    kill = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    done = True
        if write:
            board[int(floor(event.pos[1]/pixel_size))][int(floor(event.pos[0]/pixel_size))] = 1
        if kill:
            board[int(floor(event.pos[1]/pixel_size))][int(floor(event.pos[0]/pixel_size))] = 0
        display(board)


def display(array):
    for y in range(0,len(array)-1):
        for x in range(0,len(array[y])-1):
            if array[y][x] == 0:
                pygame.draw.rect(screen,white,(x*pixel_size,y*pixel_size,pixel_size,pixel_size),0)
            elif array[y][x] == 1:
                pygame.draw.rect(screen,black,(x*pixel_size,y*pixel_size,pixel_size,pixel_size),0)
    #draw grid
    for x in range(len(board[0])):
        pygame.draw.line(screen,black,(x*pixel_size,0),(x*pixel_size,display_height),1)
    for y in range(len(board)):
        pygame.draw.line(screen,black,(0,y*pixel_size),(display_width,y*pixel_size),1)
    pygame.display.update()


def updateCell(array,row,column):
    sum = 0
    #up left
    if row != 0 and column != 0:
        sum += int(array[row-1][column-1])
    #up
    if row != 0:
        sum += int(array[row-1][column])
    #up right
    if row != 0 and column != len(array[row])-1:
        sum += int(array[row-1][column+1])
    #right
    if column != len(array[row])-1:
        sum += int(array[row][column+1])
    #down right
    if row != len(array)-1 and column != len(array[row])-1:
        sum += int(array[row+1][column+1])
    #down
    if row != len(array)-1:
        sum += int(array[row+1][column])
    #down left
    if row != len(array)-1 and column != 0:
        sum += int(array[row+1][column-1])
    #left
    if column != 0:
        sum += int(array[row][column-1])
    return sum



def nextGen(array):
    newBoard = []
    for y in range(len(array)):
        newBoard.append([0 for i in range(len(array[0]))])
    
    for y in range(len(array)):
        for x in range (len(array[y])):
            z = updateCell(array,y,x)
            #die
            if array[y][x] == 1 and (z < 2 or z > 3):
                newBoard[y][x] = 0
            #live
            elif array[y][x] == 1 and (z == 2 or z == 3):
                newBoard[y][x] = 1
            #born
            elif array[y][x] == 0 and z == 3:
                newBoard[y][x] = 1
    board = newBoard
    return board
    

input_board()

display(board)

done = False
clock = pygame.time.Clock()
for gen in range(gens+1):
    clock.tick(fps)
    pygame.display.set_caption("gen: " + str(gen) + "/" + str(gens))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                while not done:
                    event = pygame.event.wait()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            done = True
                done = False
    
    board = nextGen(board)
    display(board)


sleep(1)
pygame.quit()
quit()

