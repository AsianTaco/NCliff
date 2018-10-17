import numpy as np
from Game import Board


class Agent:

    def __init__(self, discountFactor=0.9):
        self.q_valueTable = np.zeros((5, 10, 4))
        self.discountFactor = discountFactor

    def execPolicy(self, gameboard: Board, greedy=False):
        epsilon = 0.1
        position = gameboard.getPosition()

        if greedy:
            return self.q_valueTable[position].argmax()
        else:
            if np.random.random() < epsilon:
                return np.random.choice(4)
            else:
                return self.q_valueTable[position].argmax()

    def execAction(self, gameboard: Board, actionIndex):
        if actionIndex == 0:
            gameboard.moveUp()
        elif actionIndex == 1:
            gameboard.moveDown()
        elif actionIndex == 2:
            gameboard.moveLeft()
        else:
            gameboard.moveRight()

    def getReward(self, gameboard: Board):
        status = gameboard.getGameStatus()

        if status == 0:
            return -1
        if status == -1:
            return -100
        else:
            return 0

    def updateTable(self, previousPosition, nextPosition, actionIndex, reward):

        discountFactor = 0.9
        learnStep = 0.5

        oldQValue = self.q_valueTable[previousPosition][actionIndex]
        actionIndexForNextPosition = self.q_valueTable[nextPosition].argmax()
        qValueForNextPosition = self.q_valueTable[nextPosition][actionIndexForNextPosition]

        self.q_valueTable[previousPosition][actionIndex] = oldQValue + learnStep * (
                    reward + discountFactor * qValueForNextPosition - oldQValue)
