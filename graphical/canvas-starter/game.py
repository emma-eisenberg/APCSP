"""Describe your program here."""

from dataclasses import dataclass

import canvas
import pygame

app_size = (600, 600)


@dataclass
class State:
    pass


def setup():
    return State()


def draw(screen: pygame.Surface, state: State):
    screen.fill("white")
