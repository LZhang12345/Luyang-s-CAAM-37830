# Answers

Put any answers to questions in the assignment in this file, or any commentary you don't include in the code.

This is a markdown file (the `.md` extension gives it away). If you have never used markdown before, check out [this short guide](https://guides.github.com/features/mastering-markdown/).

## Problem 0
You don't need to say anything here.  Just complete [`fizzbuzz.py`](fizzbuzz.py).

## Problem 1
⌊log2(n)⌋ +(o(n) − 1)
Here ⌊log2(n)⌋ is due to the total recursion; and the (o(n) − 1) is beacause of the odd case where a is added

## Problem 2
The first function fibonacci_recursive's time complexity is exponential while the second fibonacci_iter is linear.
I expect the second one will be faster since the exponential running time is much larger than the linear one with the number of operations increase. Also, iteration is generally faster than the recursion since recursion takes much more memory space

## Problem 3
In this problem, I replaced the multiplicaton in matrix by the Egyptian algorithm so the time complexity is o(log2(n)).
I used for loop to iterate through every element in the matrix to multiply and add each element.
For fibonacci_recursive, time complexity is o(n^2)
Since there're many multiplications for given matrix, at the beginning, fibonacci_power will underperform fibonacci_iter and fibonacci_recursive,
However, when the n increases to a large number, fibonacci_power will outperform both fibonacci_iter and fibonacci_recursive.

The potential issue is that, when running into large number, if we use float64, the program tends to overflow 
So it's better to use float64 since it can hold much larger value

## Problem 4
image:
So the graph can verify the guess in the last question. We can see the running time for fibonacci_power is the largest in the beginning,
but later, the fibonacci_iter went so high since it called many recursions and with n increases, the gap between fibonacci_iter and fibonacci_power is closing,
if we have even larger n, eventually, the fibonacci_power will outform fibonacci_iter. 

## Feedback
