# About this course

Professor: Stephyn Butcher

TA: Jordan DeBarth

## Textbook

- Russell, S. & Norvig, P. (2020). ArtiCcial intelligence: A modern approach (4th ed.) Pearson. ISBN-10: 013461097 ISBN-13: 978-0134610997

# Course Topics

- State Space Search
  
  - Recognize appropriate problems and formulate them as state space search problems.
  - Explain the operation of Depth First Search (DFS) and Breadth First Search (BFS) including their performance characteristics.
  - Identify the role that action costs play in state space search and explain how Uniform-Cost Search (UCS), Greedy Search and A* Search take advantage of them.
  - Explain and formulate admissible cost heuristics.
  - Implement a computer program that can solve a state space search problem using DFS, BFS, UCS, Greedy Search and A* Search.

- Local Search/Evolutionary Optimization
  
  - Compare and contrast the State-Space and Local Search approaches and describe appropriate uses for each.
  - Apply hill-climbing and simulated annealing algorithms.
  - Describe different kinds of evolutionary computation, their commonalities and differences.
  - Implement hill-climbing and genetic algorithm to solve a local search problem.

- Pattern Recognition / Example Based Learning & Model Evaluation
  
  - Explain the kNN (k-Nearest Neighbor) algorithm, use cases and extensions.
  - Implement the kNN algorithm.
  - Describe the difference between kNN and Case-Based Reasoning.
  - Describe how kNN can be used to implement a Recommender.
  - Explain and calculate accuracy, precision and recall and describe why precision and recall may be better than accuracy.
  - Explain and conduct cross-validation on real datasets.
  - Explain the bias/variance trade off and how it relates to features and data quantity.
  - Generate and interpret learning curves.

- Hybrid AI/Real World AI
  
  - Explain the Hybrid AI model and place subsequent algorithms in their proper place.
  - Understand the issues surrounding putting AI models in production and design solutions to solve those issues.
  - Implement an application exposing an AI algorithm.

- Adversarial Search
  
  - Identify search problems that are games and understand the terms used in game theory.
  - Apply minimax and alpha-beta pruning to an extensive form game.
  - Explain the role of heuristics in adversarial search.
  - Describe how chance can be incorporated into the game tree and how the expectimax algorithm works.
  - Solve normal form games by finding both pure and mixed strategies.

- Constraint Satisfaction Problems
  
  - Identify and formulate a constraint satisfaction problem.
  - Explain and implement backtracking search with forward checking to solve CSPs.
  - Describe enhancements to backtracking search with forward checking including: Minimum Remaining Values, Degree Heuristic and Least Constraining Value.
  - Explain and implement Conflict Directed Back-jumping.

- Logic
  
  - Describe the kinds of problems that can be solved with reasoning systems.
  
  - Explain and implement the unification algorithms.
  
  - Explain the automated reasoning process using both forward and backward chaining.
  
  - Apply resolution to a reasoning problem.

- Decision Trees
  
  - Interpret a Decision Tree.
  
  - Explain how entropy and information gain are used to learn a Decision Tree from training data.
  
  - Explain the problem of overfitting in Decision Trees and describe some solutions.
  
  - Implement the basic Decision Tree (ID3) algorithm along with improvements such as normalized information gain and numerical features.
  
  - Describe the changes necessary to enable the ID3 algorithm to learn regression trees

- Bayesian Networks
  
  - Describe the problem of uncertainty and how probability permits us to reason about it.
  
  - Explain how a Bayesian Network factors a probability distribution.
  
  - Describe the various types of reasoning that can be conducted with a Bayesian Network.
  
  - Apply Variable Elimination and Gibbs Sampling to make inferences about a Bayesian Network.
  
  - Implement a Naive Bayes Classifier.

- Planning
  
  - Compare the characteristics of a total and partial order planner.
  
  - Apply and implement the STRIPS planning algorithm to a planning problem.
  
  - Apply the GraphPlan algorithm to a planning problem.

