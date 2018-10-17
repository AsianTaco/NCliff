import numpy as np


class Board:

    def __init__(self):
        self.state = self.createInitialBoard()

    def createInitialBoard(self):
        self.position = (4, 0)
        self.goal = (4, 9)
        self.gameStatus = 0

        initialBoard = np.zeros((5, 10))

        initialBoard[self.position] = 2
        initialBoard[self.goal] = 1

        for i in range(1, 9):
            initialBoard[(4, i)] = -1

        return initialBoard

    def showBoard(self):
        print(self.state)
        print('\n')

    def checkConsequences(self, newPosition):
        if newPosition == self.goal:
            self.gameStatus = 1
            print("You won.")
        elif self.state[newPosition] == -1:
            self.gameStatus = -1
            print("You lost.")

    def getPosition(self):
        return self.position

    def getGameStatus(self):
        return self.gameStatus

    def moveUp(self):

        y, x = self.position

        if y > 0:
            y -= 1

            self.state[self.position] = 0

            newPosition = (y, x)
            self.checkConsequences(newPosition)

            self.position = newPosition
            self.state[self.position] = 2

    def moveDown(self):

        y, x = self.position

        if y < 4:

            y += 1

            self.state[self.position] = 0

            newPosition = (y, x)
            self.checkConsequences(newPosition)

            self.position = newPosition
            self.state[self.position] = 2

    def moveLeft(self):
        y, x = self.position

        if x > 0:

            x -= 1

            self.state[self.position] = 0

            newPosition = (y, x)
            self.checkConsequences(newPosition)

            self.position = newPosition
            self.state[self.position] = 2

    def moveRight(self):
        y, x = self.position

        if x < 9:

            x += 1

            self.state[self.position] = 0

            newPosition = (y, x)
            self.checkConsequences(newPosition)

            self.position = newPosition
            self.state[self.position] = 2