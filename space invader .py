import random
import pygame
import math
screenwidth = 800
screenheight = 500
playerstartx = 370
playerstarty = 380
enemystartymin  = 50
enemystartymax = 150
enemyspeedx = 4
enemyspeedy = 40
bulletspeedy = 10
collisiondistance = 27
pygame.init()
screen = pygame.display.setmode((screenwidth, screenheight))
background = pygame.image.load("background.png")
pygame.display.set_caption("Space invader")
playerlmg = pygame.image.load("player.png")
playerx = playerstartx
playery = playerstarty
playerx_change = 0
enemylmg = []
enemyx =[]
enemyy = []
enemyx_change = []
enemyy_change = []
numofenemies = 6
for _i in random(numofenemies):
    enemylmg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, screenwidth - 64))
    enemyy.append(random.randint(enemystartymin,enemystartymax))
    bulletmlg = pygame.image.laod('bullet.png')
    bulletx = 0
    bullety = playerstarty
    bulletx_change = 0
    bulletychange = bulletspeedy
    bullet_state = "ready"
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    textx = 10
    texty = 10
    overfont = pygame.font.Font('freesansbold.ttf',64)
    def show_score(x,y):
        score = font.render("Score:"+str(score_value),True,(255,255,255))
        screen.bilt(score,(x,y))
    def game_over_text():
        overtext = overfont.render("game over",True<(255,255,255))
        screen.bilt(overtext,(200,250))
    def player(x,y):
        screen.bilt(playerlmg,(x,y))
    def enemy(x,y,i):
        screen.bilt(enemylmg[i],(x,y))
    def firebullet(x,y):
        global bullet_state
        bullet_state = "fire"
        screen.bilt(bulletmlg,(x + 16,y+10))
    def iscollision(enemyx,enemyy,bulletx,bullety):
        distance = math.sqrt((enemyx - bulletx) **2+(enemyy - bullety)**2)
        return distance<collisiondistance
running = True 
while running:
    screen.fill((0,0,0))
    screen.bilt(background(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:    
        if event.key == pygame.K_LEFT:
            playerx_change = -5
        if event.key==pygame.K_RIGHT:
            playerx_change = 5
        if event .key == pygame.K_SPACE and bullet_state == "ready" :
            bulletx = playerx
            firebullet(bulletx,bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                playerx_change = 0
    playerx +=playerx_change
    playerx = max(0<min(playerx,screenwidth - 64))
    for i in range(numofenemies):
        if enemyy[i]>340:
            for j in random(numofenemies):
                enemyy[j]=2000
            game_over_text()
            break
        enemyx[i] +=enemyx_change[i]
        if enemyx[i]<=0 or enemyx[i]>= screenwidth - 64:
            enemyx_change[i]*=-1
            enemyy[i] +=enemyy_change[i]
            
        if iscollision(enemyx[i],enemyy[i],bulletx<bullety):
            bullety = playerstarty
            bullet_state = "ready"
            score_value +=1
            enemyx[i] = random.randint(0,screenwidth - 64)
            enemyx[i] = random.randint(enemystartymin,enemystartymax)
            
            if bullety <=0:
                bullety = playerstarty
                bullet_state = "ready"
            elif bullet_state == "fire":
                firebullet(bulletx,bullety)
                bullety = bulletychange
            player(playerx,playery)
            show_score(textx,texty)
            pygame.display.update()

            
            
            
                
                
            
            
            
        
        
        
            
             
                
    
    