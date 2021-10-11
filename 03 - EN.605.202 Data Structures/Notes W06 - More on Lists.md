# Module 6 - More on Lists: List Variations, Hybrid Implementation, Graphs

## Course Module

### Lecture

Circular list: Josephus problem. 

List example: 

- Very large integers Addition: Circular list

- Very long integers substraction: Double linked list (maybe an extra space to record the borrow 1? Less complexity)
- Polynomial arithmetic
- Sparse matrix: Multi-linked lists. circular, double linked. 

Implementation

- Linked 

- Dynamic - stacks queues and lists
- Hybrid: 
  - Info + next (position)
  - Free list (pop to provide an empty space and Push to recycle)



ADT: Logic

- List
- Stack
- Queue
- Deque
- PQueue
- Set
- Tree
- Graph

Data Structure: Implementation

- Array
- Linked list - Single
- Linked list - Circular
- Linked list - Double
- Linked list - Multiply
- Hybrid

Methods:

- Insert
- Delete
- Search
- Copy
- Print
- Peek

## ZyBooks

### 5.1 Doubly-linked lists

A **doubly-linked list** is a data structure for implementing a list ADT, where each node has data, a pointer to the next node, and a pointer to the previous node. 

A doubly-linked list is a type of **positional list**: A list where elements contain pointers to the next and/or previous elements in the list.

**Append**: To the end

**Prepend**: append to the head

**InsertAfter**: inserts the new node after a provided existing list node. curNode is a pointer to an existing list node.

**Remove** operation for a doubly-linked list removes a provided existing list node. **curNode** is a pointer to an existing list node. The variable **sucNode** points to the node's successor, and the variable **predNode** points to the node's predecessor. 

A linked list implementation may use a **dummy node** (or **header node**): A node with an unused data member that always resides at the head of the list and cannot be removed. Using a dummy node simplifies the algorithms for a linked list because the head and tail pointers are never null.

**Dummy Node:** One(head) or Two (head and tail) will simplify corner cases. 

### 5.5 Circular lists

A **circular linked list** is a linked list where the tail node's next pointer points to the head of the list, instead of null. A circular linked list can be used to represent repeating processes. The head of a circular linked list is often referred to as the ***start*** node.

A traversal through a circular linked list is similar to traversal through a standard linked list, but must terminate after reaching the head node a second time, as opposed to terminating when reaching null.

### 5.6 Priority queue abstract data type (ADT)

A **priority queue** is a queue where each item has a priority, and items with higher priority are closer to the front of the queue than items with lower priority. The priority queue **enqueue** operation inserts an item such that the item is closer to the front than all items of lower priority, and closer to the end than all items of equal or higher priority. The priority queue **dequeue** operation removes and returns the item at the front of the queue, which has the highest priority.

When enqueueing items of equal priority, the first-in-first-out rules apply.

A **peek** operation returns the highest priority item, without removing the item from the front of the queue.

Table 5.6.1: Common priority queue ADT operations.

| Operation          | Description                                                 | Example starting with priority queue: 42, 61, 98 (front is 42) |
| ------------------ | ----------------------------------------------------------- | ------------------------------------------------------------ |
| Enqueue(PQueue, x) | Inserts x after all equal or higher priority items          | Enqueue(PQueue, 87). PQueue: 42, 61, 87, 98                  |
| Dequeue(PQueue)    | Returns and removes the item at the front of PQueue         | Dequeue(PQueue) returns 42. PQueue: 61, 98                   |
| Peek(PQueue)       | Returns but does not remove the item at the front of PQueue | Peek(PQueue) returns 42. PQueue: 42, 61, 98                  |
| IsEmpty(PQueue)    | Returns true if PQueue has no items                         | IsEmpty(PQueue) returns false.                               |
| GetLength(PQueue)  | Returns the number of items in PQueue                       | GetLength(PQueue) returns 3.                                 |

A priority queue may also be implemented such that all priorities are specified during a call to **EnqueueWithPriority**: An enqueue operation that includes an argument for the enqueued item's priority.

A priority queue is commonly implemented using a **heap**. A heap will keep the highest priority item in the root node and allow access in O(1) time. Adding and removing items from the queue will operate in worst-case $O(logN)$ time.

Table 5.6.2: Implementing priority queues with heaps.

| Priority queue operation | Heap functionality used to implement operation               | Worst-case runtime complexity |
| ------------------------ | ------------------------------------------------------------ | ----------------------------- |
| Enqueue                  | Insert                                                       | O(logN)                       |
| Dequeue                  | Remove                                                       | **O(logN)**                   |
| Peek                     | Return value in root node                                    | **O(1)**                      |
| IsEmpty                  | Return true if no nodes in heap, false otherwise             | O(1)                          |
| GetLength                | Return number of nodes (expected to be stored in the heap's member data) | O(1)                          |

### Optional - Set

A **set** is a collection of distinct elements. A set **add** operation adds an element to the set, provided an equal element doesn't already exist in the set. A set is an unordered collection. 

When storing objects, set implementations commonly distinguish elements based on an element's **key value**: A primitive data value that serves as a unique identifier for the element. 

Given a key, a set **search** operation returns the set element with the specified key, or null if no such element exists. The search operation can be used to implement a subset test. A set X is a **subset** of set Y only if every element of X is also an element of Y.

Set operations: **Union**, **intersection**, and **difference**

A **filter** operation on set X produces a subset containing only elements from X that satisfy a particular condition. The condition for filtering is commonly represented by a **filter predicate**: A function that takes an element as an argument and returns a Boolean value indicating whether or not that element will be in the filtered subset.

A **map** operation on set X produces a new set by applying some function F to each element. Ex: If X = {18, 44, 38, 6} and F is a function that divides a value by 2, then SetMap(X, F) = { 9, 22, 19, 3 }.

A **dynamic set** is a set that can change after being constructed. A **static set** is a set that doesn't change after being constructed. 

Table 5.9.1: Static and dynamic set operations.

| Operation                                | Dynamic set support? | Static set support? |
| ---------------------------------------- | -------------------- | ------------------- |
| Construction from a collection of values | Yes                  | Yes                 |
| Count number of elements                 | Yes                  | Yes                 |
| Search                                   | Yes                  | Yes                 |
| Add element                              | Yes                  | No                  |
| Remove element                           | Yes                  | No                  |
| Union (returns new set)                  | Yes                  | Yes                 |
| Intersection (returns new set)           | Yes                  | Yes                 |
| Difference (returns new set)             | Yes                  | Yes                 |
| Filter (returns new set)                 | Yes                  | Yes                 |
| Map (returns new set)                    | Yes                  | Yes                 |
