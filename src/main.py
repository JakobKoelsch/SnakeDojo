import snake
import graphics
import brain

class DummyGraphics:
    def __init(self):
        pass

    def update(self):
        return True

    def setSize(self, x):
        pass
g = DummyGraphics()
game = snake.Game(10, g)
game.addSnake((2,2), "S", brain.RandomHead())
# game.addSnake((2,2), "S", brain.RandomHead())
game.game()
