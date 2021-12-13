# Module 12 - Searching

## Course Module

### Summary

Linear Search - Average $N/2$, or $O(N)$

Binary search - $⌊log2N⌋+1$

B trees:

- All keys in a B-tree must be distinct.
- **All leaf nodes must be at the same level.**
- An internal node with N keys must have N+1 children. 
- Keys in a node are stored in sorted order from smallest to largest.
- Each key in a B-tree internal node has one left subtree and one right subtree. All left subtree keys are < that key, and all right subtree keys are > that key.
- A B-Tree is defined by the term *minimum degree* ‘t’. The value of t depends upon disk block size.
- Every node except root must contain at least t-1 keys. The root may contain minimum 1 key.
- All nodes (including root) may contain at most 2*t – 1 keys.
- Number of children of a node is equal to the number of keys in it plus 1.
- B-Tree grows and shrinks from the root which is unlike Binary Search Tree. Binary Search Trees grow downward and also shrink from downward.
- Assume too big for memory. Better for disk. Node size equal to the disk block size. 

2-3-4 Tree

- Search
- **Split** the full node (3 keys) during insertion traversal. Preemptive split to make sure parent node has room for middle value from the child. 
- Rotation: After remove we might need rotation. 
- Fusion: May need fusion before rotation to make sure we hae sibling with 2 or more keys. Root, non-root fusion. 
- Merge: After removal. 
- Assume everything in memory

AVL: 

- Balance factor: left height - right height. 
- Rotation: LL (R), LR(LR), RR(L), RL(RL)
- Assume everything in memory

### Lecture

Searching Strategies using Sorted data

- Sequential search
- Binary search
- Interpoloation search
- Indexed sequential search
- Search trees
- Must Sorted while insearting or deleting. => Cost 

Search tree

- In order traversal will give sorted list. 
- Search efficiency is the height of the tree
- Balanced?

Deletion

- 0 child
- 1 child: promote child
- 2 children: promote In order successor. 

AVL: Hieght balanced trees. 

B-Trees:m-ary tree, root has 2 more more children. **All leaves are at the same level**. with min number of children ceil(M/2) Node with 

- Red-Black
- Splay
- 2-3 
- 2-3-4

## ZyBooks

### 9.1 Searching and algorithms

An **algorithm** is a sequence of steps for accomplishing a task. **Linear search** is a search algorithm that starts from the beginning of a list, and checks each element until the search key is found or the end of the list is reached.

### 9.2 Binary search

**Binary search** is a faster algorithm for searching a list if the list's elements are sorted and directly accessible (such as an array). Binary search first checks the middle element of the list. If the search key is found, the algorithm returns the matching location. If the search key is not found, the algorithm repeats the search on the remaining left sublist (if the search key was less than the middle element) or the remaining right sublist (if the search key was greater than the middle element).

**Efficiency**: $⌊log2N⌋+1$

### 9.3 B-trees

A **B-tree** with order K is a tree where nodes can have up to K-1 keys and up to K children. An internal node **must** have one more children than keys. Each child of an internal node can have a different number of keys than the parent internal node.

The **order** is the maximum number of children a node can have.

Ex: In a B-tree with order 4, a node can have 1, 2, or 3 keys, and up to 4 children. B-trees have the following properties:

- All keys in a B-tree must be distinct.
- All leaf nodes must be at the same level.
- An internal node with N keys must have N+1 children. 
- Keys in a node are stored in **sorted** order from smallest to largest.
- Each key in a B-tree internal node has one left subtree and one right subtree. All left subtree keys are **<** that key, and all right subtree keys are **>** that key. => **No equal**

A valid order 5 B-tree: 

<img src="Img/09.03-1.png" alt="drawing" style="height:150px;"/>

A **2-3-4 tree** is an order 4 B-tree.

