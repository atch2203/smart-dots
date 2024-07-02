from ast import get_docstring
import random
from dot import Dot


class Population:
  def __init__(self, size) -> None:
    self.size = size
    self.gen = 0
    self.dots = [Dot() for _ in range(size)]

  def update(self):
    for d in self.dots: d.update()

  def show(self, screen):
    for d in self.dots: d.show(screen)
  
  def done(self):
    return any([d.reachedGoal for d in self.dots]) or all([d.dead or d.reachedGoal for d in self.dots])
  
  def selection(self):
    self.calc_fitness_sum()
    self.dots = [self.get_dot_fitness_weighted() for _ in range(self.size)]
    self.gen += 1


  def calc_fitness_sum(self) -> list:
    self.fitness_sum = sum([d.fitness() for d in self.dots])
  
  def get_dot_fitness_weighted(self) -> Dot:
    rand = random.random() * self.fitness_sum
    s = 0
    for d in self.dots:
      s += d.fitness()
      if(s > rand): return d.clone()
    
    return None
  
  def mutate(self) -> None:
    for d in self.dots:
      d.brain.mutate()

    