# Stacks
# A stack is a data structure that stores ordered items. It’s like a list, but its design is more restrictive. 
# It only allows items to be added or removed from the top of the stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
    
# Using a Stack to check for pairs of parentheses:
#from stack import Stack

def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char in "(":
            stack.push(char)
        elif char in ")":
            if stack.size() == 0:
                return False
            stack.pop()
    return stack.size() == 0

# Debounce Stack
#from stack import Stack

class DebounceStack(Stack):
    def __init__(self):
        super().__init__()
    
    def push (self, item):
        if self.size() >0 and self.items[-1] == item:
            return
        else:
            super().push(item)