# Trees are a widely used data structure that simulate a hierarchical… well… tree structure. 
# That said, they’re typically drawn upside down - the “root” node is at the top, and the “leaves” are at the bottom.
# A generic tree structure has the following rules:
    # Each node has a value and a list of “children”
    # Children can only have a single “parent”
# One of the most common types of ordered tree is a Binary Search Tree or BST. In addition to the properties we’ve already talked about, a BST has some additional constraints:
    # Instead of an unbounded list of children, each node has at most 2 children
    # The left child’s value must be less than its parent’s value
    # The right child’s value must be greater than its parent’s value
    # No two nodes in the BST can have the same value
    
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left == None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

# Min and Max
    def get_min(self):
        if not self.left:
            return self.val
        return self.left.get_min()

    def get_max(self):
        if not self.right:
            return self.val
        return self.right.get_max()

# Delete
    def delete(self, val):
        if self.val == None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if val == self.val:
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.val = min_larger_node.val
            self.right = self.right.delete(min_larger_node.val)
        return self

# Pre-order Traversal
# A “preorder” traversal is a way to visit all the nodes in a tree. 
# It’s called “preorder” because the current node is visited before its children.
    def preorder(self, visited):
        final_lst = []
        if self.val is not None:
            final_lst.append(self.val)
        if self.left:
            final_lst.extend(self.left.preorder(visited))
        if self.right:
            final_lst.extend(self.right.preorder(visited))
        return final_lst

# Post-order Traversal
# A “postorder” traversal also visits all the nodes in a tree. 
# It’s called “postorder” because the current node is visited after its children.
    def postorder(self, visited):
        final_lst = []
        if self.left:
            final_lst.extend(self.left.postorder(visited))
        if self.right:
            final_lst.extend(self.right.postorder(visited))
        if self.val is not None:
            final_lst.append(self.val)
        return final_lst
    
# Inorder Traversal
# An “inorder” traversal is the most intuitive way to visit all the nodes in a tree. 
# It’s called “inorder” because the current node is visited between its children. 
# It results in an ordered list of the nodes in the tree. 
    def inorder(self, visited):
        final_lst = []
        if self.left:
            final_lst.extend(self.left.inorder(visited))
        if self.val is not None:
            final_lst.append(self.val)
        if self.right:
            final_lst.extend(self.right.inorder(visited))
        return final_lst
    
# Node Exists
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)
    
# Search Range
    def search_range(self, lower_bound, upper_bound):
        result = []
        if self.val is None:
            return result
        if self.left and self.val >= lower_bound:
            result.extend(self.left.search_range(lower_bound, upper_bound))
        if lower_bound <= self.val <= upper_bound:
            result.append(self.val)
        if self.right and self.val <= upper_bound:
            result.extend(self.right.search_range(lower_bound, upper_bound))
        return result
    
# Tree Height Function
    def height(self):
        if self.val is None:
            return 0

        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        return max(left_height, right_height) + 1


