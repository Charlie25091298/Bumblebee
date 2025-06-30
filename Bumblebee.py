import pgzrun
import random

HEIGHT = 400
WIDTH = 600
TITLE = "Bumblebee"


bee = Actor("bee", (50,50))
flower = Actor("flower", (200,200))
score = 0
gameOver = False

def draw() :
   global score
   if gameOver == True :
       screen.fill("red")
       screen.draw.text("GAME OVER!", (200,300), color = "black")
       screen.draw.text("Final score: " + str(score), (200,325), color = "black")
   else :    
       screen.blit("background", (0,0))
       bee.draw()
       flower.draw()
       screen.draw.text("score: " + str(score), (500,50), color = "black")



def update() :
    global score
    if flower.colliderect(bee) :
       x = random.randint(0,400)
       y = random.randint(0,400)
       flower.pos = (x,y)
       score +=1
    if keyboard.left :
        bee.x -= 2
    if keyboard.right :
        bee.x += 2
    if keyboard.up :
        bee.y -= 2       
    if keyboard.down :
        bee.y += 2

def on_key_down(key) :
    if key == keys.W :
        bee.y -= 2    

def timer() :
    global gameOver
    gameOver = True

clock.schedule(timer, 10)
pgzrun.go()    
