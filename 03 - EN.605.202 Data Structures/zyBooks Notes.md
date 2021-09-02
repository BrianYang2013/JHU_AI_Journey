# Module 1 - Complexity and ADTs

## 1.1 Data structures

Choosing the best data structure often requires determining which data structure provides a good balance given expected uses. Ex: If a program requires fast insertion of new data, 

- Insert: Linked list > array.

Data Structure: 

| Data structure | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| Record         | A **record** is the data structure that stores subitems, often called fields, with a name associated with each subitem. |
| Array          | An **array** is a data structure that stores an ordered list of items, where each item is directly accessible by a positional index. |
| Linked list    | A **linked list** is a data structure that stores an ordered list of items in nodes, where each node stores data and has a pointer to the next node. |
| Binary tree    | A **binary tree** is a data structure in which each node stores data and has up to two children, known as a left child and a right child. |
| Hash table     | A **hash table** is a data structure that stores unordered items by mapping (or hashing) each item to a location in an array. |
| Heap           | A **max-heap** is a tree that maintains the simple property that a node's key is greater than or equal to the node's childrens' keys. A **min-heap** is a tree that maintains the simple property that a node's key is less than or equal to the node's childrens' keys. |
| Graph          | A **graph** is a data structure for representing connections among items, and consists of vertices connected by edges. A **vertex** represents an item in a graph. An **edge** represents a connection between two vertices in a graph. |

Q

- A linked list stores items in an unspecified order.(F)
- A list node's data can store a record with multiple subitems.(T. Name, title, salary ...)
- Inserting an item at the **end** of a 999-item array requires how many items to be shifted? (0)



## 1.2 Abstract data types

An ADT can be implemented using different underlying data structures. 

Common ADTs.

| ADT              | Description                                                  | Common underlying data structures |
| ---------------- | ------------------------------------------------------------ | --------------------------------- |
| List             | A **list** is an ADT for holding ordered data.               | Array, linked list                |
| Dynamic array    | A **dynamic array** is an ADT for holding ordered data and allowing indexed access. | Array                             |
| Stack            | A **stack** is an ADT in which items are only inserted on or removed from the top of a stack. | Linked list                       |
| Queue            | A **queue** is an ADT in which items are inserted at the end of the queue and removed from the front of the queue. | Linked list                       |
| Deque            | A **deque** (pronounced "deck" and short for double-ended queue) is an ADT in which items can be inserted and removed at both the front and back. | Linked list                       |
| Bag              | A **bag** is an ADT for storing items in which the order does not matter and duplicate items are allowed. | Array, linked list                |
| Set              | A **set** is an ADT for a collection of distinct items.      | Binary search tree, hash table    |
| Priority queue   | A **priority queue** is a queue where each item has a priority, and items with higher priority are closer to the front of the queue than items with lower priority. | Heap                              |
| Dictionary (Map) | A **dictionary** is an ADT that associates (or maps) keys with values. | Hash table, binary search tree    |

Q:

- A list ADT's underlying data structure has no impact on the program's execution.(F. Runtime)

## 1.3 Applications of ADTs

Knowledge of the underlying implementation is needed to analyze or improve the runtime efficiency.

Standard libraries in various programming languages.

| Programming language | Library                          | Common supported ADTs                       |
| -------------------- | -------------------------------- | ------------------------------------------- |
| Python               | Python standard library          | list, set, dict, deque                      |
| C++                  | Standard template library (STL)  | vector, list, deque, queue, stack, set, map |
| Java                 | Java collections framework (JCF) | Collection, Set, List, Map, Queue, Deque    |

## 1.4 Introduction to algorithms

An **algorithm** describes a sequence of steps to solve a computational problem or perform a calculation. An algorithm can be described in English, pseudocode, a programming language, hardware, etc. 

A **computational problem** specifies an input, a question about the input that can be answered using a computer, and the desired output.

Algorithm efficiency is most commonly measured by the **algorithm runtime**, and an efficient algorithm is one whose runtime increases no more than **polynomially** with respect to the input size. 

**NP-complete** problems are a set of problems(computational) for which no known efficient algorithm exists (Focus on finding a good, but non-optimal, solution.). For example, clique decision problem. NP-complete problems have the following characteristics:

- No efficient algorithm has been found to solve an NP-complete problem.
- No one has proven that an efficient algorithm to solve an NP-complete problem is impossible. 
- If an efficient algorithm exists for one NP-complete problem, then all NP-complete problems can be solved efficiently.



Q: 

- An algorithm with a polynomial runtime is considered efficient.(T. So even one order higher still consieer efficient? )
- An efficient algorithm exists for all computational problems.(F)
- An efficient algorithm to solve an NP-complete problem may exist.(T)

## 1.5 Heuristics

**Heuristic**: A technique that willingly accepts a non-optimal or less accurate solution in order to improve execution speed.

knapsack problem. 

0-1 knapsack problem: Qty of each item limited to 1



## 1.6 Relation between data structures and algorithms

## 1.7 Algorithm efficiency



## 1.8 Constant time operations



## 1.9 Growth of functions and complexity



## 1.10 O notation

## 1.11 Algorithm analysis