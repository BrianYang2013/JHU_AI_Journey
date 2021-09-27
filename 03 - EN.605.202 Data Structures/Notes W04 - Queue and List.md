# Module 4 - Queue and List

## Course Module

### Lecture

ADT Queue: No limit on number. No limit on nature of items. 

Array Implementation 

- Pro: Random access
- Cons: Homogeneous. Size limit
- Ok: Need front and rear pointers

- Imp 1, Regular: Empty space in front get wasted. false overflow
- Imp 2, Move after delete: Delete become O(n)
- Imp 3, Move rear pointer to the front open space: Can not tell full or empty status. => Keep a length variable in privacy section. 

Linked: 

- Pro: No size limit
- Cons: Homogeneous. Sequence access
- Ok: Need front and rear pointers



List: No limit on number. No limit on nature of items. Not all list sorted. Duplicates might need to consider, how to define and safely process them. List copy should be deep copy

Array

- Pros: Random access. Insert and delete: O(n/2)

- Cons: Limited size

- Ok: Homogenous
- Alternative: Flag value to avoid shifting.  Flag field. Shift will be reduced, << O(n/2), but can not use random access. Garbage collection is a standard process, to remove the flag value / field. 

Link

- Pros: No size limit. 

- Cons: Sequence access, no random access. 

- Ok: Homogenous
- 

### Office Hour





### 4.1 Queue abstract data type (ADT)

A **queue** is an ADT in which items are inserted at the end of the queue and removed from the front of the queue. 

The queue **enqueue**operation inserts an item at the end of the queue.

The queue **dequeue** operation removes and returns the item at the front of the queue. 

Table 4.1.1: Some common operations for a queue ADT.

| Operation         | Description                                                | Example starting with queue: 43, 12, 77 (front is 43) |
| ----------------- | ---------------------------------------------------------- | ----------------------------------------------------- |
| Enqueue(queue, x) | Inserts x at end of the queue                              | Enqueue(queue, 56). Queue: 43, 12, 77, 56             |
| Dequeue(queue)    | Returns and removes item at front of queue                 | Dequeue(queue) returns: 43. Queue: 12, 77             |
| Peek(queue)       | Returns but does not remove item at the front of the queue | Peek(queue) return 43. Queue: 43, 12, 77              |
| IsEmpty(queue)    | Returns true if queue has no items                         | IsEmpty(queue) returns false.                         |
| GetLength(queue)  | Returns the number of items in the queue                   | GetLength(queue) returns 3.                           |

Note: Dequeue and Peek operations should not be applied to an empty queue; the resulting behavior may be undefined.

### 4.2 Queues using linked lists

### 4.3 List data structure

Implementing a linked list using two data structures: 

1. **List data structure**: A list data structure is a data structure containing the list's head and tail, and may also include additional information, such as the list's size.
2. **List node data structure**: The list node data structure maintains the data for each list element, including the element's data and pointers to the other list element.

### 4.4 List abstract data type (ADT)

A **list** is a common ADT for holding ordered data, having operations like append a data item, remove a data item, search whether a data item exists, and print the list

Table 4.4.1: Some common operations for a list ADT.

| Operation               | Description                              | Example starting with list: 99, 77                           |
| ----------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| Append(list, x)         | Inserts x at end of list                 | Append(list, 44), list: 99, 77, 44                           |
| Prepend(list, x)        | Inserts x at start of list               | Prepend(list, 44), list: 44, 99, 77                          |
| InsertAfter(list, w, x) | Inserts x after w ?? **Index or data**?? | InsertAfter(list, 99, 44), list: 99, 44, 77                  |
| Remove(list, x)         | Removes x                                | Remove(list, 77), list: 99                                   |
| Search(list, x)         | Returns item if found, else returns null | Search(list, 99), returns item 99 Search(list, 22), returns null |
| Print(list)             | Prints list's items in order             | Print(list) outputs: 99, 77                                  |
| PrintReverse(list)      | Prints list's items in reverse order     | PrintReverse(list) outputs: 77, 99                           |
| Sort(list)              | Sorts the lists items in ascending order | list becomes: 77, 99                                         |
| IsEmpty(list)           | Returns true if list has no items        | For list 99, 77, IsEmpty(list) returns false                 |
| GetLength(list)         | Returns the number of items in the list  | GetLength(list) returns 2                                    |

