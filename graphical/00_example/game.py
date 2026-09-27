"""Your program goes in this file."""

from dataclasses import dataclass

import pygame

app_size = (640, 480)

STEP = 30
RADIUS = 20


@dataclass
class State:
    x: float = 320


def setup():
    return State()


def on_key_down(state: State, key):
    if key == pygame.K_LEFT:
        state.x -= STEP
    if key == pygame.K_RIGHT:
        state.x += STEP


def draw(screen: pygame.Surface, state: State):
    screen.fill(("black"))
    pygame.draw.circle(screen, ("pink"), (state.x, 240), RADIUS)
