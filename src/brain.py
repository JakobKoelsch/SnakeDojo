import random
class RandomHead:
    def __init__(self):
        pass

    def next(self):
        move = random.choice(["L","R","S"])
        return move