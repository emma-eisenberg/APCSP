"""A face named Oren"""

from dataclasses import dataclass

import pygame

app_size = (600,600)


@dataclass
class State:
    pass


def setup():
    return State()

def draw(screen: pygame.Surface, state: State):
    screen.fill(("white"))
    pygame.draw.circle(screen,("black"),(300,300), 100, 1)
    pygame.draw.circle(screen,("black"),(255,270), 17, 1)
    pygame.draw.circle(screen,("black"),(345,270), 17, 1)
    pygame.draw.line(screen,("black"),(300,290),(328,330), 1)
    pygame.draw.line(screen,("black"),(300,330),(328,330), 1)
    pygame.draw.line(screen,("black"),(241,355),(360,355), 1)
    pygame.draw.arc(screen,("red"),(50,50,70,50),3,4,1)
