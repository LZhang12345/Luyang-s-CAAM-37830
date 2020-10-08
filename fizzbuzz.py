"""
fizzbuzz

Write a python script which prints the numbers from 1 to 100,
but for multiples of 3 print "fizz" instead of the number,
for multiples of 5 print "buzz" instead of the number,
and for multiples of both 3 and 5 print "fizzbuzz" instead of the number.
"""
def printout(n):
    for i in range(1,n+1):
        # If i can be divided by 15
        if i%15 == 0:
            print('fizzbuzz')
        # If i can be divided by 3
        elif i%3 == 0:
            print('fizz')
        # If i can be divided by 3
        elif i%5 == 0:
            print('buzz')
        else:
            print(i)

printout(100)