# Linked Lists
# To be able to build our faster queue, we’re going to need to use a Linked List instead of an array under the hood. 
# A linked list is a linear data structure where elements are not stored next to each other in memory. 
# The elements in a linked list are linked using references to each other.

# Linked Lists
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
    
# This kind of iteration is annoying, and has more overhead, so why use a linked list? 
# We use them sometimes because linked lists are much faster to make updates to, particularly when inserting or deleting items from the middle. 
# In a normal list, if you insert an item in the middle, you have to shift all the items after it down one spot (O(n)):

# Even though iterating with linked lists kinda sucks compared to the simplicity of arrays (normal lists), we’ve got to do it. 
# Although the implementation is more complex and slow, we can still make it easy for users of our class by implementing the __iter__ method.

# from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

# Add to Tail
# from node import Node


class LinkedList:
    def add_to_tail(self, node):
        if not self.head:
            self.head = node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.set_next(node)
        
    # don't touch below this line
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
    
# Add to Head
    def add_to_head(self, node):
        if not self.head:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node
         
# Improving Linked Lists to more clearly iterate more effectively   
#from node import Node
class LinkedList:
    def add_to_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def __init__(self):
        self.head = None
        self.tail =  None

    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

# Final Iteration:
# from node import Node
class LLQueue:
    def remove_from_head(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return temp

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)
