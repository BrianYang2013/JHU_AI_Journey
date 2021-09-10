# Module 2: Stacks

## Module 2A: Stacks Part 1

Stack: Ordered, LIFO. Deleted when pop. 



##  2.1 Stack abstract data type (ADT)

A **stack** is an ADT in which items are only inserted on or removed from the top of a stack. **Lastin-first-out.** 

Table 2.1.1: Common stack ADT operations.

| Operation        | Description                                      | Example starting with stack: 99, 77 (top is 99). |
| ---------------- | ------------------------------------------------ | ------------------------------------------------ |
| Push(stack, x)   | Inserts x on top of stack                        | Push(stack, 44). Stack: 44, 99, 77               |
| Pop(stack)       | Returns and removes item at top of stack         | Pop(stack) returns: 99. Stack: 77                |
| Peek(stack)      | Returns but does not remove item at top of stack | Peek(stack) returns 99. Stack still: 99, 77      |
| IsEmpty(stack)   | Returns true if stack has no items               | IsEmpty(stack) returns false.                    |
| GetLength(stack) | Returns the number of items in the stack         | GetLength(stack) returns 2.                      |

Q:

- An empty stack is indicated by a list head pointer value of (Null. It seems by default will assume it initialized to Null )
- StackPop returns list's head node. (F. Return the data, not node)

# Misc

- ++ i is faster than i++ back to the old day, when the variable put into the register. 

- If possible, theta is better than O. But lots of cases upper and lower are different. 
- $N \ge 1$, for Big-O and $\Omega$ (I don't  understand why people interested in tedious problem like this one)
- [A website for math notation](https://plantuml.com/ascii-math): After my practice in the last term, I found Latex is easier. 

