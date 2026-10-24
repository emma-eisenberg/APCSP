"""Makes a crosshair wherever you click"""

from dataclasses import dataclass

import pygame

app_size = (600,600)


@dataclass
class State:
    x: float = 300  
    # x is the x coordinate of the mouse when it is clicked
    y: float = 300
    # y is the y coordinate of the mouse when it is clicked
    


def setup():
    return State()


def on_mouse_down(state: State, pos, button):
    x,y = pos
    state.x = x
    state.y = y

def draw(screen: pygame.Surface, state: State):
    screen.fill ("white")
    pygame.draw.circle(screen,("pink"),(state.x,state.y),26, 1)
    pygame.draw.line(screen,("black"),(state.x-36,state.y),(state.x+36,state.y), 1)
    pygame.draw.line(screen,("black"),(state.x,state.y-36),(state.x,state.y+36), 1)

    