### 4.5 Array-based lists

An **array-based list** is a list ADT implemented using an array. => Check size first!

The **Prepend** operation for an array-based list inserts a new item at the start of the list. O(N)

The **InsertAfter** operation for an array-based list inserts a new item after a specified index. O(1) to O(N)

Optional: Array-based lists often support the **InsertAt** operation, which inserts an item at a specified index. Inserting an item at a desired index X can be achieved by using InsertAfter to insert after index X - 1.

Given a key, the **search** operation returns the index for the first element whose data matches that key, or -1 if not found. O(1) to O(N)

Given the index of an item in an array-based list, the **remove-at** operation removes the item at that index. When removing an item at index X, each item after index X is moved down by 1 position. O(1) to O(N)

### 4.6 Singly-linked lists

A **singly-linked list** is a data structure for implementing a list ADT, where each node has data and a pointer to the next node. 

The list structure typically has pointers to the list's first node and last node. A singly-linked list's first node is called the **head**, and the last node the **tail**. 

**InsertAfter** 

- *Insert as list's first node:* If the list's head pointer is null, the algorithm points the list's head and tail pointers to the new node. 
- *Insert after list's tail node:* If the list's head pointer is not null (list not empty) and curNode points to the list's tail node, the algorithm points the tail node's next pointer and the list's tail pointer to the new node.
- *Insert in middle of list:* If the list's head pointer is not null (list not empty) and curNode does not point to the list's tail node, the algorithm points the new node's next pointer to curNode's next node, and then points curNode's next pointer to the new node.

**RemoveAfter**

- *Remove list's head node (special case):* If curNode is null, the algorithm points sucNode to the head node's next node, and points the list's head pointer to sucNode. If sucNode is null, the only list node was removed, so the list's tail pointer is pointed to null (indicating the list is now empty).
- *Remove node after curNode:* If curNode's next pointer is not null (a node after curNode exists), the algorithm points sucNode to the node after curNode's next node. Then curNode's next pointer is pointed to sucNode. If sucNode is null, the list's tail node was removed, so the algorithm points the list's tail pointer to curNode (the new tail node).



### 4.9 Linked list

A **list traversal** algorithm visits all nodes in the list once and performs an operation on each node. A common traversal operation prints all list nodes. 

Doubly linked: Reverse traversal

Given a key, a **search** algorithm returns the first node whose data matches that key, or returns null if a matching node was not found. 

### 4.11 Linked lists: Recursion

ListTraverseRecursive: 10 nodes, 11 calls. 

Forward traversal visits a node first, then recursively traverses the remainder of the list. If the order is swapped, such that the recursive call is made first, the list is traversed in reverse order.ß

### 4.12 Deque abstract data type (ADT)

A **deque** (pronounced "deck" and short for double-ended queue) is an ADT in which items can be inserted and removed at both the front and back. 

Table 4.12.1: Common deque ADT operations.

| Operation           | Description                                                | Example starting with deque: 59, 63, 19 (front is 59)   |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------------------- |
| PushFront(deque, x) | Inserts x at the front of the deque                        | PushFront(deque, 41). Deque: 41, 59, 63, 19             |
| PushBack(deque, x)  | Inserts x at the back of the deque                         | PushBack(deque, 41). Deque: 59, 63, 19, 41              |
| PopFront(deque)     | Returns and removes item at front of deque                 | PopFront(deque) returns 59. Deque: 63, 19               |
| PopBack(deque)      | Returns and removes item at back of deque                  | PopBack(deque) returns 19. Deque: 59, 63                |
| PeekFront(deque)    | Returns but does not remove the item at the front of deque | PeekFront(deque) returns 59. Deque is still: 59, 63, 19 |
| PeekBack(deque)     | Returns but does not remove the item at the back of deque  | PeekBack(deque) returns 19. Deque is still: 59, 63, 19  |
| IsEmpty(deque)      | Returns true if the deque is empty                         | IsEmpty(deque) returns false.                           |
| GetLength(deque)    | Returns the number of items in the deque                   | GetLength(deque) returns 3.                             |