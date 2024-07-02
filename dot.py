import copy
import pygame
import random

from consts import DOT_RAD, GOAL_P, GOAL_RAD, HEIGHT, MAX_VEL, MUTATE_RATE, PADDING, WIDTH

class Dot:
  def __init__(self) -> None:
    self.brain = Brain(1000)
    self.step = 0
    
    self.dead = False
    self.reachedGoal = False
    
    self.p = pygame.Vector2(20+PADDING,HEIGHT/2)
    self.v = pygame.Vector2(0,0)
    self.a = pygame.Vector2(0,0)

  def update(self) -> None:
    self.move()
    if self.step >= 1000:
      self.dead = True
    if self.p.distance_to(GOAL_P) < GOAL_RAD + DOT_RAD: 
      self.reachedGoal = True
    if not(PADDING < self.p.x < WIDTH-PADDING and PADDING < self.p.y < HEIGHT-PADDING):
      self.dead = True
    

  def move(self) -> None:
    if self.dead or self.reachedGoal:
      return
    self.a = self.brain.instructions[self.step]
    self.step += 1
    self.p += self.v
    self.v += self.a
    if self.v.magnitude() > MAX_VEL: self.v.scale_to_length(MAX_VEL)

  def show(self, screen) -> None:
    pygame.draw.circle(screen, "black", self.p, DOT_RAD)

  def fitness(self):
    if self.reachedGoal:
      return 1/10 + 10000/(self.step ** 2)
    else:
      dist_to_goal = self.p.distance_squared_to(GOAL_P)
      return 1/dist_to_goal

  def clone(self):
    other = Dot()
    other.brain = copy.deepcopy(self.brain)
    return other
    


class Brain:
  def __init__(self, instruct_len) -> None:
    self.instructions = [pygame.Vector2(random.random()-0.5, random.random()-0.5).normalize() for _ in range(instruct_len)]
  
  def mutate(self):
    for i in range(len(self.instructions)):
      if random.random() < MUTATE_RATE:
        self.instructions[i].rotate_ip_rad(2 * random.random() - 1)
    
