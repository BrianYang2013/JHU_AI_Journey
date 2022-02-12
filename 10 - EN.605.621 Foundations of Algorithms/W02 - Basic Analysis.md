# Lecture

## Elementary Data Structure Review

ADT

Dynamic Set: Search(S,k), Insert(S,p), Delete(S, p), Min(S), Max(S), Successor(S,p), Predecessor(S,p)

Stack, Queues, 

Graphs: Directed graphs, Transversing a Graph, Connectivity

Trees

## Functions

Sets

Relations: Reflexive, Symmetric, Transive, Equivalence, AntiSymmetry, Partial Orders. 

Function

Bijections: surjection, injection. 

## Proof by Induction

Elements of induction: Base case, The inductive step, Axiom of induction. 

## Divide and Conquer

Solving Recurrences

Methods for Solving Recurrences

Divide and Conquer

- Try to apply Master Theoream. Check restriction
- Generate a recursion tree for T(n)
- Use iteration method

Substitution method: 

- the bound is guessed and then mathematical induction is used to determine if the guess is correct.

- Guess, Verify, Solve
- Desire-residual

Recursion tree: 

- converts the recurrence into a tree whose nodes represent the cost incurred at various levels of the recursion
- Generate guess

Master Theorem: 

- provides bounds for recurrences of the form T(*n*) = *a*T(*n*/*b*) + *f*(*n*)
- $a \ge 1$, $b>1$ are constant
- f(n) is asymptotically positive
- n/b may not be an integer, but we ignore floors and ceilings
- Should be polynomially larger: $n$ vs $n lgn$ does not work. 

## Iteration Method

## Loop Invariants

- Initialization
- Maintenance
- Termination

## T(n) Examples

- $T(n) = 3T(n/4)+cn^2$,   $T(n)=\Theta(n^2)$
- Change the variables
  - $T(n)=2T(\sqrt n)+ \lg n$, $T(n)=O(\lg n \lg \lg n)$
- Master method
  - $T(n) = 9T(n/3) + n$,   $T(n)=\Theta(n^2)$
  - $T(n) = T(2n/3) + 1$,   $T(n)=\Theta(\lg n)$
  - $T(n) = 3T(n/4) + n \lg n$,   $T(n)=\Theta(n \lg n)$
  - 

