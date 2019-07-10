# Cliff Walking problem

An implementation of tabular Q-learning for the Cliff Walking problem as described by Richard S. Sutton and Andrew G. Barto's book "Reinforcement Learning: An Introduction" MIT Press, 2018, p. 132.

## Setup

This project can be setup by cloning this repository and installing the dependencies by running

```
pip install -r requirements.txt
```
You might want to install the dependecies in a seperate virtual environment, if you have other python projects as well.

## Components

This project consist of three files: Agent.py, Gameboard.py and main.py

### Agent.py

This component implements the agent and the Q-learning control algorithm (Watkins, 1992). The agent can either use an epsilon-greedy policy or a greedy policy that maximises over the estimated Q-values.

### Gameboard.py

This component implements a 5x10 gridworld with the Cliff evironment in a numpy array. The agent's position is represented by the number 2; the save positions are presented by the number 0; the number -1 represents the grids on which the cliff is situated and the number 1 represents the goal.

### main.py

This script trains the agent for 100 episodes in the cliff walking problem with the epsilon-greedy policy and then visualises one episode in which the agent follows the greedy policy. Furthermore, the training results over the 100 episodes are plotted and the estimated Q-values of all action-state pairs are also printed out.
Run this script with

````
python main.py
````