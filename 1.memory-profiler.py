# To work with the below code run the following in the terminal
# pip install memory_profiler

import sys
from memory_profiler import memory_usage


# Example function to monitor memory usage
def example_function():
    a = [i for i in range(10000)]
    print("Memory usage of list a:", sys.getsizeof(a))


if __name__ == '__main__':
    mem_usage = memory_usage((example_function,))
    print("Memory usage during the function execution:", mem_usage)
