# To work with the below code run the following in the terminal
# pip install objgraph

import objgraph


# Example function creating circular references
def create_circular_reference():
    a = {}
    b = {'ref': a}
    a['ref'] = b
    return a, b


a, b = create_circular_reference()

# Show most common types
print("Most common object types:")
objgraph.show_most_common_types()

# Show references to a specific object
print("\nReferences to 'a':")
objgraph.show_refs([a], filename='refs.png')
