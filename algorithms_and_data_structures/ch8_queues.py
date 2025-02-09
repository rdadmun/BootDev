# Queues
# A queue is a data structure that stores ordered items. 
# It’s like a list, but again, like a stack, its design is more restrictive. 
# A queue only allows items to be added to the tail of the queue and removed from the head of the queue.

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)
    
# Matchmaking Queue
from queue import Queue

def matchmake(queue, user):
    name, action = user
    if action == "join":
        queue.push(name)
    elif action == "leave":
        queue.search_and_remove(name)
    if queue.size() < 4:
        return "No match found"
    matched_users = [queue.pop(), queue.pop()]
    return f"{matched_users[0]} matched {matched_users[1]}!"

