# Read

## Building Machines That Learn and Think Like People

### 0 Abstract

We argue that these machines should 

1. build causal models of the world that support explanation and understanding, rather than merely solving pattern recognition problems; 
2. ground learning in intuitive theories of physics and psychology, to support and enrich the knowledge that is learned; 
3. harness compositionality and learning-to-learn to rapidly acquire and generalize knowledge to new tasks and situations. 

### 1. Introduction

Neural network, deep learning, convolutional neural network, Model-free and model-based reinforcement learning, deep reinforcement learning, Deep Q-learning, Generative model, Program induction, probabilistic machine learning. object recognition/speech recognition/control,  human learning and human cognition. **Intuitive physics, theory of mind, causal reasoning.**  mental models or intuitive theories. 

In this article

- Review some of the **criteria** previously offered by cognitive scientists, developmental psychologists, and AI researchers. 
- We articulate what we view as the **essential ingredients** for building such a machine that learns or thinks like a person, synthesizing theoretical ideas and experimental data from research in cognitive science. 
- We consider contemporary AI (and deep learning in particular) in light of these ingredients, finding that deep learning models **have yet to incorporate many of them** and so may be solving some problems in different ways than people do. 
- We end by discussing what we view as the most **plausible paths** towards building machines that learn and think like people. This includes prospects for integrating deep learning with the core cognitive ingredients we identify, inspired in part by recent work fusing neural networks with lower-level building blocks from classic psychology and computer science (attention, working memory, stacks, queues) that have traditionally been seen as incompatible. 

Two different computational approaches to intelligence.

- The statistical pattern recognition approach treats **prediction** as primary. In this view, learning is about discovering features that have high value states in common. 
- The alternative approach treats models of the world as primary, where **learning** is the process of model-building.

It is important to draw a distinction between AI that purports to emulate or draw inspiration from aspects of human cognition, and AI that does not.

creativity, common sense, and general purpose reasoning

Overview of the key ideas

- Start-up software, or cognitive capabilities present early in development: **intuitive physics, intuitive psycholog**
- Learning: construction of causal models of the world: **compositionality and learning-to-learn**
- How the rich models our minds build are put into action, in real time 
- The integration of model-based and model-free methods in reinforcement learning 

### 2. Cognitive and neural inspiration in artificial intelligence

PDP: parallel distributed processing

### 3. Challenges for building more human-like machines

A different picture has emerged that highlights the importance of early inductive biases, including core concepts such as **number, space, agency and objects**, as well as powerful **learning algorithms** that rely on prior knowledge to extract knowledge from small amounts of training data. 

While humans and neural networks may perform equally well on the MNIST digit recognition task and other large-scale image classification tasks, it does not mean that they learn and think in the same way. 

- people learn from fewer examples and they learn richer representation
- Moreover, people learn more than how to do pattern recognition: they learn a **concept** – that is, a model of the class that allows their acquired knowledge to be flexibly applied in new ways. people can also generate **new** example. 

The DQN was a significant advance in reinforcement learning, showing that a single algorithm can learn to play a wide variety of complex tasks. 

Transfer learning

One way to examine the differences is by considering the amount of experience required for learning. The differences
between the human and machine learning curves suggest that they may be learning different kinds of knowledge, using different learning mechanisms, or both. 

The learned DQN network is also rather inflexible to changes in its inputs and goals. People can learn models and use them for arbitrary new tasks and goals. 

It is not that DQN and people are solving the same task differently. They may be better seen as solving different tasks. Human learners – unlike DQN and many other deep learning systems – approach new problems armed with extensive prior experience. The human is encountering one in a years-long string of problems, with rich overlapping structure. Humans as a result often have important domain-specific knowledge for these tasks, even before they ‘begin.’ The DQN is starting completely from scratch.

### 4. Core ingredients of human intelligence

#### 4.1 Developmental start-up software

Early in development, humans have a foundational understanding of several core domains: **number** (numerical and set operations), **space** (geometry and navigation), **physics** (inanimate objects and mechanics) and **psychology**
(agents and groups). The underlying cognitive representations can be understood as “**intuitive theories**,” with a causal structure resembling a scientific theory.

##### Intuitive physics

##### Intuitive psychology

