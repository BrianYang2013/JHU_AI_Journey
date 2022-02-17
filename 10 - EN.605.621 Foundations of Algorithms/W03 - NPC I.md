# Lecture

## The Complexity Zoo

[Complexity Zoo](https://complexityzoo.net/Complexity_Zoo)

[Deterministic Turing Machine](https://complexityzoo.net/Petting_Zoo#Deterministic_Turing_Machine)

- Turing machine: Abstract model of a computer with: 
  - internal state
  - infinite length tape
  - Read/write head, move left or right

## Decidability

optimization problems -> decision problems

Semi-decidable problem: does there exist a Turing machine that can determine any other Turning machine will halt? This is called the halting problem, and it has been proven that no such Turing machine exists.



## Formal Langages

Regular Languages: A regular language is a language $L$ such that there exists a deterministic finite automaton (DFA) that accepts the language.

- Left linear, right linear. 

Context Free Grammars: 

## The Chomsky Hierarchy

- Typo 0 languages: unrestricted grammars. type 0 grammars generate all languages that can be recognized by a Turing machine.
- Type 1 languages: These correspond to the set of context sensitive languages and correspond to those languages that can be recognized by a Turing machine with a bounded tape.
- Type 2 languages: These are the context free languages as defined previously.
- Type 3 languages: These are the regular languages as defined previously.

| Type | Grammar           | Language     | Automate       |
| ---- | ----------------- | ------------ | -------------- |
| 3    | Finite State      | Regular      | Finite         |
| 2    | Context-Free      | C-F          | Pushdown       |
| 1    | Context-Sensitive | C-S          | Linear bounded |
| 0    | General rewrite   | Unrestricted | Turing machine |

## Cook's Theorem

Satisfiability Problem, SAT, is NP-Complete. 

Proof:

- in NP: Choose the satisfiable assignment (certificate) and verify
- Reduce SAT to a language problem. 

## Nondeterminacy and Formal Derivation of Programs

[Nondeterminacy and Formal Derivation of Programs](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.90.97&rep=rep1&type=pdf), Edsger W. Dijkstra, Burroughs Corporation, Communications fo the ACM, August 1975, Volume 18, Number 8, Pages 453-457.

## 520S  Lecture Notes Chapter 34

To be update



## Wrap up

- Deterministic Turing Machines
  - A finite state control
  - A tape consisting of a two-way sequence of tape squares
  - A read-write head
- DTM manipulated through the execution of a program by
  - A finite set $Γ$ of symbols
  - A finite set Q of states ($q_0$ as start and $q_Y$ and $q_N$ as halting states)
  - A transition function  δ:(Q− {qY,qN})×Γ → Q×Γ×{+1,−1}.
- Computability
- Complexity Classes
  - P: solvable on a deterministic Turing machine in polynomial time.
  - NP: solvable on a nondeterministic Turing machine in polynomial time.
  - co-NP: languages L such that the complement of L is in NP.
  - Possible 4 situations
  - Decidability
- Formal Languages
  - Regular Languages
  - Context Free Grammars
  - The Chomsky Hierarchy
- NPC