# analysis Module
#	- contains methods for running runtime and space complexity analyses
#	- returns data that can be used for visualization

import time


# measure runtime of a number of algorithms on a single set of data
def sorting_runtime_all(input_data, algorithms):
    results = {}
    for algorithm_name, algorithm_function in algorithms.items():
        sorted_data, time_taken = sorting_runtime_one(algorithm_function, input_data)
        results[algorithm_name] = (sorted_data, time_taken)

    # sample results value:  
    # { 'Bubble Sort': ([2, 33, 42], 3.3855438232421875e-05), 
    # 	'Bucket Sort': ([2, 33, 42], 4.00543212890625e-05), 
    #	...
    #	'Quicksort': ([2, 33, 42], 1.621246337890625e-05), 
    #	'Radix Sort': ([2, 33, 42], 3.0040740966796875e-05)	}
    return results


# measure runtime of a single algorithm on a single set of data
def sorting_runtime_one(algorithm_function, input_data):
    start_time = time.time()
    sorted_data = algorithm_function(input_data.copy())  # Make a copy to avoid modifying the original data
    end_time = time.time()

    time_taken = end_time - start_time

    return sorted_data, time_taken