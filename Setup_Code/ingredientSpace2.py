import csv
import json
import numpy as np

all_data = np.loadtxt("recipesnocomma.csv", skiprows=1, dtype=object, delimiter=",")
all_data = all_data[:, 1:]
all_data = all_data.astype(np.float32)
result_arr = []

for i in range(len(all_data[0])-1):
   filtered_recipes = (all_data[all_data[:, i] == 1]) # generates a vector of ones for every row in the columns, and returns a vector of booleans
   sum_filter = np.sum(filtered_recipes, axis=0)/(len(filtered_recipes[:, 0]))
   print(sum_filter)
   result_arr.append(sum_filter,)

final_result = np.stack(result_arr)
swap_result = result_arr.T
print(final_result)
   # Save Numpy array to csv
np.savetxt('array.csv', swap_result, delimiter=',', fmt='%f')