"""Your program goes in this file."""

from dataclasses import dataclass

import canvas

import pygame

app_size = (600, 600)


@dataclass
class State:
    x: float = 300
    y: float = 300
    on: bool = False


def setup():
    return State()
    

def on_mouse_down(state: State, pos, button):
    x,y = pos
    state.x = x
    state.y = y
    if state.on == False:
        state.on = True
    else:
        state.on = False

def light(screen: pygame.Surface, state):
    canvas.rect(screen, "black", (-25,-125,50,150))
    canvas.circle(screen, "green", (0,0),15)
    canvas.circle(screen, "yellow", (0,-50),15)
    if state.on == False:
        canvas.circle(screen, "grey", (0,-100),15)

    else:
        canvas.circle(screen, "red", (0,-100),15)

def draw(screen: pygame.Surface, state: State):
    screen.fill("white")
    canvas.push_transform(state.x, state.y)
    light(screen,state)
    canvas.pop_transform()