Pre-verbal infants distinguish animate agents from inanimate objects.  infants also expect agents to act contingently and reciprocally, to have goals, and to take efficient actions towards those goals subject to constraints. It is generally agreed that infants expect agents to act in a goal-directed, efficient, and socially sensitive fashion. 

- generative models of action choice, "naive utility calculus” models,  predictive coding.  

#### 4.2 Learning as rapid model building

Children may only need to see a few examples before they largely ‘get it,’ grasping the boundary of the infinite set that defines each concept from the infinite set of all possible objects. 

It is also important to mention that there are many classes of concepts that people learn more slowly. 

##### Compositionality: 

Compositionality is the classic idea that new representations can be constructed through the combination of primitive elements.

##### Causality

To explain the role of causality in learning, conceptual representations have been likened to intuitive theories or explanations, providing the glue that lets core features stick while other equally applicable features wash away. 

Beyond concept learning, people also understand scenes by building causal models. Human-level scene understanding involves composing a story that explains the perceptual observations, drawing upon and integrating the ingredients of intuitive physics, intuitive psychology, and compositionality.

##### Learning-to-learn

When humans or machines make inferences that go far beyond the data, strong prior knowledge (or inductive biases or constraints) must be making up the difference. 

Leanring-to-learn: closely related to the machine learning notions of “transfer learning”, “multi-task learning” or “representation learning.” 

#### 4.3 Thinking Fast

##### Approximate inference in structured models

Hierarchical Bayesian models; remarkable effectiveness of gradient-based learning in high-dimensional parameter spaces; probabilistic machine learning; Monte Carlo sampling; 

Discovering new theories can be slow and arduous, as testified by the long timescale of cognitive development, and learning in saltatory fashion (rather than through gradual adaptation) is characteristic of aspects of human intelligence, including discovery and insight during development. 

##### Model-based and model-free reinforcement learning

### 5. Responses to common questions

- Comparing the learning speeds of humans and neural networks on specific tasks is not meaningful, because humans have extensive prior experience.
  - multi-task learning or transfer learning
  - we see them as fundamental building blocks for facilitating rapid learning from sparse data.
  - Option 1: if only they can just get big enough training datasets, sufficiently rich tasks, and enough computing power – far beyond what has been tried out so far – then deep learning methods might be sufficient to learn representations equivalent to what evolution and learning provides humans with. 
  - Option 2: build in appropriate infant-like knowledge representations and core ingredients as the starting point for our learning-based AI systems, or to build learning systems with strong inductive biases that guide them in this direction.
- Biological plausibility suggests theories of intelligence should start with neural networks
  - Our approach is guided by a pragmatic view that the clearest path to a computational formalization of human intelligence comes from understanding the “software” before the “hardware.” In the case of this article, we proposed key ingredients of this software in previous sections. 
  -  Unfortunately, what we “know” about the brain is not all that clear-cut. 
  - most neural networks use some form of gradient-based (e.g., backpropagation) or Hebbian learning. BP not have biological support, and the cognitive significance of any biologically grounded form of Hebbian learning is unclear. 

- Language is essential for human intelligence. Why is it not more prominent here?
  

### 6. Looking forward

#### 6.1 Promising directions in deep learning

- integrating psychological ingredients with deep neural networks, especially selective attention
- augmented working memory
- experience replay
- developing neural networks with “working memories” that augment the shorter-term memory provided by unit activation and the longer-term memory provided by the connection weights
- differentiable programming suggests the intriguing possibility of combining the best of program induction and deep learning.
- One worthy goal would be to build an AI system that beats a world-class player with the amount and kind of training human champions receive – rather than overpowering them with Google-scale computational resources. 
  - What would it take to build a professional-level Go AI that learns from only 50,000 games? 
  - humans can learn the basics of the game quickly through a combination of explicit instruction, watching others, and experience. Playing just a few games teaches a human enough to beat someone who has just learned the rules but never played before. Could AlphaGo model these earliest stages of real human learning curves?

#### 6.2 Future applications to practical AI problems

- Scene understanding
- Autonomous agents and intelligent devices
- Autonomous driving
- Creative design

#### 6.3 Towards more human-like learning and thinking machines



# Sparks of Artificial General Intelligence - Early experiments with GPT-4



# Misc

Inductive Bias
