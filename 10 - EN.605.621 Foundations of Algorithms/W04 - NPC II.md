# Lecture

P: Solve in polynomial time

NP: Verify in polynomial time

## 3-CNF-SAT

3-CNF Satisfiability

- Literal
- Boolean formula
- CNF, Conjunctive normal form
- 3-CNF: 3-conjunctive normal form

3-CNF Satisfiability is NPC

- SAT parse tree
- Truth table
- DNF to CNF conversion

## The Hamiltonian Cycle Problem

## Bayesian Network Inference

More in course: AI / Reasoning under uncertainty

Definition: A bayesian network is a directed acyclic graph, 

- vertices correspond to random variables, 
- directed edge correspondence conditional dependence or casual relationships between variables, 
- each vertex has an associated conditional probability distribution (CPD), defined as $P(x_i|Pa(x_i))$, where $Pa(x_i)$ identifies the "parents" of vertex $x_i$. 

BN-Pr-DP is NP-complete. (via 3-CNF-SAT)

## Famous NP-Complete Problems

## An interesting source of information on NP optimization problems

[A compendium of NP optimization problems](https://www.csc.kth.se/~viggo/problemlist/)

Editors: Pierluigi Crescenzi, and Viggo Kann Subeditors: Magnús Halldórsson (retired), Marek Karpinski, Gerhard Woeginger

## Pseudo-Polynomial Time Problems

A pseudo-polynomial-time algorithm... will display ’exponential behavior’ only when confronted with instances containing ’exponentially large’ numbers, [which] might be rare for the application we are interested in. If so, this type of algorithm might serve our purposes almost as well as a polynomial time algorithm.

## The Polynomial Hierarchy

NP, co-NP and PSPACE

Satisfiability problems: SAT is NPC

Hierarchy, The polynomial hierarchy

## Homework 2

[Pumping Lemma](https://www2.lawrence.edu/fast/GREGGJ/CMSC515/chapt01/Pumping.html)

[Context Free Grammars](https://www2.lawrence.edu/fast/GREGGJ/CMSC515/chapt02/CFG.html)





