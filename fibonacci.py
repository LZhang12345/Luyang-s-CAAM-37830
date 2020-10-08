"""
fibonacci

functions to compute fibonacci numbers

Complete problems 2 and 3 in this file.
"""

import time # to compute runtimes
from tqdm import tqdm # progress bar
import numpy as np
import matplotlib.pyplot as plt

# Question 2
"""
The recursion: f(n) = f(n-1) + f(n-2), note the special case here(when n <= 1)
"""
def fibonacci_recursive(n):
    if n > 1:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    else:
        return n

"""
The iteration is simplier since it just follow the instruction from homework,
using the for loop to iterate and get the answer
"""
# Question 2
def fibonacci_iter(n):
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, a+b
    return b

"""
In this function, since we have to use the egyptian_multiplication, 
so I chose not to use numpy.dot, instead, it used for loop to iterate through the entire
matrix and multiply each element (using egyptian_multiplication to perform mulitplication of numbers),
then get the new matrix
"""
# Question 3
def fibonacci_power(n):
    """
    Here I use np.float64 since it will can store the larger number than int64
    a changes with iteration but base never changes
    """
    a = np.array([[1,1],[1,0]], dtype=np.float64)
    
    base = np.array([[1,1],[1,0]], dtype=np.float64)
    d = np.array([1,0], dtype=np.float64)
    e = np.array([0,0], dtype=np.float64)
    """
    Iterate from 1 to n, like a^n
    """
    for i in range (1,n):
        # Create a new array to store the newly generated array
        c = [[0,0],[0,0]]
        #Itereate through the new 2*2 matrix
        for i in range(np.size(c,1)):
            for j in range(np.size(c,0)):
                for k in range(np.size(c,0)):
                    # Here calling the egyptian_multiplication
                    c[i][j] += egyptian_multiplication(a[i][k], base[k][j])
        for i in range(np.size(c,1)):
            for j in range(np.size(c,0)):
                a[i][j] = c[i][j]  
    # Compute a^n * [1,0]T
    for i in range(np.size(a,0)):
        for k in range(np.size(e)):
            e[i] += egyptian_multiplication(a[i][k], d[k])
    return e[1] 

"""
Here calling the original egyptian_multiplication function
"""
def egyptian_multiplication(a, n):
    def isodd(n):
        return n & 0x1 == 1
    if n == 1:
        return a
    if n == 0:
        return 0
    if isodd(n):
        return egyptian_multiplication(a + a, n // 2) + a
    else:
        return egyptian_multiplication(a + a, n // 2)

if __name__ == '__main__':
    """
    this section of the code only executes when
    this file is run as a script.
    """
    def get_runtimes(ns, f):
        """
        get runtimes for fibonacci(n)

        e.g.
        trecursive = get_runtimes(range(30), fibonacci_recusive)
        will get the time to compute each fibonacci number up to 29
        using fibonacci_recursive
        """
        ts = []
        for n in tqdm(ns):
            t0 = time.time()
            fn = f(n)
            t1 = time.time()
            ts.append(t1 - t0)

        return ts

    #print the first 30 numbers 
    for i in range(1,31):
        print("{} number: fibonacci_power {}; fibonacci_recursive {}; fibonacci_iter {}".format(i,fibonacci_power(i), fibonacci_recursive(i), fibonacci_iter(i)))

    nrecursive = range(35)
    trecursive = get_runtimes(nrecursive, fibonacci_recursive)

    niter = range(10000)
    titer = get_runtimes(niter, fibonacci_iter)

    npower = range(10000)
    tpower = get_runtimes(npower, fibonacci_power)

    
    ## write your code for problem 4 below...
    # use plt to plot three line in the same graph
    plt.loglog(nrecursive,trecursive, label = 'nrecursive')
    plt.loglog(niter,titer, label = 'niter')
    plt.loglog(npower,tpower, label = 'npower')
    # put the legent in the upper left
    plt.legend(loc="upper left")
    # assign x and y label
    plt.xlabel("number of iteration")
    plt.ylabel("time")
    # assign the title
    plt.title("Running speed for each method")
    plt.show()