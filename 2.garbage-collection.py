import gc

# Enabling automatic garbage collection
gc.enable()

# Creating cyclic references
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

# Deleting references
del node1
del node2

# Forcing garbage collection
gc.collect()
