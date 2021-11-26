# Module 9 - Search

### 9.1 Searching and algorithms

Figure 9.1.1: Linear search algorithm.

```
LinearSearch(numbers, numbersSize, key) {
   i = 0

   for (i = 0; i < numbersSize; ++i) {
      if (numbers[i] == key) {
         return i
      }
   }
      
   return -1 // not found
}
   
main() {
   numbers = {2, 4, 7, 10, 11, 32, 45, 87}
   NUMBERS_SIZE = 8
   i = 0
   key = 0
   keyIndex = 0
      
   print("NUMBERS: ")
   for (i = 0; i < NUMBERS_SIZE; ++i) {
      print(numbers[i] + " ")
   }
   printLine()
      
   print("Enter a value: ")
   key = getIntFromUser()
      
   keyIndex = LinearSearch(numbers, NUMBERS_SIZE, key)
      
   if (keyIndex == -1) {
      printLine(key + " was not found.")
   } 
   else {
      printLine("Found " + key + " at index " + keyIndex + ".")
   }
}
```

### 9.2 Binary search

Figure 9.2.1: Binary search algorithm.

```
BinarySearch(numbers, numbersSize, key) {
   mid = 0
   low = 0
   high = numbersSize - 1
   
   while (high >= low) {
      mid = (high + low) / 2
      if (numbers[mid] < key) {
         low = mid + 1
      }
      else if (numbers[mid] > key) {
         high = mid - 1
      }
      else {
         return mid
      }
   }
   
   return -1 // not found
}

main() {
   numbers = { 2, 4, 7, 10, 11, 32, 45, 87 }
   NUMBERS_SIZE = 8
   i = 0
   key = 0
   keyIndex = 0
   
   print("NUMBERS: ")
   for (i = 0; i < NUMBERS_SIZE; ++i) {
      print(numbers[i] + " ")
   }
   printLine()
   
   print("Enter a value: ")
   key = getIntFromUser()
   
   keyIndex = BinarySearch(numbers, NUMBERS_SIZE, key)
   
   if (keyIndex == -1) {
      printLine(key + " was not found.")
   }
   else {
      printLine("Found " + key + " at index " + keyIndex + ".")
   }
}
```

### 9.3 B-trees

### 9.4 2-3-4 tree search algorithm

9.4.1: 2-3-4 tree search algorithm.

```
BTreeSearch(node, key) {
   if (node is not null) {
      if (key == node⇢A ||
          key == node⇢B ||
          key == node⇢C) {
         return node
      }
      if (key < node⇢A) {
         return BTreeSearch(node⇢left, key)
      }
      else if (node⇢B is null || key < node⇢B) {
         return BTreeSearch(node⇢middle1, key)
      }
      else if (node⇢C is null || key < node⇢C) {
         return BTreeSearch(node⇢middle2, key)
      }
      else {
         return BTreeSearch(node⇢right, key)
      }
   }
   return null
}
```

### 9.5 2-3-4 tree insert algorithm

Splitting an internal node allocates 2 new nodes, each with a single key, and the middle key from the split node moves up into the parent node. Splitting the root node allocates 3 new nodes, each with a single key, and the root of the tree becomes a new node with a single key.

9.5.3: B-tree split operation.

```
BTreeSplit(tree, node) {
   if (node is not full) {
      return null
   }
   nodeParent = node⇢parent
   splitLeft = new BTreeNode(node⇢A, node⇢left, node⇢middle1)
   splitRight = new BTreeNode(node⇢C, node⇢middle2, node⇢right)
   if (nodeParent is not null) {
      BTreeInsertKeyWithChildren(nodeParent, node⇢B, splitLeft, splitRight)
   }
   else {
      nodeParent = new BTreeNode(node⇢B, splitLeft, splitRight)
      tree⇢root = nodeParent
   }
   return nodeParent
}
```

Figure 9.5.1: Inserting a key with children within a parent node.

```
BTreeInsertKeyWithChildren(parent, key, leftChild, rightChild) {
   if (key < parent⇢A) {
      parent⇢C = parent⇢B
      parent⇢B = parent⇢A
      parent⇢A = key
      parent⇢right = parent⇢middle2
      parent⇢middle2 = parent⇢middle1
      parent⇢middle1 = rightChild
      parent⇢left = leftChild
   }
   else if (parent⇢B is null || key < parent⇢B) {
      parent⇢C = parent⇢B
      parent⇢B = key
      parent⇢right = parent⇢middle2
      parent⇢middle2 = rightChild
      parent⇢middle1 = leftChild
   }
   else {
      parent⇢C = key
      parent⇢right = rightChild
      parent⇢middle2 = leftChild
   }
}
```

