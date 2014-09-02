import os

class Game:
  """
  >>> game = Game()
  >>> game.score()
  [0, 0]
  >>> game = Game()
  >>> game.scores(1).score()
  [15, 0]
  >>> game = Game()
  >>> game.scores(1).scores(1).score()
  [30, 0]
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).score()
  [40, 0]
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(2).score(2).score()
  Deuce
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).score(2).score(2).score(2).score()
  [40, 40]
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).score(2).score(2).score(2).scores(1).score()
  Advantage player 1
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).score(2).score(2).score(2).scores(1).scores(2).score()
  Deuce
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).score(2).score(2).score(2).scores(1).scores(2).scores(2).score()
  Advantage player 2
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).score(2).score(2).score(2).scores(1).scores(2).scores(2).scores(2).score()
  The winner is player 2
  """

  
 