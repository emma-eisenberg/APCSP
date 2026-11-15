"""an arrow that gets bigger with each click"""

from dataclasses import dataclass

import canvas

import pygame

app_size = (600, 600)


@dataclass
class State:
    arrow_length: float = 45


def setup():
    return State()


def arrow(screen: pygame.Surface,arrow_length: float):
    canvas.line(screen,"purple", (-arrow_length,0),(0,0))
    canvas.line(screen,"purple",(-10,-10),(0,0))
    canvas.line(screen,"purple",(-10,10),(0,0))

def on_mouse_down(state: State, pos, button):
    state.arrow_length = state.arrow_length + 5

def draw(screen: pygame.Surface, state: State):
   screen.fill("white")
   canvas.push_transform(300,300,1)
   arrow(screen, state.arrow_length)
   canvas.pop_transform()

   