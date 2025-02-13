# Hashmaps
# A hash map or "hash table" is a data structure that maps keys to values:
# "bob" -> "ross"
# "pablo" -> "picasso"
# "leonardo" -> "davinci"
# The lookup, insertion, and deletion operations of a hashmap have an average computational cost of O(1). 
# Assuming you know the key, nothing beats a hashmap! A Python dictionary is an example of a hashmap. 
# See, you already know what a hashmap is!

# Key to Index
class HashMap:
    def key_to_index(self, key):
        sum_value = 0
        for char in key:
            sum_value += ord(char)
        val = sum_value % len(self.hashmap)
        return int(val) 
    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
class HashMap:
    def key_to_index(self, key):
        sum_value = 0
        for char in key:
            sum_value += ord(char)
        val = sum_value % len(self.hashmap)
        return int(val) 
    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

# Insert
    def insert(self, key, value):
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

# Get
    def get(self, key):
        index = self.key_to_index(key)            
        if self.hashmap[index] is None or self.hashmap[index][0] != key:
            raise Exception("sorry, key not found")
        return self.hashmap[index][1]

# Challange 1 - Resizing:
class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        load_factor = self.current_load()
        if load_factor < 0.05:
            return
        new_size = len(self.hashmap) * 10
        new_hashmap = [None for _ in range(new_size)]
        for bucket in self.hashmap:
            if bucket is not None:
                key, value = bucket
                index = self.key_to_index(key) % new_size
                new_hashmap[index] = key, value
        self.hashmap = new_hashmap

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        filled_slots = sum(1 for bucket in self.hashmap if bucket is not None)
        return filled_slots / len(self.hashmap)
    
# Linear Probing
class HashMap:
    def insert(self, key, value):
        original_index = self.key_to_index(key)
        index = original_index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = key, value
    def get(self, key):
        original_index = self.key_to_index(key)
        index = original_index
        first_iteration = True
        while self.hashmap[index] is not None:    
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == self.key_to_index(key):
                raise Exception("sorry, key not found")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")