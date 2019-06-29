import Gameboard
import Agent

agent = Agent.Agent()

for i in range(100):
    game = Gameboard.Gameboard()

    while game.getGameStatus() == 0:
        firstPosition = game.getPosition()
        actionIndex = agent.execPolicy(game)
        agent.execAction(game, actionIndex)
        newPosition = game.getPosition()
        reward = agent.getReward(game)
        agent.updateTable(firstPosition, newPosition, actionIndex, reward)

game = Gameboard.Gameboard()
game.showBoard()

while game.getGameStatus() == 0:
    actionIndex = agent.execPolicy(game, greedy=True)
    agent.execAction(game, actionIndex)
    game.showBoard()

print(agent.q_valueTable)