The keys in a 2-3-4 tree node are labeled as A, B and C. The child nodes of a 2-3-4 tree internal node are labeled as left, middle1, middle2, and right. If a node contains 1 key, then keys B and C, as well as children middle2 and right, are not used. If a node contains 2 keys, then key C, as well as the right child, are not used. A 2-3-4 tree node containing exactly 3 keys is said to be **full**, and uses all keys and children.

A node with 1 key is called a **2-node**. A node with 2 keys is called a **3-node**. A node with 3 keys is called a **4-node**.

### 9.4 2-3-4 tree search algorithm

Table 9.4.1: 2-3-4 tree child node to choose based on search key.

| Condition                                  | Child node to search |
| ------------------------------------------ | -------------------- |
| key < node's A key                         | left                 |
| node has only 1 key or key < node's B key  | middle1              |
| node has only 2 keys or key < node's C key | middle2              |
| none of the above                          | right                |

### 9.5 2-3-4 tree insert algorithm

Given a new key, a 2-3-4 tree **insert** operation inserts the new key in the proper location such that all 2-3-4 tree properties are preserved. New keys are **always inserted into leaf nodes** in a 2-3-4 tree. Insertion returns the leaf node where the key was inserted, or null if the key was already in the tree.

An important operation during insertion is the **split** operation, which is done on every full node encountered during insertion traversal. The split operation **moves the middle key from a child node into the child's parent node.** The first and last keys in the child node are moved into two separate nodes. The split operation returns the parent node that received the middle key from the child.

Example: Split a full root node(1 become 3, increase 2 nodes), and full non-root node 

<img src="Img/09.05-1.png" alt="drawing" style="height:100px;"/><img src="Img/09.05-2.png" alt="drawing" style="height:150px;"/><img src="Img/09.05-3.png" alt="drawing" style="height:150px;"/>

Table 9.5.1: **2-3-4 tree non-full-leaf insertion cases.**

| Condition                                             | Outcome                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| New key equals an existing key in node                | No insertion takes place, and the node is not altered.       |
| New key is < node's first key                         | Existing keys in node are shifted right, and the new key becomes node's first key. |
| Node has only 1 key or new key is < node's middle key | Node's middle key , if present, becomes last key, and new key becomes node's middle key. |
| None of the above                                     | New key becomes node's last key.                             |

The **preemptive split** insertion scheme always splits any full node encountered during insertion traversal. The preemptive split insertion scheme ensures that any time a full node is split, the parent node has room to accommodate the middle value from the child.

### 9.6 2-3-4 tree rotations and fusion

**Rotation concepts**

Removing an item from a 2-3-4 tree may require rearranging keys to maintain tree properties. A **rotation** is a rearrangement of keys between 3 nodes that maintains all 2-3-4 tree properties in the process. The 2-3-4 tree removal algorithm uses rotations to transfer keys between sibling nodes. 

A **right rotation**: on a node causes the node to lose one key and the node's right sibling to gain one key. 

Move the right key into node as left key, and move down the left key in root to middle 1 left key. 

<img src="Img/09.06-1.png" alt="drawing" style="height:150px;"/><img src="Img/09.06-2.png" alt="drawing" style="height:150px;"/>

A **left rotation** on a node causes the node to lose one key and the node's left sibling to gain one key.

<img src="Img/09.06-3.png" alt="drawing" style="height:150px;"/><img src="Img/09.06-4.png" alt="drawing" style="height:150px;"/>

A node being rotated must have at least 2 keys, and the right adjacent sibling must have no more than 2 keys.

A **fusion** is a combination of 3 keys: 2 from adjacent sibling nodes that have 1 key each, and a third from the parent of the siblings. Fusion is the inverse operation of a split. The key taken from the parent node must be the key that is between the 2 adjacent siblings. The parent node must have at least 2 keys, with the exception of the root.

Fusion of the root node is a special case that happens only when the root and the root's 2 children each have 1 key. In this case, the 3 keys from the 3 nodes are combined into a single node that becomes the new root node.

