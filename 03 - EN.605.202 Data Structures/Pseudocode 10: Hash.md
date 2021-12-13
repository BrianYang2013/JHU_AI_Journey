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
