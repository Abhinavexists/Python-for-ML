'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import multiprocessing.pool
import sys
import time

# Increasing the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorial of a given number
def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)

if __name__=="__main__":
    numbers=[5000,6000,700,8000]

    start_time = time.time()

    # create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)

end_time = time.time()