import numpy as np
path = 'data/ex3_data.npy'
arr = np.load(path)
print( "Number of NaN values in each column ", np.sum( np.isnan(arr), axis = 0 ))
print( "Number of rows with at least one NaN value ", sum( np.sum( np.isnan(arr), axis = 1 )>=1 )  )
filtered_arr = arr[ ~np.isnan(arr).any(axis = 1) , :]
print( "Numpy matrix after removing NaN rows\n", filtered_arr)
