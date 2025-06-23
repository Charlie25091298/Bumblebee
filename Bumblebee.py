import pgzrun
import random

HEIGHT = 600
WIDTH = 600
TITLE = "Bumblebee"


bee = Actor("bee", (50,50))
flower = Actor("flower", (200,200))

def draw() :
   screen.blit("background", (0,0))
   bee.draw()
   flower.draw()


def update() :
    if flower.colliderect(bee) :
       x = random.randint(0,600)
       y = random.randint(0,600)
       flower.pos = (x,y)
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


pgzrun.go()    