9.5.6: B-tree insertion with preemptive split algorithm.

```
BTreeInsert(node, key) {
   if (key is in node) {
      return null // duplicates not allowed
   }
   if (node is full) {
      node = BTreeSplit(tree, node, nodeParent)
   }
   if (node is not leaf) {
      if (key < node⇢A)
         return BTreeInsert(node⇢left, key)
      else if (node⇢B is null || key < node⇢B)
         return BTreeInsert(node⇢middle1, key)
      else if (node⇢C is null || key < node⇢C)
         return BTreeInsert(node⇢middle2, key)
      else
         return BTreeInsert(node⇢right, key)
   }
   else {
      BTreeInsertIntoLeaf(node, key)
      return node
   }
}
```

### 9.6 2-3-4 tree rotations and fusion

**Utility functions for rotations**

Several utility functions are used in the rotation operation. 

- `BTreeGetLeftSibling` returns a pointer to the left sibling of a node or null if the node has no left sibling. BTreeGetLeftSibling returns null, left, middle1, or middle2 if the node is the left, middle1, middle2, or the right child of the parent, respectively. Since the parent node is required, a precondition of this function is that the node is not the root. 
- `BTreeGetRightSibling` returns a pointer to the right sibling of a node or null if the node has no right sibling. 
- `BTreeGetParentKeyLeftOfChild` takes a parent node and a child of the parent node as arguments, and returns the key in the parent that is immediately left of the child. 
- `BTreeSetParentKeyLeftOfChild` takes a parent node, a child of the parent node, and a key as arguments, and sets the key in the parent that is immediately left of the child.
- `BTreeAddKeyAndChild` operates on a non-full node, adding one new key and one new child to the node. The new key must be greater than all keys in the node, and all keys in the new child subtree must be greater than the new key. Ex: If the node has 1 key, the newly added key becomes key B in the node, and the child becomes the middle2 child. If the node has 2 keys, the newly added key becomes key C in the node, and the child becomes the right child.
- `BTreeRemoveKey` removes a key from a node using a key index in the range [0,2]. This process may require moving keys and children to fill the location left by removing the key. The pseudocode for BTreeRemoveKey is below.

Figure 9.6.1: BTreeRemoveKey pseudocode.

```
BTreeRemoveKey(node, keyIndex) {
   if (keyIndex == 0) {
      node⇢A = node⇢B
      node⇢B = node⇢C
      node⇢C = null
      node⇢left = node⇢middle1
      node⇢middle1 = node⇢middle2
      node⇢middle2 = node⇢right
      node⇢right = null
   }
   else if (keyIndex == 1) {
      node⇢B = node⇢C
      node⇢C = null
      node⇢middle2 = node⇢right
      node⇢right = null
   }
   else if (keyIndex == 2) {
      node⇢C = null
      node⇢right = null
   }
}
```

9.6.4: Left rotation pseudocode.

```
BTreeRotateLeft(node) {
   leftSibling = BTreeGetLeftSibling(node)
   keyForLeftSibling = BTreeGetParentKeyLeftOfChild(node⇢parent, node)
   BTreeAddKeyAndChild(leftSibling, keyForLeftSibling, node⇢left)
   BTreeSetParentKeyLeftOfChild(node⇢parent, node, node⇢A)     
   BTreeRemoveKey(node, 0)
}
```

9.6.6: Root fusion.

```
BTreeFuseRoot(root) {
   oldLeft = root⇢left
   oldMiddle1 = root⇢middle1
   root⇢B = root⇢A
   root⇢A = oldLeft⇢A
   root⇢C = oldMiddle1⇢A
   root⇢left = oldLeft⇢left
   root⇢middle1 = oldLeft⇢middle1
   root⇢middle2 = oldMiddle1⇢left
   root⇢right = oldMiddle1⇢middle1
   return root
}
```

9.6.8: Non-root fusion.

```
BTreeFuse(leftNode, rightNode) {
   parent = leftNode⇢parent
   if (parent is root and has 1 key)
      return BTreeFuseRoot(parent)
   middleKey = BTreeGetParentKeyLeftOfChild(parent, rightNode)
   fusedNode = new Node(leftNode⇢A, middleKey, rightNode⇢A)
   fusedNode⇢left = leftNode⇢left
   fusedNode⇢middle1 = leftNode⇢middle1
   fusedNode⇢middle2 = rightNode⇢left
   fusedNode⇢right = rightNode⇢middle1
   keyIndex = BTreeGetKeyIndex(parent, middleKey)
   BTreeRemoveKey(parent, keyIndex)
   BTreeSetChild(parent, fusedNode, keyIndex)
   return fusedNode
}
```

