import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
}
data_frame = pd.DataFrame(data)


# Defining a custom function
def custom_function(x):
    return x * 2 if x % 2 == 0 else x * 3


# Applying the custom function to each element using apply
custom_transformed = data_frame.map(custom_function)
print("\nDataFrame after Applying Custom Function:\n", custom_transformed)



