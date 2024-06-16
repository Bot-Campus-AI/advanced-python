import sys

# Creating an object
a = [1, 2, 3]
print("Reference count of a:", sys.getrefcount(a))

# Creating another reference to the object
b = a
print("Reference count after creating b:", sys.getrefcount(a))

# Deleting a reference
del b
print("Reference count after deleting b:", sys.getrefcount(a))