#### Utility functions for removal

Figure 9.7.1: BTreeGetMinKey pseudocode.

- `BTreeGetMinKey` returns the minimum key in a subtree.

```
BTreeGetMinKey(node) {
   cur = node
   while (cur⇢left != null) {
      cur = cur⇢left
   }
   return cur⇢A
}
```

Figure 9.7.2: BTreeGetChild pseudocode.

- `BTreeGetChild` returns a pointer to a node's left, middle1, middle2, or right child, if the childIndex argument is 0, 1, 2, or 3, respectively.

```
BTreeGetChild(node, childIndex) {
   if (childIndex == 0)
      return node⇢left
   else if (childIndex == 1)
      return node⇢middle1
   else if (childIndex == 2)
      return node⇢middle2
   else if (childIndex == 3)
      return node⇢right
   else
      return null
}
```

Figure 9.7.3: BTreeNextNode pseudocode.

- `BTreeNextNode` returns the child of a node that would be visited next in the traversal to search for the specified key.

```
BTreeNextNode(node, key) {
   if (key < node⇢A)
      return node⇢left
   else if (node⇢B == null || key < node⇢B)
      return node⇢middle1
   else if (node⇢C == null || key < node⇢C)
      return node⇢middle2
   else
      return node⇢right
}
```

Figure 9.7.4: BTreeKeySwap pseudocode.

- `BTreeKeySwap` swaps one key with another in a subtree. The replacement key must be known to be a key that can be used as a replacement without violating any of the 2-3-4 tree rules.

```
BTreeKeySwap(node, existing, replacement) {
   if (node == null)
      return false

   keyIndex = BTreeGetKeyIndex(node, existing)
   if (keyIndex == -1) {
      next = BTreeNextNode(node, existing)
      return BTreeKeySwap(next, existing, replacement)
   }

   if (keyIndex == 0)
      node⇢A = replacement
   else if (keyIndex == 1)
      node⇢B = replacement
   else
      node⇢C = replacement

   return true
}
```

9.7.4: BTreeRemove algorithm: leaf case.

```
BTreeRemove(tree, key) {
   if (tree⇢root is leaf with 1 key &&
      tree⇢root⇢A == key) {
      tree⇢root = null
      return true
   }
 
   cur = tree⇢root
   while (cur != null) {
      if (cur has 1 key and cur != tree⇢root) {
         cur = BTreeMerge(cur)
      }
      keyIndex = BTreeGetKeyIndex(cur, key)
      if (keyIndex != -1) {
         if (cur is leaf) {
            BTreeRemoveKey(cur, keyIndex)
            return true
         }
         tmpChild = BTreeGetChild(cur, keyIndex + 1)
         tmpKey = BTreeGetMinKey(tmpChild)
         BTreeRemove(tree, tmpKey)
         BTreeKeySwap(tree⇢root, key, tmpKey)
         return true
      }
         
      cur = BTreeNextNode(cur, key)
   }
   return false
}
```

9.7.5: BTreeRemove algorithm: non-leaf case.

```
BTreeRemove(tree, key) {
   if (tree⇢root is leaf with 1 key &&
      tree⇢root⇢A == key) {
      tree⇢root = null
      return true
   }
 
   cur = tree⇢root
   while (cur != null) {
      if (cur has 1 key and cur != tree⇢root) {
         cur = BTreeMerge(cur)
      }
      keyIndex = BTreeGetKeyIndex(cur, key)
      if (keyIndex != -1) {
         if (cur is leaf) {
            BTreeRemoveKey(cur, keyIndex)
            return true
         }
         tmpChild = BTreeGetChild(cur, keyIndex + 1)
         tmpKey = BTreeGetMinKey(tmpChild)
         BTreeRemove(tree, tmpKey)
         BTreeKeySwap(tree⇢root, key, tmpKey)
         return true
      }
         
      cur = BTreeNextNode(cur, key)
   }
   return false
}
```





### 9.7 2-3-4 tree removal



9.8 AVL: A balanced tree



9.9 AVL rotations


9.10 AVL insertions



9.11 AVL removals



9.12 Red-black tree: A balanced tree


9.13 Red-black tree: Rotations

9.14 Red-black tree: Insertion

9.15 Red-black tree: Removal
