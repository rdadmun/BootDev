# Data Structures Intro
# Stacks: Last in, first out.
# Queues: First in, first out.
# Linked Lists: A chain of nodes, efficient for inserts and deletes.
# Binary Trees: A tree where each node has up to two children.
# Red Black Trees: A self-balancing binary tree using colors.
# Hashmaps: A data structure that maps keys to values.
# Tries: A tree used for storing and searching words efficiently.
# Graphs: A collection of nodes connected by edges.

# Count Marketers
def count_marketers(job_titles):
    count = 0
    for job in job_titles:
        if job == "marketer":
            count +=1
    return count

# Lists
# Append: Appending an element to the end of a list, e.g. cars.append("ford") is (on average) O(1). 
    # We go directly to the end and add the element.
# Index: Accessing an element by index, e.g. cars[2] is O(1). 
    # We go directly to the index and return the element.
# Delete: Removing an element from the middle of a list, e.g. cars.pop(2) is O(n). 
    # We have to shift all the elements after the deleted element down one index.
# Search: Searching for an element in a list, e.g. cars.index("ford") is O(n). 
    # We have to iterate over the list until we find the element.
    
def last_work_experience(work_experiences):
    if not work_experiences:
        return None
    return work_experiences[-1]

