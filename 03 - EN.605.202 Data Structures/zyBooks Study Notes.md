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

Heuristic optimization

- knapsack problem：Package with total max weight, item with weight and value. Maximize value. 

- 0-1 knapsack problem: Qty of each item limited to 1

A **self-adjusting heuristic** is an algorithm that modifies a data structure based on how that data structure is used. Ex: Many self-adjusting data structures, such as red-black trees and AVL trees, use a self-adjusting heuristic to keep the tree balanced. Tree balancing organizes data to allow for faster access.

## 1.6 Relation between data structures and algorithms

Q: 

- Which of the following is **not** equal to the number of items in the topSales array? (Ok, read the question carefully)

## 1.7 Algorithm efficiency

**Algorithm efficiency** is typically measured by the algorithm's computational complexity. 

**Computational complexity** is the amount of resources used by the algorithm. The most common resources considered are the runtime and memory usage (may include others like network communication).

An algorithm's **runtime complexity** is a function, **T(N)**, that represents the number of constant time operations performed by the algorithm on an input of size N. : Because an algorithm's runtime may vary significantly based on the input data, a common approach is to identify **best** and **worst** case scenarios. Input data size must remain a variable. 

An algorithm's **space complexity** is a function, **S(N)**, that represents the number of fixed-size memory units used by the algorithm for an input of size N. S(N) = f(N) + k

An algorithm's **auxiliary space complexity** is the space complexity not including the input data.

Q: 

- Computational complexity analysis allows the efficiency of algorithms to be compared.(T, no trap)
- The linear search algorithm's best case scenario is when N = 0. (F, N is variable)

## 1.8 Constant time operations

A **constant time operation** is an operation that, for a given processor, always operates in the same amount of time, regardless of input values. Loop might vary if loop length is a variable. 

Table 1.8.1: Common constant time operations.

| Operation                                                    | Example                                    |
| ------------------------------------------------------------ | ------------------------------------------ |
| Addition, subtraction, multiplication, and division of fixed size integer or floating point values. | `w = 10.4 x = 3.4 y = 2.0 z = (w - x) / y` |
| Assignment of a reference, pointer, or other fixed size data value. | `x = 1000 y = x a = true b = a`            |
| Comparison of two fixed size data values.                    | `a = 100 b = 200 if (b > a) {   ... }`     |
| Read or write an array element at a particular index.        | `x = arr[index] arr[index + 1] = x + 1`    |

Q:

- The 3 constant time operations in the code below can collectively be considered 1 constant time operation.(T, no trap)

- In the code below, suppose str1 is a pointer or reference to a string. The code only executes in constant time if the assignment copies the pointer/reference, and not all the characters in the string. (T. So on the other hand, if copy all characters then it might varies. )

  ```
  str2 = str1
  ```

- The hardware running the code is the only thing that affects what is and what is not a constant time operation. (F. The programming language also affects what is a constant time operation. Ex: A programming language could provide variable size floating point values as the only available numerical type and implement arithmetic operations in software. Since the values are not fixed size, arithmetic operations would not be constant time.)

## 1.9 Growth of functions and complexity

- **Lower bound**: A function f(N) that is ≤ the best case T(N), for all values of N ≥ 1. T(N)=3N+6, then 3N or 3N+6. 
- **Upper bound**: A function f(N) that is ≥ the worst case T(N), for all values of N ≥ 1. T(N)=5N^2+7N, then 12N^2 or 5N^2+7N
- **Asymptotic notation** is the classification of runtime complexity that uses functions that indicate only the growth rate of a bounding function.

Table 1.9.1: Notations for algorithm complexity analysis.

| Notation | General form | Meaning                                                      |
| -------- | ------------ | ------------------------------------------------------------ |
| O        | T(N)=O(f(N)) | A positive constant c exists such that, for all N ≥ 1, T(N)≤c∗f(N). |
| Ω        | T(N)=Ω(f(N)) | A positive constant c exists such that, for all N ≥ 1, T(N)≥c∗f(N). |
| Θ        | T(N)=Θ(f(N)) | T(N)=O(f(N)) and T(N)=Ω(f(N)).                               |

