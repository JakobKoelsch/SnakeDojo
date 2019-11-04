import graphics

dirTransitions = {  "SS":"S", "WS":"W", "NS":"N", "ES":"E",
                    "SL":"E", "WL":"S", "NL":"W", "EL":"N",
                    "SR":"W", "WR":"N", "NR":"E", "ER":"S"  }



class Game:
    def __init__(self, boardSize, graphicsEngine):
        self.board = Board(boardSize)
        self.snakes = []
        self.board.setSnakes(self.snakes)
        self.g = graphicsEngine
        self.g.setSize(boardSize)

    def addSnake(self, pos, dir, ai):
        # TODO: verify board is not already occupied at the new position
        snek = Snake(pos, dir, ai)
        self.snakes.append(snek)

    def game(self):
        #TODO: implement game logic
        anySnakeAlive = True
        gameWindowOpen = True
        while anySnakeAlive and gameWindowOpen:
            gameWindowOpen = self.g.update()
            #TODO: some snake movement
            anySnakeAlive = False
            for snek in self.snakes:
                if snek.isAlive():
                    anySnakeAlive = True
        pass



class Board:
    def __init__(self, size):
        # TODO: implement
        pass

    def setSnakes(self, snakes):
        self.snakes = snakes

class Snake:
    def __init__(self, pos, dir, ai):
        self.head = pos
        self.body = []
        self.dir = dir
        self.brain = ai
        self.alive = True

    def move(self, move):
        if alive:
            #TODO optional: add possibility of faulty behaviour (bad reflexes)
            dir = dirTransitions[self.dir+move]

            if dir == "N":
                pos[1] -= 1
            elif dir == "W":
                pos[0] -= 1
            elif dir == "S":
                pos[1] += 1
            elif dir == "E":
                pos[0] += 1
            else:
                print("Invalid dir in Snake.move()!")

            #TODO: add "snake" chain behaviour

    def isAlive(self):
        return self.alive

    def eat(self):
        #is called before move() call
        #TODO: implement
        pass

    def kill(self):
        self.alive = False

    def getHead(self):
        return self.head

    def getSnake(self):
        return self.head + self.body
    
