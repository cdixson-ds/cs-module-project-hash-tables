#table = [None] * 8

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # def __repr__(self):
    #     return f"HashTableEntry({repr(self.key)},{repr(self.value)})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        #initiate w/empty values
        self.bucket = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.bucket)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        #num of items put into the hash table divided by capacity
        return self.count / self.capacity


    def fnv1(self, key):
        """
        # FNV-1 Hash, 64-bit

        # Implement this, and/or DJB2.
        # """


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        arr = key.encode('ascii')
        #arr = key.encode('utf-8')


        for i in arr:
            hash = (( hash * 33) ^ i) % 0x100000000
        return hash
        

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #generate number representation of string and 
        #split with modulus by the capacity, get index for key

        return self.djb2(key) % self.capacity
        #return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #add value by key
        index = self.hash_index(key)
        node = self.bucket[index]
        prev = HashTableEntry(key, value)
        
        if node is not None:
            self.bucket[index] = prev
            self.bucket[index].next = node
            
        #if something is in the bucket
        else:
            self.bucket[index] = prev
            self.count += 1
        #check if hash resize necessary
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if key is key:
            self.put(key, None)
            self.count -= 1
        else:
            print("key not found.")
    

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.bucket[index]
        if node is not None:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return node

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_hash = HashTable(new_capacity)
        for entry in self.bucket:
            if entry:
                #update new hashtable, pass in key/value
                new_hash.put(entry.key, entry.value)
                if entry.next:
                    #set the current var to entry
                    current = entry
                    while current.next:
                        current = current.next
                        #use put to modify new hash table
                        new_hash.put(current.key, current.value)
        self.bucket = new_hash.bucket
        self.capacity = new_hash.capacity



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
