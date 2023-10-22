from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,speed,x,y,images):
        super().__init__()
        self.image = transform.scale(image.load(images),(50,50))
        self.speed = speed
        self.timer = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    

class Player(GameSprite):
    def __init__(self,speed,x,y,images):
        super().__init__(speed,x,y,images)
        self.health = 3
        self.image = transform.scale(image.load(images),(15,300))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.passedship = 0
        self.a = 5

    def blit(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def walk(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y <375:
            self.rect.y+=self.speed
        if keys[K_w] and self.rect.y > -75:
            self.rect.y-=self.speed
            
class Player2(GameSprite):
    def __init__(self,speed,x,y,images):
        super().__init__(speed,x,y,images)
        self.health = 3
        self.image = transform.scale(image.load(images),(15,125))
        self.passedship = 0
        self.a = 5

    def blit(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def walk(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y <375:
            self.rect.y+=self.speed
        if keys[K_UP] and self.rect.y > -75:
            self.rect.y-=self.speed

class Ball(sprite.Sprite):
    def __init__(self,xspeed,yspeed,x,y,images):
        super().__init__()
        self.image = transform.scale(image.load(images),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.images = images
        self.xspeed = xspeed
        self.yspeed = yspeed
    def blit(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def otskok(self):
        self.rect.x += self.xspeed      
        self.rect.y += self.yspeed
        if self.rect.y>=450:
            self.yspeed=-5
        if self.rect.y<=0:
            self.yspeed=5
            self.xspeed=-5
        if sprite.spritecollide(ball,players,False):
            self.xspeed*=-1   
FPS = 60                
clock = time.Clock()
okno = display.set_mode((700,500))
display.set_caption('Ping Pong')
player_1 = Player(5,0,200,'Player.png')
player_2 = Player2(5,683,200,'Player2.png')
players = sprite.Group()
players.add(player_1)
players.add(player_2)
ball = Ball(5,5,100,100,'Ball.png')
background = transform.scale(image.load("background.png"),(700,500))
game = True
finish = False
font.init()

lose = font.Font(None,50).render('Проиграл!', True,(255,0,0))
restart = font.Font(None,50).render('Press R to Restart', True,(255,0,0))
while game:
    keys = key.get_pressed()
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish == True: 
        if keys[K_r]:
            player_2.rect.x=683
            player_2.rect.y=200
            player_1.rect.x=0
            player_1.rect.y=200
            ball.rect.x=100
            ball.rect.y=100
            finish = False
    if finish != True:
        okno.blit(background,(0,0))
        
        player_1.blit()
        player_1.walk()
        
        player_2.blit()
        player_2.walk()
        
        ball.blit()
        ball.otskok()
        if ball.rect.x>=650:
            okno.blit(lose,(350,200))
            okno.blit(restart,(350,300))
            finish = True
        if ball.rect.x<=0:
            okno.blit(lose,(350,200))
            okno.blit(restart,(350,300))
            finish = True
        

    clock.tick(FPS)

    display.update()