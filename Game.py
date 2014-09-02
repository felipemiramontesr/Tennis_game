import os

scores = [0, 15, 30, 40, "win"]

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
  >>> game.scores(1).scores(1).scores(2).scores(2).score()
  Deuce
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).score()
  [40, 40]
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).score()
  Advantage player 1
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).score()
  Deuce
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).scores(2).score()
  Advantage player 2
  >>> game = Game()
  >>> game.scores(1).scores(1).scores(1).scores(2).scores(2).scores(2).scores(1).scores(2).scores(2).scores(2).score()
  The winner is player 2
  """

  score_player1 = 0   #score index player 1
  score_player2 = 0   #score index player 2
  advantage = 0       #number of player
  winner = 0          #number of player
  deuce = False
  
  def scores(self, player):
    if self.deuce == False:
      #add point
      if player == 1:
        self.score_player1 += 1
      elif player == 2:
        self.score_player2 += 1

      #winner
      if self.score_player1 >= 4:
        self.winner = 1
      elif self.score_player2 >= 4:
        self.winner = 2
    else:
      #advantage
      if self.advantage == 0:
        self.advantage = player
      elif self.advantage == player:
        self.advantage = 0
        self.winner = player
      else:
        self.advantage = 0
    
    #deuce
    self.deuce = True if self.score_player1 == 3 and self.score_player2 == 3 else False

    return self

  #print score
  def score(self):
    if self.advantage > 0:
      print("Advantage player", self.advantage) 
    elif self.winner > 0:
      print("The winner is player", self.winner) 
    elif self.deuce == True:
      print("Deuce")
    else:
      print ([scores[self.score_player1], scores[self.score_player2]])

game = Game()
 