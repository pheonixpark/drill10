from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Bigball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(90,600)
        self.image=load_image('ball41x41.png')
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.y -= random.randint(1,5)


class Smallball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(90,600)
        self.image=load_image('ball21x21.png')
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.y -= random.randint(1, 5)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
grass=Grass()
ball1=Bigball()
ball2=Smallball()
bigballs=[Bigball() for i in range (1,10+1)]
smallballs=[Smallball() for i in range (1,10+1)]

droping=True

while droping:
    handle_events()
    for ball1 in bigballs:
        ball1.update()
    for ball2 in smallballs:
        ball2.update()

    clear_canvas()
    grass.draw()
    for ball1 in bigballs:
        ball1.draw()
    for ball2 in smallballs:
        ball2.draw()
    update_canvas()

clear_canvas()




# initialization code

# game main loop code

# finalization code