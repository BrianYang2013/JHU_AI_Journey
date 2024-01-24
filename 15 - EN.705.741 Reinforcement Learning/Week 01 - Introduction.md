# Textbook

- In this book we explore a **computational** approach to learning from interaction.

- goal-directed learning from interaction; Response, Influence, 
- Reinforcement learning is learning what to do—**how to map situations to actions**—so as to maximize a numerical reward signal.
- Most important distinguishing features of RL: Trial-and-error search and deplayed reward
- RL vs Supervised learning: Label; extrapolate or generalization; learn from experience
- RL vs Unsupervised learning: Maximize a reward signal instead of trying to find hidden structure. 
- **Trade-off between exploration and exploitation.** 
- 

# Terminology

- Problem, environment, Agent
- decision policy
- Return, episode
- Episodic vs. Continuous
- Reward signal r， value function $V^ \pi$ or Q^pi, Policy Pi, Model of the environment

## Dynamical systems theory





## Markov decision processes

Markov Decision Processes (MDPs) are a fundamental concept in the field of reinforcement learning and decision-making. Let's break this down into simpler terms:

1. **Markov Process**: At its core, a Markov process is a mathematical system that experiences transitions from one state to another, according to certain probabilistic rules. The key feature is the Markov property: the future state depends only on the current state and not on the sequence of events that preceded it.
2. **Decision**: This is where you come in! In a Markov Decision Process, decisions or actions are made at each state, influencing the transition to the next state.
3. **Process**: It refers to the sequence of states and actions over time.

Now, let's dive into the components of an MDP:

- **States (S)**: These are the different situations or positions the system can be in.
- **Actions (A)**: At each state, there are various actions that you can take.
- **Transition Probability (P)**: This is a mathematical way of saying how likely it is to move from one state to another, given an action.
- **Reward (R)**: After taking an action and moving to a new state, you receive a reward (or penalty). This guides the learning process towards desirable outcomes.

The objective in an MDP is usually to find a policy (a way of choosing actions based on the current state) that maximizes some notion of cumulative reward.

### Examples:

1. **Robot Navigation**: Imagine a robot in a grid-like environment. Each grid cell is a state. The robot can move up, down, left, or right (actions). The transition probabilities depend on the robot's movement accuracy (it might not always go where it intends). The goal (reward) could be to find the shortest path to a specific location without bumping into obstacles (which might give negative rewards).
2. **Inventory Management**: Consider a store managing its inventory. The state is the current level of stock. Actions are ordering different quantities of new stock. The transition probabilities are related to the uncertainty in demand. The reward could be profit, and negative rewards come from situations like stockouts or excessive inventory.
3. **Game Playing (like Chess or Go)**: Each game position is a state. The actions are the possible moves. Transition probabilities are typically deterministic in these games (if you make a move, the position changes in a predictable way). Rewards are given for winning, losing, or drawing the game.
4. **Healthcare Treatment Plans**: Patients in different stages of a disease are in different states. The actions are various treatment options. Transition probabilities involve the likelihood of a patient's health improving or deteriorating given a treatment. Rewards are assigned based on the health outcomes for the patient.
5. **Financial Decision Making**: In investment strategies, the state could be the current portfolio. Actions are buying or selling assets. Transition probabilities involve market uncertainty. Rewards are based on portfolio performance.
6. **Environment Control (like Smart Thermostats)**: The state is the current room temperature and conditions. Actions are adjusting the thermostat settings. Transition probabilities depend on external temperature and the effectiveness of the heating/cooling system. The reward is based on maintaining comfortable temperatures efficiently.



## Stochastic task

A stochastic task refers to a task or process that is inherently random or unpredictable, often influenced by random variables. It's the opposite of a **deterministic** task, where outcomes are predictable and consistent under the same conditions. 

To understand this better, let's dive into the technical details and use some analogies:

1. **Technical Detail**: In stochastic tasks, outcomes are modeled using probability distributions rather than fixed values. This means that instead of saying "this will happen," we say "there's a certain probability of this happening."

2. **Analogy**: Think of a stochastic task like fishing in a large lake. You have general knowledge about where fish might be, but catching a fish at a specific time and place involves chance. You can't predict exactly when or where you'll catch a fish, but you can estimate the likelihood based on factors like time of day, weather, and the type of bait used.

Examples of stochastic tasks:

- **Stock Market Investment**: The stock market is inherently unpredictable. While you can analyze trends and historical data, the future movement of stock prices involves a degree of randomness.

- **Weather Forecasting**: Meteorologists use probabilistic models to predict weather. They can estimate the likelihood of rain or snow, but there's always an element of uncertainty due to the complex and chaotic nature of weather systems.

- **Machine Learning**: Many machine learning algorithms, especially those involving neural networks or genetic algorithms, have stochastic elements. They might start with random weights or make random mutations, leading to slightly different outcomes even with the same input data.

- **Queueing Theory in Operations Research**: This involves modeling systems like customer service lines or traffic flow, where arrivals and service times can be unpredictable.
