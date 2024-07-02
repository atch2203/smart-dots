import pygame

from consts import GOAL_P, GOAL_RAD


class Goal:
  def __init__(self) -> None:
    self.p = GOAL_P

  def show(self, screen):
    pygame.draw.circle(screen, "green", self.p, GOAL_RAD)