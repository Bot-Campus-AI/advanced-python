import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

# Example function with memory allocations
def example_function():
    a = [i for i in range(10000)]
    b = [i * 2 for i in range(10000)]
    return a, b

example_function()

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

# Stop tracing memory allocations
tracemalloc.stop()
