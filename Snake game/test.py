import pygame 
import random

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))


#Title and icon
pygame.display.set_caption("Space")
icon = pygame.image.load("C:/Users/anike/Downloads/ufo.png")
pygame.display.set_icon(icon)


back = pygame.image.load('C:/Users/anike/OneDrive/Desktop/race/background-1.png')


#player
playerImg = pygame.image.load("C:/Users/anike/OneDrive/Desktop/pixelART1.JPG")
playerX= 370
playerY= 480
playerX_change = 0


#enemy
enemyImg = pygame.image.load("C:/Users/anike/Downloads/alien.png")
enemyX= random.randint(0,724)
enemyY= random.randint(50,150)
enemyX_change = 0.2
enemyY_change = 40



#bullet
bulletImg = pygame.image.load("C:/Users/anike/Downloads/bullet.png")
bulletX= 0
bulletY= 480
bullet_Xchange = 0
bulletY_change = 1 
bullet_state = "ready"

def player(X,Y):
    screen.blit(playerImg, (X,Y))


def enemy(X,Y):
    screen.blit(enemyImg, (X,Y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+16))

#game loop
running = True
while running:
    
    #RGB
    screen.fill((0, 0, 0))
    screen.blit(back, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.3
            if event.key == pygame.K_SPACE:
                bulletX= playerX
                fire_bullet(bulletX, bulletY)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    enemyX = enemyX + enemyX_change
    #enemyY = enemyY + enemyY_change
    
    

    if playerX <= 0:
        playerX= 0
    elif playerX >= 736:
        playerX = 736

    if enemyX <= 0:
        enemyX_change= 0.2
        enemyY = enemyY + enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY = enemyY + enemyY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    #if(bulletY == enemyY) :
        #enemyX = 100
        #enemyY = 100


    enemy(enemyX, enemyY)
    player(playerX, playerY)

    pygame.display.update()
