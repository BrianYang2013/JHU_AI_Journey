# Module 10 - Hash

### 10.2: Common hash functions

Figure 10.2.1: Modulo hash function.

```
HashRemainder(int key) {
   return key % N
}
```

The mid-square hash function is typically implemented using binary (base 2) for better performance. 

Figure 10.2.2: Mid-square hash function (base 2).

```
HashMidSquare(int key) {
   squaredKey = key * key
   
   lowBitsToRemove = (32 - R) / 2
   extractedBits = squaredKey >> lowBitsToRemove
   extractedBits = extractedBits & (0xFFFFFFFF >> (32 - R)) 

   return extractedBits % N
}
```

Figure 10.2.3: Multiplicative string hash function.

```
HashMultiplicative(string key) {
   stringHash = InitialValue 

   for (each character strChar in key) {
      stringHash = (stringHash * HashMultiplier) + strChar
   }

   return stringHash % N
}
```

### 10.3 Chaining

Figure 10.3.1: Hash table with chaining: Each bucket contains a list of items.

```
HashInsert(hashTable, item) {
   if (HashSearch(hashTable, item⇢key) == null) {
      bucketList = hashTable[Hash(item⇢key)]
      node = Allocate new linked list node
      node⇢next = null
      node⇢data = item
      ListAppend(bucketList, node)
   }
}

HashRemove(hashTable, item) {
   bucketList = hashTable[Hash(item⇢key)]
   itemNode = ListSearch(bucketList, item⇢key)
   if (itemNode is not null) {
      ListRemove(bucketList, itemNode)
   } 
}

HashSearch(hashTable, key) {
   bucketList = hashTable[Hash(key)]
   itemNode = ListSearch(bucketList, key)
   if (itemNode is not null)
      return itemNode⇢data
   else
      return null
}
```

### 10.4 Linear probing

10.4.4: Insert with linear probing.

```
HashInsert(hashTable, item) {
   // Hash function determines initial bucket
   bucket = Hash(item.key)    
   bucketsProbed = 0
   N = hashTable's size
   while (bucketsProbed < N) {
      // Insert item in next empty bucket
      if (hashTable[bucket] is Empty) {
         hashTable[bucket] = item
         return true 
      }

      // Increment bucket index
      bucket = (bucket + 1) % N

      // Increment number of buckets probed
      ++bucketsProbed
   }

   return false      
}
```

10.4.6: Remove with linear probing.

```
HashRemove(hashTable, key) {  
   // Hash function determines initial bucket
   bucket = Hash(key)
   bucketsProbed = 0

   while ((hashTable[bucket] is not EmptySinceStart) and
         (bucketsProbed < N)) {

      if ((hashTable[bucket] is not Empty) and
         (hashTable[bucket]⇢key == key)) {
         hashTable[bucket] = EmptyAfterRemoval
         return
      }

      // Increment bucket index
      bucket = (bucket + 1) % N

      // Increment number of buckets probed
      ++bucketsProbed
   }
}
```

10.4.8: Search with linear probing.

```
HashSearch(hashTable, key) {
   // Hash function determines initial bucket
   bucket = Hash(key)
   bucketsProbed = 0

   while ((hashTable[bucket] is not EmptySinceStart) and
         (bucketsProbed < N)) {

      if ((hashTable[bucket] is not Empty) and
         (hashTable[bucket]⇢key == key)) {
         return hashTable[bucket]
      }

      // Increment bucket index
      bucket = (bucket + 1) % N

      // Increment number of buckets probed
      ++bucketsProbed
   }

   return null  // Item not found
}
```

### 10.5 Quadratic probing

Figure 10.5.1: HashInsert with quadratic probing.

```
HashInsert(hashTable, item) {
   i = 0
   bucketsProbed = 0

   // Hash function determines initial bucket
   bucket = Hash(item⇢key) % N
   while (bucketsProbed < N) {
      // Insert item in next empty bucket 
      if (hashTable[bucket] is Empty) {
         hashTable[bucket] = item
         return true  
      }

      // Increment i and recompute bucket index
      // c1 and c2 are programmer-defined constants for quadratic probing
      i = i + 1
      bucket = (Hash(item⇢key) + c1 * i + c2 * i * i) % N

      // Increment number of buckets probed
      bucketsProbed = bucketsProbed + 1
   }
   return false       
}
```

Figure 10.5.2: HashRemove and HashSearch with quadratic probing.

```
HashRemove(hashTable, key) {
   i = 0
   bucketsProbed = 0

   // Hash function determines initial bucket
   bucket = Hash(key) % N

   while ((hashTable[bucket] is not EmptySinceStart) and (bucketsProbed < N)) {
      if ((hashTable[bucket] is Occupied) and (hashTable[bucket]⇢key == key)) {
         hashTable[bucket] = EmptyAfterRemoval
         return true
      }

      // Increment i and recompute bucket index
      // c1 and c2 are programmer-defined constants for quadratic probing
      i = i + 1
      bucket = (Hash(key) + c1 * i + c2 * i * i) % N

      // Increment number of buckets probed
      bucketsProbed = bucketsProbed + 1
   }
   return false // key not found
}


HashSearch(hashTable, key) {
   i = 0
   bucketsProbed = 0

   // Hash function determines initial bucket
   bucket = Hash(key) % N

   while ((hashTable[bucket] is not EmptySinceStart) and (bucketsProbed < N)) {
      if ((hashTable[bucket] is Occupied) and (hashTable[bucket]⇢key == key)) {
         return hashTable[bucket]
      }

      // Increment i and recompute bucket index
      // c1 and c2 are programmer-defined constants for quadratic probing
      i = i + 1
      bucket = (Hash(key) + c1 * i + c2 * i * i) % N

      // Increment number of buckets probed
      bucketsProbed = bucketsProbed + 1
   }
   return null  // key not found
}
```

### 10.6 Double hashing

Figure 10.7.1: Direct hashing: Insert, remove, and search operations use item's key as bucket index.

```
HashInsert(hashTable, item) {
   hashTable[item⇢key] = item 
}

HashRemove(hashTable, item) {
   hashTable[item⇢key] = Empty
}

HashSearch(hashTable, key) {
   if (hashTable[key] is not Empty) {
      return hashTable[key]
   }
   else  {
      return null
   }
}
```

### 10.9 Bucket sort

Figure 10.9.1: Bucket sort algorithm.

```
BucketSort(numbers, numbersSize, bucketCount) {
   if (numbersSize < 1)
      return

   buckets = Create list of bucketCount buckets

   // Find the maximum value
   maxValue = numbers[0]
   for (i = 1; i < numbersSize; i++) {
      if (numbers[i] > maxValue)
         maxValue = numbers[i]
   }

   // Put each number in a bucket
   for each (number in numbers) {
      index = floor(number * bucketCount / (maxValue + 1))
      Append number to buckets[index]
   }

   // Sort each bucket
   for each (bucket in buckets)
      Sort(bucket)

   // Combine all buckets back into numbers list
   result = Concatenate all buckets together
   Copy result to numbers
}
```
