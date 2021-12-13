# Module 14 - Transposition and Hash

## Course Module

### Summary

Hash will consider

- Hash function covers most of the buckets / Hash table? Even/Odd, percentage. 
- How many collisions? 

### Lecture

## ZyBooks

### 10.1 Hash tables

A **hash table** is a data structure that stores **unordered** items by mapping (or hashing) each item to a location in an array (or vector).

A hash table's main advantage is that **searching (or inserting / removing)** an item may require only **O(1)**, in contrast to O(N) for searching a list or to O(log N) for binary search.

In a hash table, an item's **key** is the value used to map to an index. Each hash table array element is called a **bucket**. A **hash function** computes a bucket index from the item's key.

A common hash function uses the **modulo operator %**, which computes the integer remainder when dividing two numbers. 

**Empty cells:** The approach for a hash table algorithm determining whether a cell is empty depends on the implementation. For example, if items are simply non-negative integers, empty can be represented as -1. More commonly, items are each an object with multiple fields (name, age, etc.), in which case each hash table array element may be a pointer. Using pointers, empty can be represented as null.

A **collision** occurs when an item being inserted into a hash table maps to the same bucket as an existing item in the hash table. 

- **Chaining** is a collision resolution technique where each bucket has a list of items (so bucket 5's list would become 55, 75). 

- **Open addressing** is a collision resolution technique where collisions are resolved by looking for an empty bucket elsewhere in the table

### 10.2 Common hash functions

A good hash function minimizes collisions

A **mid-square hash** squares the key, extracts R digits from the result's middle, and returns the remainder of the middle digits divided by hash table size N. Ex: For a hash table with 100 entries and a key of 453, the decimal (base 10) mid-square hash function computes 453 * 453 = 205209, and returns the middle two digits 52. For N buckets, R must be greater than or equal to $⌈log10N⌉$ to index all buckets. The process of squaring and extracting middle digits reduces the likelihood of keys mapping to just a few buckets.

- Key = 453, Buckets = 100, R=2: key^2 = 205209, 52MOD100=52
- Key = 40, Buckets = 100, R=2: key^2 = 1600, 60MOD100=60
- Key = 110, Buckets = 200, R=3: key^2 = 12100, 210MOD200=10

N = 200, R = $ceil(log_2{200}) = 8$

A **multiplicative string hash** repeatedly multiplies the hash value and adds the ASCII (or Unicode) value of each character in the string. A multiplicative hash function for strings starts with a large initial value. For each character, the hash function multiplies the current hash value by a multiplier (often prime) and adds the character's value. Finally, the function returns the remainder of the sum divided by the hash table size N.

Daniel J. Bernstein created a popular version of a multiplicative string hash function that uses an initial value of 5381 and a multiplier of 33. Bernstein's hash function performs well for hashing short English strings.

### 10.3 Chaining

**Chaining** handles hash table collisions by using a list for each bucket, where each list may store multiple items that map to the same bucket. 

<img src="Img/10.03-1.png" alt="drawing" style="height:500px;"/>

10.4 Linear probing
10.5 Quadratic probing
10.6 Double hashing
10.7 Direct hashing
10.8 Hashing Algorithms: Cryptography, Password Hashing
10.9 Bucket sort

### 
