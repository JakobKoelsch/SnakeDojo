import graphics
import numpy as np
import random

dirTransitions = {  "SS":"S", "WS":"W", "NS":"N", "ES":"E",
                    "SL":"E", "WL":"S", "NL":"W", "EL":"N",
                    "SR":"W", "WR":"N", "NR":"E", "ER":"S"  }


EMPTY = 0
FOOD = 1
DEATH = 2
X = 0
Y = 1

class Game:
    def __init__(self, boardSize, graphicsEngine):
        self.board = Board(boardSize)
        self.snakes = []
        self.board.setSnakes(self.snakes)
        self.g = graphicsEngine
        self.g.setSize(boardSize)

    def addSnake(self, pos, dir, brain):
        if not self.board.isOccupied(pos):
            snek = Snake(pos, dir, brain)
            self.snakes.append(snek)
        else:
            print("Tried to spawn snake at occupied position ", pos)

    def game(self):
        anySnakeAlive = True
        gameWindowOpen = True
        while anySnakeAlive and gameWindowOpen:
            gameWindowOpen = self.g.update()
            self.board.moveSnakes()
            anySnakeAlive = self.board.anySnakeAlive()
            self.board.keepFoodLevel(1)
            self.giveFeedback()

    def giveFeedback(self):
        for snek in self.snakes:
            #TODO: to something
            #e.g. if snek.fullStomach: reward else: punish
            #also check for death, maybe have extra punishment for every dead round with others alive
            #depends if i do real time learning or add the feedback to one loss fctn
            pass


class Board:
    def __init__(self, size):
        self.board = np.zeros((size,size))
        self.snakes = []
        self.food = []

    def isOccupied(self, pos):
        self.fillBoard()
        return self.board[pos[X]][pos[Y]] == EMPTY

    def spawnFood(self, n):
        spawned = 0
        rand = np.zeros((2,1))
        while spawned < n:
            randX = random.choice(range(len(self.board)))
            randY = random.choice(range(len(self.board[0])))
            if self.board[randX, randY] == EMPTY:
                self.board[randX, randY] = FOOD
                spawned += 1

    def keepFoodLevel(self, n):
        if len(self.food) < n:
            self.spawnFood(n-len(self.food))

    def setSnakes(self, snakes):
        self.snakes = snakes

    def anySnakeAlive(self):
        ret = False
        for snek in self.snakes:
            if snek.isAlive():
                ret = True
        return ret

    def moveSnakes(self):
        for snek in self.snakes:
            nextMove = snek.brain.next()
            snek.move(nextMove)

        self.fillBoard()
        
        for snek in self.snakes:
            coll = self.collision(snek.getHead())
            if coll == FOOD:
                snek.eat()
            elif coll == DEATH:
                snek.kill()
            elif coll == EMPTY:
                pass
            else:
                print("Error: Faulty board element.")

    def fillBoard(self):
        self.board = np.empty_like(self.board)
        for yum in self.food:
            self.board[yum[X], yum[Y]] = FOOD
        for snek in self.snakes:
            for bodyPart in snek.getSnake():
                self.board[bodyPart[X], bodyPart[Y]] = DEATH


    def collision(self, head):
        ret = DEATH
        if head[X] not in range(len(self.board)) or head[Y] not in range(len(self.board)):
            ret = DEATH
        else:
            ret = self.board[head[X], head[Y]]
        return ret 



class Snake:
    def __init__(self, pos, dir, brain):
        self.head = pos
        self.body = []
        self.dir = dir
        self.brain = brain
        self.alive = True
        self.fullStomach = True

    def move(self, move):
        if self.alive:
            #TODO optional: add possibility of faulty behaviour (bad reflexes)
            pos = list(self.head)
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
            
            self.body.insert(0, self.head)
            self.head = tuple(pos)          
            if self.fullStomach:
                self.fullStomach = False
            else:
                self.body.pop()



    def isAlive(self):
        return self.alive

    def eat(self):
        self.fullStomach = True

    def kill(self):
        self.alive = False

    def getHead(self):
        return self.head

    def getSnake(self):
        return [self.head] + self.body
    
