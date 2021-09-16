# Module 3 - Recursion

## Lecture

## 3.1 Recursion: Introduction, Functions, Definitions

A **recursive algorithm** is an algorithm that breaks the problem into smaller subproblems and applies the same algorithm to solve the smaller subproblems.

A function that calls itself is known as a **recursive function**

**base case**: A case where a recursive algorithm completes without applying itself to a smaller subproblem.

## 3.4 Creating a recursive function

Creating a recursive function can be accomplished in two steps.

- ***Write base case*** -- Every recursive function must have a case that returns a value without performing a recursive call. That case is called the **base case**. A programmer may write that part of the function first, and then test. There may be **multiple** base cases.
- ***Write recursive case*** -- The programmer then adds the recursive case to the function.
- Outer function: check for a valid input value. For example: "factorial(n)".
- Inner function: For recursion. Such as " _factorial(n)"

Recursive VS Loop

- In general, any recursive solution can also be done using loops. However, in some cases using a recursive algorithm may make a solution more clear, concise, and understandable.
- A recursive solution is not better than a non-recursive solution that simply uses a loop. Loop is more intuitive and maybe faster. 
- We might store the middle result to improve the performance. 

Common error

- Not cover all possible base cases in a recursive function. 
- Write a recursive function that doesn't always reach a base case. 



Q: If an alphabetically sorted list (ascending) has elements numbered 0 to 50, and the item at element 0 is "Bananas", how many recursive calls to find() will be made during the failed search for "Apples"? (7) 

### 3.6 Analyzing the time complexity of recursive algorithms

**Recurrence relation**: A function f(N) that is defined in terms of the same function operating on a value < N. Ex: Binary search performs constant time operations, then a recursive call that operates on half of the input, making the runtime complexity T(N) = O(1) + T(N / 2). => have T at both side. 

**Recursion tree**: A visual diagram of an operation done by a recursive function, that separates operations done directly by the function and operations done by recursive calls.

Interesting idea on mid-1 and mid+1

- Because mid has already been checked, it need not be part of the new window, so mid+1 rather than mid can be used for the window's new low side, or mid-1 for the window's new high side. 
- But the mid-1 can have the drawback of a non-intuitive base case (i.e., mid < low, because if the current window is say 4..5, mid is 4, so the new window would be 4..4-1, or 4..3). We believe range==1 is more intuitive, and thus use mid rather than mid-1. 
- However, we still have to use mid+1 when searching higher, due to integer rounding. In particular, for window 99..100, mid is 99 ((99+100)//2=99.5, rounded to 99 due to truncation of the fraction). So the next window would again be 99..100, and the algorithm would repeat with this window forever. mid+1 prevents the problem, and doesn't miss any numbers because mid was checked and thus need not be part of the window.

### 3.8 Adding output statements for debugging

W03 Recursive findname.py

More advanced techniques for handling debug output exist too, such as the *[logging](http://docs.python.org/3/library/logging.html)* Python standard library



3.9 Recursive exploration of all possibilities
3.10 Greedy algorithms - Optional
3.11 Dynamic programming - Optional