**Root fusion**

<img src="Img/09.06-5.png" alt="drawing" style="height:150px;"/><img src="Img/09.06-6.png" alt="drawing" style="height:150px;"/>

**Non-root fusion**

<img src="Img/09.06-7.png" alt="drawing" style="height:150px;"/>

<img src="Img/09.06-8.png" alt="drawing" style="height:150px;"/>

<img src="Img/09.06-9.png" alt="drawing" style="height:150px;"/>

### 9.7 2-3-4 tree removal

**Merge algorithm**

A B-Tree **merge** operates on a node with 1 key and increases the node's keys to 2 or 3 using either a rotation or fusion. A node's 2 adjacent siblings are checked first during a merge, and if either has 2 or more keys, a key is transferred via a rotation. Such a rotation increases the number of keys in the merged node from 1 to 2. If all adjacent siblings of the node being merged have 1 key, then fusion is used to increase the number of keys in the node from 1 to 3. The merge operation can be performed on any node that has 1 key and a non-null parent node with at least 2 keys.

<img src="Img/09.07-1.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-2.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-3.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-4.png" alt="drawing" style="height:200px;"/>

<img src="Img/09.07-5.png" alt="drawing" style="height:400px;"/>

**Utility functions for removal**

Several utility functions are used in a B-tree remove operation.

- `BTreeGetMinKey` returns the minimum key in a subtree.
- `BTreeGetChild` returns a pointer to a node's left, middle1, middle2, or right child, if the childIndex argument is 0, 1, 2, or 3, respectively.
- `BTreeNextNode` returns the child of a node that would be visited next in the traversal to search for the specified key.
- `BTreeKeySwap` swaps one key with another in a subtree. The replacement key must be known to be a key that can be used as a replacement without violating any of the 2-3-4 tree rules.

**Remove algorithm**

Given a key, a 2-3-4 tree **remove** operation removes the first-found matching key, restructuring the tree to preserve all 2-3-4 tree rules. Each successful removal results in a key being removed from a leaf node. 

Two cases are possible when removing a key, the first being that the key resides in a leaf node, and the second being that the key resides in an internal node.

The **preemptive merge** removal scheme involves increasing the number of keys in all single-key, non-root nodes encountered during traversal. The merging always happens before any key removal is attempted. **Preemptive merging ensures that any leaf node encountered during removal will have 2 or more keys,** allowing a key to be removed from the leaf node without violating the 2-3-4 tree rules.

