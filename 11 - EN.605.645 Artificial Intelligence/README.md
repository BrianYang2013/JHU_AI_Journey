# About this course

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

- Logic

- Decision Trees

- Bayesian Networks

- Planning

- Reinforcement Learning

- Regression and SVM

- Artificial Neural Networks

## Check List

- [ ] Everyday: respond to email (give detail information, reduce misunderstanding)
- [ ] Everyday: Check Canvas on Announcements, Posts, etc.
- [ ] Everyday: Check Team and "Like" every post from professor, as acknowledge that we have read it
- [ ] Monday: Module Open: 
  - [x] Review Self-Check (do the algorithm by hand), PA (implementation)
  - [ ] Watch Lectures (Videos), extra reading materials. 
  - [ ] Read Textbook: Only the relevant part. 

- [x] Wednesday: Office Hours
- [x] Thursday night: **Submit** Self-Check in PDF in Canvas, (complete or incomplete)
- [ ] Early Friday: **Post** self-check questions in discussion group.  
- [ ] Middle Sunday: Group self check **comments** (discuss conceptually). Review at least two other self-checks and post comments. Start with fewest responses so far. Respond to ALL questions(?).
- [ ] Sunday: **Assessment**, 10 questions this week, 5 random from previous. 45mins, Randomized. Can not go back. => Do it as early as you can. The programming not help assessment, but assessment might help programming. 
- [ ] Sundays: **PA**: Submit notebook: <JHED ID>.ipynb
- [ ] Mindmap
- [ ] Special: Overview -> Lecture -> Model evaluation. Look for course notes for the output. 

## **Programming Assignments**

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

- Grade criteria:
  
  - Conform to the course programming requirements
  - Provide the requested output correctly

- A: 9-10

- 

## Grading

**Grades:** 

- Self-checks: 13/14, SU 12/12
- Programming Assignments: 12/ 14, SU 10/12
- Assessments: 12/14, SU 10/13
  - A: 13-15 pts each time
- Class Participation: A

# Notes

2022-06-01: Office hour

- Take one course at at time. Two courses for full time students. 
- No late. No external resources. No google. 

# Tips

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

# Reference

## General

## CheatSheet and Tools

- *[Big O Cheat Sheet](http://bigocheatsheet.com/)*
- *[Time (and Space) Complexity of Various Sorting Algorithms](http://scanftree.com/Data_Structure/time-complexity-and-space-complexity-comparison-of-sorting-algorithms)*
- *[Visual Data structure](https://visualgo.net/en)*

## Naming Convension

Style:

- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

Reference: 

- https://www.jianshu.com/p/a793c0d960fe

- https://www.python.org/dev/peps/pep-0008/#naming-conventions

Module, package: a_b.py

Class: ThisIsAClass. Pascal style. 

Variable:

- Global: NUMBER. Upper. 
- Local: this_is_a_var. Lower
- Instance variable: _price.
- Private variable: __private_var

Function: get_name(), lower
