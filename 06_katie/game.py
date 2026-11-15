"""an arrow that gets bigger with each click"""

from dataclasses import dataclass

import canvas

import pygame

app_size = (600, 600)

STEP = 15

@dataclass
class State:
    katie: float = 300
    smile: bool = True


def setup():
    return State()


def draw(screen:pygame.Surface, state:State):
    screen.fill ("white")
    canvas.push_transform (state.katie,300)
    katie(screen,state.smile)
    canvas.pop_transform()

#copied from hw sheet
def katie(screen: pygame.Surface, smiling):
    
# face
    canvas.circle(screen, "black", (0, 0), 50, 1)

# ears
    canvas.line(screen, "black", (-24, -44), (-19, -60))
    canvas.line(screen, "black", (-19, -60), (-14, -47))
    canvas.line(screen, "black", (24, -44), (19, -60))
    canvas.line(screen, "black", (19, -60), (14, -47))

# eyes
    canvas.circle(screen, "black", (-16, -16), 10, 1)

    canvas.circle(screen, "black", (16, -16), 10, 1)

# pupils
    canvas.ellipse(screen, "black", (-19, -23, 6, 14))
    canvas.ellipse(screen, "black", (13, -23, 6, 14))

# nose and nostrils
    canvas.circle(screen, "black", (0, 0), 5, 1)
    canvas.circle(screen, "black", (-3, 0), 1)
    canvas.circle(screen, "black", (3, 0), 1)

# whiskers
    canvas.line(screen, "black", (-20, 0), (-3, 7))
    canvas.line(screen, "black", (-20, 14), (-3, 9))
    canvas.line(screen, "black", (20, 0), (3, 7))
    canvas.line(screen, "black", (20, 14), (3, 9))

# mouth (a frown)
    if smiling == False:
        canvas.line(screen, "black", (-8, 28), (0, 20))
        canvas.line(screen, "black", (0, 20), (8, 28))
    else:
        canvas.line(screen, "black", (-8,10),(0,20))
        canvas.line(screen, "black", (0,20), (8,10))

def on_mouse_down(state: State, pos, button):
    x,y = pos 
    if x > state.katie:
        state.katie = state.katie+STEP
        state.smile = True
    else:
        state.katie = state.katie-STEP
        state.smile = False

    
    
        
    


         

   