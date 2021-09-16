# Module 2: Stacks

## Module 2A: Stacks Part 1

Stack: 

- Ordered, LIFO. Deleted when pop. 
- Homework: Push and Pop are standard opereation, Is_Empty is not. 
- Lectures: Push, Pop, Is_Empty, constructor are standard opereation. Peek and ClearStack are optional. 

infix, prefix, postfix

- **Ordre of the number won't change.** 
- $ will be used for exponential, instead of functin or ^, **
- General rule for same precedence. Exception: $ Process right to left. 
  - 2 \$ 3\$2 = 2 \$ (3 \$2) = 2^9 = 512. Not (2\$3)\$2 =8^2=64
  - $A \$_1B\$_2C = ABC\$_2\$_1$
- **Evaluate** 
  - Operand push in. Operator, pop 2 and evaluate. 
  - Postfix: Read from Left. B op A. Older items on stack are further to the left. 
  - Prefix: Read from right. A op B. Older items on stack are further to the right. 
- Infix to postfix rule: 
  - Process from **left** to right
  - Parentheses require special handling. Still within precedence rules
  - Pseducode:
    - Operand, output. 
    - Operator, compare with stack top. **higher push in**, lower or equal pop/push in. 
    - End: pop. 
    - Treat ( ) conceptually as separate problem

- Inflix to prefix rule
  - Process inflix string from **right** to left
  - Pseducode
    - Operand, output to the left
    - Operator, compare with stack top. **higher push in**, lower or equal pop/push lower operand. 
    - End: pop. 
    - Treat ( ) conceptually as separate problem

Quick Reference: 

| **Read**     | **Stack**  | **Action** (infix to prefix, from right to left)     |
| ------------ | ---------- | ---------------------------------------------------- |
| **Operand**  |            | Output (from right to left)                          |
| **Operator** | > Top      | Push. Also for empty                                 |
| **Operator** | <=Top      | Pop top operator and push in                         |
| **)**        |            | Push                                                 |
| **(**        | Pop till ) | Output operator between ( ), with top-down sequence. |
| **END**      |            | Pop all                                              |



| Read         | Stack      | Action (infix to postfix, from left to right)               |
| ------------ | ---------- | ----------------------------------------------------------- |
| **(**        |            | Push                                                        |
| **Operand**  |            | Output                                                      |
| **Operator** | <=Top      | Pop top operator and push in (=: left-to-right associative) |
| **Operator** | >Top       | Push. Also for empty                                        |
| **)**        | Pop till ( | Output operator between ( ), with top-down sequence.        |

Stack Implementation

- Overflow (insert into a full stack) and Underflow (delete from an empty stack)
- Array: 
  - Pro: Random access
  - Cons: Limited size(static). Requires homogeneous, 
  - Need a Top pointer and Array for data
- Linked Array
  - Pro: No size limits (dynamic)
  - Cons: Sequence access(only care top, not a big problem). Require homogeneous
  - Need Top pointer. 

Deep copy

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

## 2.2 Stacks using linked lists

# Misc

- ++ i is faster than i++ back to the old day, when the variable put into the register. 

- If possible, theta is better than O. But lots of cases upper and lower are different. 
- $N \ge 1$, for Big-O and $\Omega$ (I don't  understand why people interested in tedious problem like this one)
- [A website for math notation](https://plantuml.com/ascii-math): After my practice in the last term, I found Latex is easier. 

