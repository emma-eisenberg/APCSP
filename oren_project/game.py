"""an arrow that gets bigger with each click"""

from dataclasses import dataclass

import canvas

import pygame

app_size = (600, 600)

STEP = 20

@dataclass
class State:
    length: float = 200
    color: float = 255
    mouth: bool = False
    dead: bool = False

def setup():
    return State()

def draw(screen:pygame.Surface, state: State):
    screen.fill("white")
# outline
    canvas.circle(screen,("black"),(300,300), 100, 1)
#left eye
    canvas.circle(screen,("black"),(260,270), 17, 1)
#right eye
    canvas.circle(screen,("black"),(340,270), 17, 1)
#nose
    canvas.line(screen,("black"),(300,290),(328,330), 1)
    canvas.line(screen,("black"),(300,330),(328,330), 1)
#mouth
    if state.mouth == True:
        canvas.ellipse(screen, "black", (250, 340, 115, 25))
    else:
        canvas.line(screen,("black"),(241,355),(360,355), 1)
#hair
    canvas.line(screen, "black", (300, 200), (300, state.length),1)
    canvas.line(screen, "black", (250, 213), (250, state.length+13), 1)
    canvas.line(screen, "black", (350, 213), (350, state.length+13), 1)
#cheek
    canvas.circle(screen, (255,state.color,state.color), (245,320), 13)
    canvas.circle(screen, (255,state.color,state.color), (360,320), 13)
    if state.dead == True:
        canvas.line(screen, "red", (425, 400), (190, 200), 10)
        canvas.line(screen, "red", (425, 200), (190, 400), 10)


def on_tick(state: State, dt: float):
    if state.dead == False:
        state.length = state.length - STEP * dt
    

def on_mouse_down(state: State, pos, button):
        if state.color>=5:
            state.color=state.color-25.49
        else:
            state.color=0
            state.dead = True   


def on_mouse_move(state: State, pos):
    x,y=pos
    dx = x - 300
    dy = y - 300
    if state.dead == False:
        if dx*dx + dy*dy <= 100 * 100:
            state.mouth = True
        else:
            state.mouth = False      


         

   