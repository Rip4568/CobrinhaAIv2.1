import pygame
from pygame.locals import *
import random
pygame.init()

def grid():
    x = random.randint(10,590)
    y = random.randint(10,590)
    return (x//10 * 10, y//10 * 10)

def distancia(ponto1,ponto2):
    x1 = ponto1[0][0]
    y1 = ponto1[0][1]
    x2 = ponto2[0]
    y2 = ponto2[1]
    distancia_dos_pontos = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distancia_dos_pontos

def colision(cx,cy,cx2,cy2):
    return (cx == cx2) and (cy == cy2)

def buscador_de_macas(snake,snake_x,snake_y,apple_x,apple_y,apple_posAI,buscar):
    if snake_x > apple_x:
        my_direction = LEFT
        if my_direction == LEFT:
            snake[0] = (snake[0][0]-10, snake[0][1])
            if colision(snake_x,snake_y,apple_x,apple_y):
                colision2(buscar)
    if snake_x < apple_x:
        my_direction = RIGHT
        if my_direction == RIGHT:
            snake[0] = (snake[0][0]+10, snake[0][1])
            if colision(snake_x,snake_y,apple_x,apple_y):
                colision2(buscar)
    if snake_y > apple_y:
        my_direction = UP
        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
            if colision(snake_x,snake_y,apple_x,apple_y):
                colision2(buscar)
    if snake_y < apple_y:
        my_direction = DOWN
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
            if colision(snake_x,snake_y,apple_x,apple_y):
                colision2(buscar)

buscar = None

screen = pygame.display.set_mode((610,610))
pygame.display.set_caption('Cobrinha')

snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

canto_pos = (5,5)
canto = pygame.Surface((600,600))
canto.fill((255,255,255))

#canto verde (centro) OK!!!
canto_pos2 = (7,7)
canto2 = pygame.Surface((595,595))
canto2.fill((25,130,0))

apple_pos = grid()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

apple_pos2 = grid()
apple2 = pygame.Surface((10,10))
apple2.fill((0,255,0))

apple_pos3 = grid()
apple3 = pygame.Surface((10,10))
apple3.fill((0,0,255))

apple_pos4 = grid()
apple4 = pygame.Surface((10,10))
apple4.fill((120,120,0))

UP = 0
RIGHT = 1
DOWN = 2
LEFT =3

my_direction = None

apple_posAI = None
apple_x= None
apple_y = None
snake_x = snake[0][0]
snake_y = snake[0][1]

Dsa = distancia(snake,apple_pos)
Dsa2 = distancia(snake,apple_pos2)
Dsa3 = distancia(snake,apple_pos3)
Dsa4 = distancia(snake,apple_pos4)
lista = (Dsa,Dsa2,Dsa3,Dsa4)
menor = min(lista)

if menor == Dsa:
    apple_x= apple_pos[0]
    apple_y = apple_pos[1]
    apple_posAI = apple_pos
    buscar = 1
elif menor == Dsa2:
    apple_x= apple_pos2[0]
    apple_y = apple_pos2[1]
    apple_posAI = apple_pos2
    buscar = 2
elif menor == Dsa3:
    apple_x= apple_pos3[0]
    apple_y = apple_pos3[1]
    apple_posAI = apple_pos3
    buscar = 3
elif menor == Dsa4:
    apple_x= apple_pos4[0]
    apple_y = apple_pos4[1]
    apple_posAI = apple_pos4
    buscar = 4

clock = pygame.time.Clock()

while True:
    clock.tick(3)
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()

    if buscar == 1:
        buscador_de_macas(snake,snake_x,snake_y,apple_x,apple_y,apple_posAI,buscar)
        if colision(snake_x,snake_y,apple_x,apple_y):
            apple_pos = grid()
            for i in range(0,3):
                snake.append((0,0))
            buscar = 0
    elif buscar == 2:
        buscador_de_macas(snake,snake_x,snake_y,apple_x,apple_y,apple_posAI,buscar)
        if colision(snake_x,snake_y,apple_x,apple_y):
            apple_pos2 = grid()
            for i in range(0,3):
                snake.append((0,0))
            buscar = 0
    elif buscar == 3:
        buscador_de_macas(snake,snake_x,snake_y,apple_x,apple_y,apple_posAI,buscar)
        if colision(snake_x,snake_y,apple_x,apple_y):
            apple_pos3 = grid()
            for i in range(0,3):
                snake.append((0,0))
            buscar = 0
    elif buscar == 4:
        buscador_de_macas(snake,snake_x,snake_y,apple_x,apple_y,apple_posAI,buscar)
        if colision(snake_x,snake_y,apple_x,apple_y):
            apple_pos4 = grid()
            for i in range(0,3):
                snake.append((0,0))
            buscar = 0
    elif buscar == 0:
        Dsa = distancia(snake,apple_pos)
        Dsa2 = distancia(snake,apple_pos2)
        Dsa3 = distancia(snake,apple_pos3)
        Dsa4 = distancia(snake,apple_pos4)
        lista = (Dsa,Dsa2,Dsa3,Dsa4)
        menor = min(lista)
        if menor == Dsa:
            apple_x= apple_pos[0]
            apple_y = apple_pos[1]
            apple_posAI = apple_pos
            buscar = 1
        elif menor == Dsa2:
            apple_x= apple_pos2[0]
            apple_y = apple_pos2[1]
            apple_posAI = apple_pos2
            buscar = 2
        elif menor == Dsa3:
            apple_x= apple_pos3[0]
            apple_y = apple_pos3[1]
            apple_posAI = apple_pos3
            buscar = 3
        elif menor == Dsa4:
            apple_x= apple_pos4[0]
            apple_y = apple_pos4[1]
            apple_posAI = apple_pos4
            buscar = 4

    snake_x = snake[0][0]
    snake_y = snake[0][1]

    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0],snake[i-1][1])

    screen.fill((0,0,0))
    screen.blit(canto,canto_pos)
    screen.blit(canto2,canto_pos2)
    screen.blit(apple,apple_pos)
    screen.blit(apple2,apple_pos2)
    screen.blit(apple3,apple_pos3)
    screen.blit(apple4,apple_pos4)
    for pos in snake :
        screen.blit(snake_skin,pos)

    pygame.display.update()