- Reinforcement Learning
  
  - Identify and formulate problems that are good candidates for reinforcement learning.
  - Explain and implement value iteration.
  - Explain and implement model-free algorithms such as Q-Learning and SARSA.
  - Describe the basic idea behind the model-driven reinforcement learning approach.
  - Reading: Barto & Sutton, *Reinforcement Learning*
    - Section 4.4, [Value Iteration (Links to an external site.)](http://www.incompleteideas.net/book/ebook/node44.html)
    - Section 6.5, [Q-Learning (Links to an external site.)](http://www.incompleteideas.net/book/ebook/node65.html)
    - Section 6.4, [SARSA](http://www.incompleteideas.net/book/ebook/node64.html)

- Regression and SVM
  
  - Identify and explain the difference between supervised and unsupervised machine learning.
  
  - Explain and implement the gradient descent algorithm for regression.
  
  - Explain and implement the gradient descent algorithm for logistic regression.
  
  - Explain the SVM approach to the linear discriminant.
  
  - Explain the problem linear v. non-linear separability and the role of “The Kernel Trick”.

- Artificial Neural Networks
  
  - Explain the perceptron learning algorithm.
  
  - Identify the key improvements introduced by the multi-layer perceptron.
  
  - Explain the back-propagation algorithm for training a multi-layer perceptron.
  
  - Implement a multi-layer perceptron.
  
  - Describe some of the key issues in using a multi-layer perceptron for a machine learning task.

# Introduction

## Module 1 - State Space Search

This week we start the first of our three main themes: state space search (the others are optimization and pattern recognition).

The basic idea is this: if you have a problem domain and you can represent it as a collection of states and actions, you can turn the problem into a tree or graph with states following other states based on actions. Once the problem is expressed as a tree or graph, we already have algorithms to search trees and graphs: depth first search, breadth first search. The question then shifts to whether we are guaranteed to find a goal and if so, is it the best way to get there? Finally, we shift our focus to better search algorithms and that's where A* search comes in.

This kind of problem solving is something we're all used to, a kind of "what if" reasoning. I want to do something, like finish a degree, then I can start with having taken no classes and then start building out a possible state space with a "take class X" actions. Some of these won't apply because I won't have met the requirements. Later in the semester, we'll see that we can do this kind of planning better with a specific formulation of the problem, but the idea is the same.

What isn't as obvious, however, is that we can use state space search to derive new knowledge. We can also use state space search to play games.

Welcome to Artificial Intelligence.

## Module 2 - Optimization

**or Local Search**

Last week (it seems like only yesterday) we covered the basics of State Space Search. We can think of state space search as our first approximation of reasoning. If you can cast your problem space in terms of states, actions, transitions and costs, then you can use State Space Search to solve problems in that space. And in many cases, that looks like reasoning. Should I go here? Go there? What's the next step? How much will that solution cost?

While you might solve a single problem in that search space (if it's especially complex), it's probably more profitable to apply state space search if you have to solve many problems in that space. We don't install GPS to only find out how to get from New York City to Atlanta but to get directions from many places to many destinations.

This week we look at another one of the components of AI that we'll address this semester: optimization. Many problems in AI involve optimization--if not directly then at least indirectly. And analytical methods will not work for almost all of these problems because they usually have continuous state spaces with multiple optima. No Bordered Hessians here! Note that this is almost a tautology...if you can't use analytical methods, it's an AI problem! (Some have said that AI is "algorithms for NP problems").

We'll look at hill climbing, simulated annealing, and evolutionary computation...specifically the genetic algorithm. There are many, many other methods and they are dear to my heart as Particle Swarm Optimization was the subject of my dissertation research. We'll look at another optimization algorithm, gradient descent, later in the semester. It's worth noting that some of the problems we looked at last week can be cast as optimization problems and solved with local search methods. Usually it's the kinds of problems where we don't care about the path, only the solution.

Take a look at the Self Check and Programming Assignment sooner rather than later. This assignment requires you to both create working code and as part of that working code, you'll need to "experiment" with the proper parameters.

## Module 3 - Pattern Recognition

**or Machine Learning, if you like...**

So far we've covered an algorithm for reasoning (State Space Search) and optimization (Genetic Algorithm/Local Search). In this module, we'll introduce an algorithm for pattern recognition: k Nearest Neighbor. We'll also have a chance to look at some related algorithms: Case Based Reasoning (CBR) and Recommendation Systems.

As I've mentioned, I'm charting a path through these topics that emphasizes a more coherent story about Hybrid AI (more about that next week). As a result, the lecture dependencies have been disrupted a bit. kNN used to be the **last** module of the semester so the lectures assume other content has been covered.

As a result, I made a short Overview video you'll find in Module 3, before the main Lectures content. I apologize for the sniffling but I had just returned from an afternoon outside and my allergies overwhelmed me. You should watch that video **first**. 

We'll also be covering model evaluation. Here we'll cover things like Mean Squared Error, Confusion Matrices, as well as Validation Curves (to help us tune hyperparameters) and Learning Curves (to help us determine if getting more data will help our models). I have made a follow up video for evaluation curves, based on student questions at the time. I don't think this material is adequately covered. You should watch that video **last** (or it won't make sense!).

There's a lot of material this week so start watching early.

The programming assignment is more structured than the previous two but it also let's you "choose your own adventure" (for the last part). If you're not sure about the output for any given section, look at the course notes (this is the only module with course notes so far...)

## Module 4 - Real World AI...

**...this ain't in Norvig & Russell**

We take a break this week from our mad dash to learn various AI algorithms to look at the Big Picture both in terms of "Hybrid AI" (which I still think is funny but ok, I'll roll with it) and "AI in Production". The materials are still somewhat under development because there's very little reference readings for them.

The history (and usual order of topics) of AI has been such that the Symbolic AI that we did the first week is often called "Good Old Fashioned" AI and the Numeric AI we did the second and third weeks is, by contrast, "Modern" AI. And while the death of Symbolic AI has been predicted many times, it's still kicking. We also have the problem of term inflation...any use of data is now "AI". Add to this the necessity and desirability of "Humans in the Loop" and we can't just call this all "AI" anymore...and so maybe "Hybrid AI" isn't so bad. 

We'll talk a little about that this week. The rest of the semester hangs on the idea of Hybrid AI, systems of algorithms/approaches used to solve large scale problems.

The second topic is "AI in Production". Yes, it's nice to have a regression that predicts Concrete Compressive Strength (if that's your problem to solve!) but how does it even get used? How do get stakeholders to buy into this "AI" thing? We'll go through an example ("Case Study") of a system I was involved with at LivingSocial as Machine Learning Manager (whatever **that** meant).

****Materials****

You won't find **any** of this stuff in Norvig...it's either too bleeding edge or **engineering-centric** to be in an academic text. I have provided some reading on Hybrid AI and new lectures but they're a bit more "talky" than the usual ones. I will add additional readings throughout the week.

****Assignments****

This week you will also take a more engineering-centric approach to both the Self Check and the Programming Assignment. I want you to "surface" one of your algorithms from Module 1 (A* Search) or 3 (kNN w/Concrete Compressive Strength)  using Streamlit ([Streamlit • The fastest way to build and share data apps](https://streamlit.io/ "https://streamlit.io/")). Finding out how Streamlit works, exploring the documentation, is your Self Check (you can confer and help each other out in your Discussion Groups).

The Programming Assignment is the surfaced algorithm. See Canvas for details. BTW, you still can't use Pandas! You can use tabulate and Markdown, though. Read the Streamlit documentation! Save your questions for Office Hours...

This week's Module Orientation...

https://wse.zoom.us/rec/share/LHgHKJcaeL1QJFNxvvJtSBIYcu6axS6edwFu8TzZxzlVvJi6BP2hVPkYtQ6NJtjC.JK6XV3UE1OCwq2-9?startTime=1644853150000

Everyone have a great week.

## Module 5 - Adversarial Search

**The games AI play...**

****Review****

Over the first three weeks we've introduced three functional aspects of intelligence and algorithms to implement them in computer programs ("artificial intelligence"). These are reasoning (state space search), optimization (local search), and pattern recognition (kNN). Last week we talked about Artificial Intelligence "in general".

1. Hybrid AI - this is a new term that for some covers AI systems that combine machine learning (Numeric AI) and Humans in the Loop and for others covers AI systems that combine Symbolic AI ("GOFAI") and Numeric AI. For us, Hybrid AI covers all three. This is a framework upon which you can put each algorithm you encounter for the rest of the semester.

2. AI in Production - Algorithms are fine and dandy but how do you get them out of the Notebook and what happens when you do? In this part of the module, we thought about all the different things you need to think about to field a model in production. There's a lot there but hopefully, you'll know what to look out for when you go to do this yourself.

****Module 5****

As I mentioned before, the rest of the semester is basically iterative deepening on these three topics. And this week, Module 5 is an extension of State Space Search (Symbolic AI).

This week we elaborate on State Space Search in the form of games (or "adversarial search"). Games like chess and checkers were once thought of as important tests of intelligence. It turns out it's easier to get a computer to play chess than to recognize a daisy in a picture under all conditions. Who knew?

Games like chess have all the elements needed for State Space Search: states, actions, transitions, costs. The only difference is that in between every move the agent makes, another is making moves as well...and not necessarily with the agent's best interests in mind! Unfortunately, the algorithms discussed this week are not really the algorithms used in modern computer games. However, the algorithms are still very useful.

We will also look at strategic decision making in general using Game Theory (developed by John Nash, *A Beautiful Mind*). One of the algorithms used to solve this problem can use state space search. This is the topic of the programming assignment.

****Goal****

Every week I want to you think about two things:

1) how is this an elaboration or improvement upon the previous algorithm in this "genre"? It's worth noting that "best" has many dimensions and in Machine Learning generally, there is no single best algorithm ("No Free Lunch Theorem").
2) how do I combine this algorithm with algorithms in the other buckets to solve a bigger problem? Or, you can think of the reverse, how do I decompose this bigger problem into subproblems, one of which this algorithm can solve?

## Module 6 - Constraint Satisfaction Problems

**It's not just Sudoku!**

Welcome to Module 6!

This week we specialize State Space Search in a different way to solve a class of problems with constraints (see the pattern?). These generally fall under the class of problems where you don't care about the path through the search space, only the solution. We can contrast these with problems where the path is important and we already know what success looks like. The Farmer/Goat/Wolf/Cabbage and typical navigation problems are of the latter type. We know what success is but we don't know how to get there.

The n-Queens problem is of the former type. We don't care how you place the queens or in what order, we only care that in the end, where you placed them has certain properties. That is, we don't know the solution but we do know what it looks like.  This happens a lot when we need to assign values to variables (Sudoku, Cryptoarithmetic). Of course, these are not all fun and games...all kinds of real world scheduling problems are a constraint satisfaction problems, too.

Always review the self check and programming assignment at the start of the week so there are no surprises later!

The pseudocode is recursive this week. You should study it a bit to see *why* this problem can be solved that way. It will give you special insights into modifying the general algorithm given in Module 1.

Everyone have a great week and a Happy 4th!

## Module 7 - Logic

**and reasoning**

This week we continue to specialize State Space Search to solve very specific kinds of problems. In this case, logical reasoning. We'll spend a lot of time just going over how, exactly, logic actually works and then we'll look at how we might use logic and search to reason about the world using rules.

In the 1950s and certainly through the 70s, logic-based reasoning systems really were what people thought of when they thought of "Artificial Intelligence". Most of the practical applications went under the name of "expert systems" and, even today, companies use Prolog ("programming logic") systems for various tasks. This topic falls under Symbolic AI. **I will be covering these topics in depth in 743 - Advanced AI, in the Fall, if you're interested.**

From a historical perspective, it strangely turned out that creating a calculus solver was easier than creating something that could tell the difference between a dog or a cat in a picture. Go figure! In any case, the rules come from an expert. In the next module, we'll return to a bit of Machine Learning where we try to learn rules from data in the form of Decision Trees. It's interesting to think about where and when each of these two approaches to rules might be better than the other or even combined.

This week we'll cover a lot of ground in logic but the programming assignment covers only a very small part of that: unification. Please make sure you understand what is being requested of you and don't implement too much (I once had a student who tried to implement resolution...not the same thing!).

Finally, **there's no assessment this week but you'll get a grade to make everything work out. You all did very well, congratulations!**

## Module 8 - Decision Trees

**and other rule based ML**

First, I can't believe the semester is about 2/3rds done!

Second, this week the topic is Rules but from the pattern recognition side of AI. We will concentrate mostly on Decision Trees.

Decision Trees fall firmly in the category of "Machine Learning" (pattern recognition). Using various techniques, we develop a tree of decision points much like creating a specialized version of "20 Questions" (although there can be fewer than or more than 20!). Decision Trees are kind of interesting because they're a canonical example of a white-box learning algorithm. That is, we can determine why for some particular inputs (features) a particular prediction was made by inspecting the path of the decisions made through the tree.

This stands in contrast to a blackbox technique like Neural Networks, although there are some cool visualizations of hidden nodes for some kinds of ANNs (usually images processing).

I want you to pay special attention to how we might interpret a path through the tree as a conditional, IF ... THEN ..., rule. Actually, the C4.5 algorithm will often extract the rules from a decision tree and prune **those** individually. You don't really see this much anymore (probably because representing and using the rules themselves is challenging...a tree really is a compact representation). In any case, you should understand a Decision Tree to be a collection of rules. With this understanding, I want you to think back to the last module on Logic/Reasoning and think about the similarities and differences between the two approaches. When might you use one or the other? How might you combine them?

So this week, we take up the strand of pattern recognition again, but with an algorithm that might appear to have interesting similarities and differences with the rules and reasoning systems we investigated last week. Look for those similarities and differences.

You're all doing very well!

## Module 9 - Bayesian Networks

**P(B|A) ~= P(A|B)P(B)**

where "~=" is "proportional to".

This week we continue our investigation of "rules" by looking at Bayesian Networks, which build explicitly on the pattern recognition approach of Decision Trees and at least implicitly on Logic.

Our first observation is that any given rule might not be true all the time. When we looked at reasoning systems, we assumed that rules were definitely true or definitely false and then reasoned our way through to a course of action. With Decision Trees, we also looked for definitely true or definitely false rules, based on the data. Now, we didn't always get them. Sometimes the leaves were not homogeneous, at which point we would use the majority class label.

Still, there's an intuition that taking the majority class label for 51 positive cases versus 49 negative cases in one situation and 78 positive cases versus 22 negative cases in another situation are different things. We have more confidence in the latter than the former. This intuition forms the basis for using probability as a reasoning system. The engine of this reasoning system is Bayes Rule.

Our second observation is that for any given problem, the number of rules grows exponentially in the number of variables and the domains of the variables. If we have a two binary variables, we have 4 rules (2^2). But if we have 10 binary variables, we need 1,024 rules (2^10). But what if classification doesn't depend in every case on every combination of variable values?

In order to make these problems tractable, we use "conditional independence" to partition the feature space into sub-sections and then use Bayes Rule to combine them into an answer. For the programming assignment, we look at the simplest possible Bayesian Network, Naive Bayes Classifier.

We also get to introduce probability, which we will have cause to use later in the semester.

Everyone have a great week!

## Module 10 - Planning

How to get from A to Z with your clothes on...

This is arguably the hardest assignment, at least for most students. Start early...

This week we will be taking what we learned from Modules 1 & 7 and combine them into planning algorithms. This week falls squarely in "GOFAI" or Symbolic AI.

Planning algorithms are, at their essence, state space search...this is especially true for the algorithm you will be implementing: **forward planning**. (Some students in the past have been confused and implemented STRIPS or GraphPlan...those are *not* the right algorithm).

Forward planning is just depth first search so you won't find any pseudocode for it. The interesting bit is the successor states function. Given the current state and the available actions, the list of successor states is generated by all actions that could be applied in the current state.

How do we tell if an action can be applied? We test to see if the preconditions unify with the current state **and recognize they may unify in more than one way**. The best way to accomplish this is...state space search. Here you are searching the state space of clause unifications. But it's a very simple kind of state space search that linearly scans the preconditions and keeps track of the successful branching caused by having multiple ways for a single term to unify with the current state. If you find this all a bit challenging, work it out on paper first! And if you're still perplexed, come to Office Hours on Wednesday!

So forward planning is interesting because it involves two levels of state space search: the outer level is the usual "find a plan" type of state space search and the inner level is "find all the unifications between the current state and potential actions" to generate child states.

You should really try to do this by hand a few times to get the idea of what you need to program. There are two problems here:

1. which actions are applicable in the current state (have their preconditions met in the current state).
2. for any given action that is applicable, are there multiple ways it can be applicable (different ways their preconditions are met in the current state).

Solving a planning problem requires you to investigate **both** possibilities in order to generate all the children of the current state. Of course, you need to apply unification to see if the preconditions are met.

## Module 11 - Reinforcement Learning

Planning when the world doesn't go according to plan

So far this semester, we've toured the big pieces of AI: Symbolic AI and Numeric AI or (roughly): reasoning, optimization, and pattern recognition. Pattern recognition as "machine learning" is usually divided into three main areas (although there are thought to be more these days): Supervised Learning, Unsupervised Learning, and Reinforcement Learning.

We saw supervised learning with Decision Trees and the Naive Bayes Classifier. Basically, we have some features, X, and a target, y, and we try to learn a mapping from X->y that matches the "real" relationship as closely as possible (it's more complicated than this because we may be missing some x's or have x's we don't need). With unsupervised learning, we have only the features, X, and we try to find patterns.

Reinforcement learning is completely different...although you can solve any problem in supervised learning or unsupervised learning with reinforcement learning (it's just not a good idea!). In reinforcement learning, an agent acts in the world and receives feedback on its actions, building up knowledge about how to go about its business (the policy). Now, much of the time "the world" is only a simulation and "acting" is a LOT Of trial and error, but overall, it's really that simple. And so, of course, it's horribly difficult!

We will look at a number of algorithms this week designed to "learn from experience": value iteration, q-learning, SARSA. The programming assignment has been revised this year to be a bit easier by implementing value iteration instead of q-learning (but you can implement q-learning if you want, it's very cool).

## Module 12-13 - Artificial Neural Networks

**...and Module 12 - Linear Regression**

Modules 12 and 13 are the ones that get doubled up because of the shorter Summer semester. You should...

1. Watch Module 12 and 13 lectures.
2. At least look at the Module 12 self check. It is a foundation for the Module 13 concepts.
3. Do the Module 13 self check.
4. Do the Module 13 Programming Assignment.
5. Take the combined Module 12 & 13 assessment.
6. Profit

This week we continue with machine learning and delve into (Artificial) Neural Networks. Neural Networks have experienced a resurgence of late in the guise of *deep* *learning*. It is unfortunate that the name isn't a bit more descriptive. In any case, this week we'll concentrate on *multi-layer perceptrons* (MLP) and afterwards you'll begin to see what the fuss about deep learning (or deep networks) is all about.

By the end of the week, I also want you to see how an MLP is just a bunch of stacked, parallel logistic regressions and that the chief difficulty--solved by the Back Propagation algorithm--is training the weights. Put a different way, think about the work you did last week on the logistic regression as the simplest possible neural network, so simple, the training of the weights was straight forward.

This is important: you really, really need to understand how and why everything is doing what it's doing:

1. a neural network can be though thought of as an actual network where **signals** travel from node to node. 2. for *output*, the signals travel forward. As you complete the self check, think of the calculations as signals moving forward through the network. *3.* for **backpropagation**, the signals travel **backward**, I have drawn the arrows point back for this reason. But it's probably even better if you go ahead and redraw the network reversed (draw the outputs, hidden layers, then inputs).

Trace these back and forth. We will go over this in Office Hours (Thursday, 7p ET).

Please be aware that this assignment uses **stochastic** gradient descent, which is slightly different than "regular" or "batch" gradient descent (you won't have done last week's lesson but if you look at the pseudocode it is different). For "convergence" it is ok to pick a large number of iterations (experiment!) rather than use epsilon again. **Be methodical in your programming. Make lots of small functions, thoroughly tested. I cannot emphasize this enough...**

Have a great week!

## Check List

- [x] Everyday: respond to email (give detail information, reduce misunderstanding)

- [x] Everyday: Check Canvas on Announcements, Posts, etc.

- [x] Everyday: Check Team and "Like" every post from professor, as acknowledge that we have read it

- [x] Monday: Module Open: 
  
  - [x] Review Self-Check (do the algorithm by hand), PA (implementation)
  - [x] Watch Lectures (Videos), extra reading materials. 
  - [ ] Read Textbook: the relevant part. 

- [x] Wednesday: Office Hours

- [x] Thursday night: **Submit** Self-Check in PDF in Canvas, (complete or incomplete)

- [x] Early Friday: **Post** self-check questions in discussion group.  

- [x] Middle Sunday: Group self check **comments** (discuss conceptually). Review at least two other self-checks and post comments. Start with fewest responses so far. Respond to ALL questions(?).

- [x] Sunday: **Assessment**, 10 questions this week, 5 random from previous. 45mins, Randomized. Can not go back. => Do it as early as you can. The programming not help assessment, but assessment might help programming. 

- [x] Sundays: **PA**: Submit notebook: <JHED ID>.ipynb

- [x] Mindmap

- [x] Special: Overview -> Lecture -> Model evaluation. Look for course notes for the output. 

## Programming Assignments

- In functional style: Functional Programming approach constructs programs by building up small easily testable *pure* functions into a domain specific language (DSL) for the problem at hand called by *impure* functions at the edges of the program.
  
  - Functions are first class values, independent of Classes or Types.
  - Data modeling with generic data structures: lists, sets, dictionaries, tuples instead of Classes.
  - Operations such as iteration are replaced with higher level oft repeated abstractions such as map, filter and reduce.

- Office hour 1
  
  - Basic python structures. 
  - Functional, take arguments and return arguments. 
  - Documentation: clear, follow template, ID, name, function, description, the theory behind (A* requries a heuristic)
  - Implementation: better with annotation, optional. 
  - 3 unit tests - corner cases ... assert. 
  - **Only the requested output is acceptable.** 
  - Under 20 lines

- Professor will: answer all questions, prior to submission, about the algorithm

# Tips

- Take one course at at time. Two courses for full time students.

- Coding
  
  - Use Dictionary to manages the parameters
  
  - 20 lines per function
  
  - Unit test.

- Focus on logic. No library (except IO and math). 

- Understand the problem and the benefits gained in selecting a particular strategy or tools. Focus on the trade offs. Consider Pro and cons among many different factors, such as: 
  
  - Programming environment
  - Time constraints
  - Existing code
  - Personal preferences

- [Feynman Technique](https://en.wikipedia.org/wiki/Feynman_Technique)
  
  - **Concept**: Choose the subject to study
  - **Explain**: Pretend to explain it to a child
  - **Fill**: Fill in gaps in understanding exposed in step 2 by returning to the sources
  - **Simplify**: Simplify the explanation

- Discussion: Critical thinking

# Paper and article

3CQs...

1. Compliment the previous post
2. make the Comment.
3. make a Connection
4. ask a Question.

[AI could make health care fairer—by helping us believe what patients say](https://www.technologyreview.com/2021/01/22/1016577/ai-fairer-healthcare-patient-outcomes/#:~:text=Artificial%20intelligence-,AI%20could%20make%20health%20care%20fairer%E2%80%94by%20helping%20us%20believe,gaps%20in%20existing%20medical%20knowledge)

[ANDREW NG: UNBIGGEN AI - The AI pioneer says it’s time for smart-sized, “data-centric” solutions to big issues]([Andrew Ng: Unbiggen AI - IEEE Spectrum](https://spectrum.ieee.org/andrew-ng-data-centric-ai))

[ARTIFICIAL INTELLIGENCE IS MISREADING HUMAN EMOTION](https://www.theatlantic.com/technology/archive/2021/04/artificial-intelligence-misreading-human-emotion/618696/)

[Explainable Monitoring: Stop flying blind and monitor your AI](https://www.fiddler.ai/blog/explainable-monitoring-stop-flying-blind-and-monitor-your-ai)

[A Gentle Introduction to Concept Drift in Machine Learning](https://machinelearningmastery.com/gentle-introduction-concept-drift-machine-learning/)

[Too many AI researchers think real-world problems are not relevant](https://www.technologyreview.com/2020/08/18/1007196/ai-research-machine-learning-applications-problems-opinion/)
