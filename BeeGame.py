import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
score = 0
game_over = False
bee= Actor("bee")
bee.pos =100,100
flower=Actor("flower")
flower.pos=200,200
def draw():
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))
    if game_over:
        screen.fill("yellow")
        screen.draw.text("TIME UP! FINAL SCORE: "+str(score),color="red",fontsize=40,midtop=(WIDTH/2,10))
def place_flower():
    flower.x=randint(70,(WIDTH-70))   
    flower.y=randint(70,(HEIGHT-70)) 
    
def time_up():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.a:
        bee.x= bee.x-2
    if keyboard.d:
        bee.x= bee.x+2
    if keyboard.s:
        bee.y= bee.y+2
    if keyboard.w:
        bee.y= bee.y-2    
    flower_collected=bee.colliderect(flower)
    if flower_collected:
        score= score+10
        place_flower()

clock.schedule(time_up,60.0)
pgzrun.go()