To remove a key from an internal node, the key to be removed is replaced with the minimum key in the right child subtree (known as the key's successor), or the maximum key in the leftmost child subtree. First, the key chosen for replacement is stored in a temporary variable, then the chosen key is removed recursively, and lastly the temporary key replaces the key to be removed.

**9.7.4: BTreeRemove algorithm: leaf case.**

<img src="Img/09.07-6.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-7.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-8.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-9.png" alt="drawing" style="height:400px;"/>

**9.7.5: BTreeRemove algorithm: non-leaf case.**

<img src="Img/09.07-10.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-11.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-12.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-13.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-14.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.07-15.png" alt="drawing" style="height:400px;"/>

### 9.8 AVL: A balanced tree

#### Balanced BST

An **AVL tree** is a **BST(make sure it is BST!)** with a height balance property and specific operations to rebalance the tree when a node is inserted or removed. This section discusses the balance property; another section discusses the operations. A BST is **height balanced** if for any node, the heights of the node's left and right subtrees differ by only 0 or 1. 

A node's **balance factor** is the left subtree height minus the right subtree height, which is 1, 0, or -1 in an AVL tree. 

Recall that a tree (or subtree) with just one node has height 0. For calculating a balance factor, a non-existent left or right child's subtree's height is said to be -1.

<img src="Img/09.08-1.png" alt="drawing" style="height:300px;"/>

Minimizing binary tree height yields fastest searches, insertions, and removals. 

maintaining a minimum height tree requires extensive tree rearrangements. In contrast, an AVL tree only requires a few local rotations (discussed in a later section), so is more computationally efficient, but doesn't guarantee a minimum height. However, theoreticians have shown that an AVL tree's worst case **height is no worse than about 1.5x the minimum binary tree height**, so **the height is still $O(log N)$** where N is the number of nodes. Furthermore, experiments show that AVL tree heights in practice are much closer to the minimum.

### 9.9 AVL rotations

<img src="Img/09.09-1.png" alt="drawing" style="height:200px;"/>

#### Algorithms supporting AVL trees

The `AVLTreeUpdateHeight` algorithm updates a node's height value by taking the maximum of the child subtree heights and adding 1. 

The `AVLTreeSetChild` algorithm sets a node as the parent's left or right child, updates the child's parent pointer, and updates the parent node's height. 

The `AVLTreeReplaceChild` algorithm replaces one of a node's existing child pointers with a new value, utilizing `AVLTreeSetChild` to perform the replacement.

The `AVLTreeGetBalance` algorithm computes a node's balance factor by subtracting the right subtree height from the left subtree height.

9.9.7: Right rotation algorithm.

<img src="Img/09.09-2.png" alt="drawing" style="height:200px;"/>

<img src="Img/09.09-3.png" alt="drawing" style="height:200px;"/>

<img src="Img/09.09-4.png" alt="drawing" style="height:200px;"/>

#### AVL tree balancing

When an AVL tree node has a balance factor of 2 or -2, which **only occurs after an insertion or removal**, the node must be rebalanced via rotations. The `AVLTreeRebalance` algorithm updates the height value at a node, computes the balance factor, and rotates if the balance factor is 2 or -2.

### 9.10 AVL insertions

Rotation

<img src="Img/09.10-1.png" alt="drawing" style="height:200px;"/>

Double Rotation

<img src="Img/09.10-2.png" alt="drawing" style="height:200px;"/>

4 modes

<img src="Img/09.10-3.png" alt="drawing" style="height:400px;"/>

And rotations for 4 modes

<img src="Img/09.10-4.png" alt="drawing" style="height:400px;"/>

An AVL tree insertion involves **searching** for the insert location, **inserting** the new node, **updating** balance factors, and **rebalancing**.

2 examples: Phone book

<img src="Img/09.10-5.png" alt="drawing" style="height:400px;"/>

<img src="Img/09.10-6.png" alt="drawing" style="height:150px;"/>

AVL tree has X levels, the first X-1 levels might not be full. 

AVL tree doesn't guarantee minimum height, as levels are not guaranteed to be kept full. The worst case will be 1.5x min height, So it is still $O(logn)$but not floor$(logn)$ (which is for the min height)

The node passed to AVLTreeInsert must be a leaf node.

#### AVL insertion algorithm complexity

The AVL insertion algorithm traverses the tree from the root to a leaf node to find the insertion point, then traverses back up to the root to rebalance. One node is visited per level, and at most 2 rotations are needed for a single node. Each rotation is an O(1) operation. Therefore, the runtime complexity of insertion is O(log N).

Because a fixed number of temporary pointers are needed for the AVL insertion algorithm, including any rotations, the space complexity is O(1).

### 9.11 AVL removals

#### Removing nodes in AVL trees

Given a key, an AVL tree **remove** operation removes the first-found matching node, restructuring the tree to preserve all AVL tree requirements. Removal begins by removing the node using the standard BST removal algorithm. After removing a node, all ancestors of the removed node, from the nodes' parent up to the root, are rebalanced. A node is rebalanced by first computing the node's balance factor, then performing rotations if the balance factor is 2 or -2.



### 9.12 Red-black tree: A balanced tree

### 9.13 Red-black tree: Rotations

### 9.14 Red-black tree: Insertion

### 9.15 Red-black tree: Removal