$T(N) = 2N^2+N+9$

$O(N) = N^2$ or $N^3$		$Ω(N) = N^2$		$Θ(N) = N^2$

## 1.10 O notation

**Big O notation** is a mathematical way of describing how a function (running time of an algorithm) generally behaves in relation to the input size. In Big O notation, all functions that have the same growth rate (as determined by the highest order term of the function) are characterized using the same Big O notation. In essence, all functions that have the same growth rate are considered equivalent in Big O notation. Rules:

1. If f(N) is a sum of several terms, the highest order term (the one with the fastest growth rate) is kept and others are discarded.
2. If f(N) has a term that is a product of several factors, all constants (those that are not in terms of N) are omitted.

Figure 1.10.1: Rules for determining Big O notation of composite functions.

| Composite function | Big O notation |
| ------------------ | -------------- |
| c · O(f(N))        | O(f(N))        |
| c + O(f(N))        | O(f(N))        |
| g(N) · O(f(N))     | O(g(N) · f(N)) |
| g(N) + O(f(N))     | O(g(N) + f(N)) |

Table 1.10.1: Growth rates for different input sizes.

| Function  | N = 10 | N = 50     | N = 100      | N = 1000 | N = 10000  | N = 100000 |
| --------- | ------ | ---------- | ------------ | -------- | ---------- | ---------- |
| $log_2N$  | 3.3 μs | 5.65 μs    | 6.6 μs       | 9.9 μs   | 13.3 μs    | 16.6 μs    |
| N         | 10 μs  | 50 μs      | 100 μs       | 1000 μs  | 10 ms      | 100 ms     |
| $Nlog_2N$ | .03 ms | .28 ms     | .66 ms       | .099 s   | .132 s     | 1.66 s     |
| $N^2$     | .1 ms  | 2.5 ms     | 10 ms        | 1 s      | 100 s      | 2.7 hours  |
| $N^3$     | 1 ms   | .125 s     | 1 s          | 16.7 min | 11.57 days | 31.7 years |
| $2^N$     | .001 s | 35.7 years | > 1000 years |          |            |            |



Figure 1.10.2: Runtime complexities for various code examples.

| Notation   | Name         | [Example pseudocode](./Pseudocode.md#1.10.2: Runtime complexities) |
| ---------- | ------------ | ------------------------------------------------------------ |
| O(1)       | Constant     | `FindMin(x, y) `                                             |
| O(log N)   | Logarithmic  | `BinarySearch(numbers, N, key) `                             |
| O(N)       | Linear       | `LinearSearch(numbers, numbersSize, key)`                    |
| O(N log N) | Linearithmic | `MergeSort(numbers, i, k)`                                   |
| O(N2)      | Quadratic    | `SelectionSort(numbers, numbersSize) `                       |
| O(cN)      | Exponential  | `Fibonacci(N) `                                              |

Q: 

- $3·N · O(N^2) = O(N^3)$
- $log_2N = O(logN)$

## 1.11 Algorithm analysis

Runtime analysis determines the total number of operations. 

Algorithm runtime analysis often focuses on the **worst-case runtime** complexity.  Other runtime analyses include best-case runtime and average-case runtime. Determining the average-case runtime requires knowledge of the statistical properties of the expected data inputs.



- $f(N)=4N+3=O(N)$

- i = 0 execute once. Constant +1
- In the final loop, i < N will be executed. Constant +1

```
maxVal = numbers[0]
for (i = 0; i < N; ++i) {
   if (numbers[i] > maxVal) {
      maxVal = numbers[i]
   }
}
```



Q

- What is the **big-O notation** for the worst-case runtime? (f(N)=2+4N+1 is not correct. O(N))