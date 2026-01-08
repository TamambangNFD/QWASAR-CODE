# Welcome to Atari Games
***

## Task
The objective of this project is to build artificial intelligence agents capable of playing Atari video games using Deep Reinforcement Learning.
The main challenge lies in the high-dimensional state space of Atari games, where the agent must learn directly from raw pixel inputs rather than predefined rules or features. Traditional Q-tables are infeasible due to the enormous number of possible states, requiring neural networks to approximate the action-value function.


## Description
This project solves the problem using Deep Q-Networks (DQN). Each game environment is modeled as a reinforcement 
learning task where an agent interacts with the game, receives rewards, and learns an optimal policy over time.

Three models were implemented:
CartPole: Uses a simple multilayer perceptron to learn control from low-dimensional state vectors.
Space Invaders: Uses a convolutional neural network to process raw game frames and learn shooting and movement strategies.
Pacman: Uses a convolutional neural network with frame stacking to learn navigation, reward collection, and enemy avoidance.
All models are trained from scratch using experience replay, ε-greedy exploration, and temporal-difference learning.

## Installation
Install the required dependencies using pip:

pip install gymnasium gymnasium [Atari] gymnasium[classic control] ale-py
pip install torch numpy matplotlib opencv-python

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121


## Usage
Each game is provided as a Jupyter notebook:
cartpole.ipynb
spaceinvaders.ipynb
pacman.ipynb

Open a notebook and run all cells to start training the agent.
During training, reward plots are displayed to visualize learning progress.

After training, the agent can be tested by running the evaluation cell, 
which renders the game and allows you to watch the trained model play autonomously.
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
