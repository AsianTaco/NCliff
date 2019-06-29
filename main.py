from Gameboard import Gameboard
from Agent import Agent

import numpy as np
import matplotlib.pyplot as plt


agent = Agent()

game_record = []

print('Training agent for {} games'.format(100))
for i in range(100):
    game = Gameboard()

    while game.getGameStatus() == 0:
        firstPosition = game.getPosition()
        actionIndex = agent.execPolicy(game)
        agent.execAction(game, actionIndex)
        newPosition = game.getPosition()
        reward = agent.getReward(game)
        agent.updateTable(firstPosition, newPosition, actionIndex, reward)

    game_record.append(game.getGameStatus())

plt.plot(game_record)
plt.ylabel('Game results')
plt.title('Game record over {} games'.format(100))
plt.show()

print('Testing trained agent for one game')

game = Gameboard()
game.showBoard()

while game.getGameStatus() == 0:
    actionIndex = agent.execPolicy(game, greedy=True)
    agent.execAction(game, actionIndex)
    game.showBoard()

print('Action values for moving up at this position:')
print(np.matrix(np.around(agent.q_valueTable[:,:,0],2)))
print('Action values for moving down at this position:')
print(np.matrix(np.around(agent.q_valueTable[:,:,1],2)))
print('Action values for moving left at this position:')
print(np.matrix(np.around(agent.q_valueTable[:,:,2],2)))
print('Action values for moving right at this position:')
print(np.matrix(np.around(agent.q_valueTable[:,:,3],2)))
