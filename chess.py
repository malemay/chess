from Game import Game

game = Game()
game.display()

while(not game.gameover):
    game.move()
    game.display()


