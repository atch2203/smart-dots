import pygame
from consts import HEIGHT, WIDTH
from dot import Dot
from goal import Goal
from population import Population

class Game:
  def __init__(self) -> None:
    self.dots = Population(20)

  def restart(self) -> None:
    self.dots.selection()
    self.dots.mutate()
    

  def run(self) -> None:
    pygame.init()

    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.clock = pygame.time.Clock()
    self.goal = Goal()
    self.running = True

    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      self.loop()
    
  def loop(self):
    if self.dots.done():
      self.restart()

    self.screen.fill("white")

    self.dots.update()
    self.dots.show(self.screen)

    self.goal.show(self.screen)

    pygame.display.flip()

    self.clock.tick(320)

  pygame.quit()

if __name__ == "__main__":
  game = Game()
  game.run()