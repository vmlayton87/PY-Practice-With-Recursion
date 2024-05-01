# Write code for algorithm 3 below:
# Write a function that returns the nth elements in the Fibonacci Sequence.

# The Fibonacci Sequence is the series of numbers where the next number is found by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# For example, if n=4, then the result would be '2' and if n=2, the result would be '1'
# Here is more information on the Fibonacci Sequence: https://www.mathsisfun.com/numbers/fibonacci-sequence.html

# fibonacci seqence takes the two previous values and adds them together: f(1)=0, f(2)= F(1)+ 1, f(3)= f(2)+ f(1), f(n)=f(n-1)+f(n-2)

def nth_fib_element(n):
    if type(n) != int and type(n) != float:
        print("The value is not a number, pleasechoose a number.")
    elif n < 1 or type(n) != int :
        print("The value is not a positional number, please choose a whole number of 1 or larger.")    
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib_element(n-1) + nth_fib_element(n-2)

print("testing errors:")
print("a negative number:" , nth_fib_element(-1))
print("a string:", nth_fib_element("hello"))
print("0:", nth_fib_element(0))

print("the fibonacci sequence:") 
print(nth_fib_element(1))
print(nth_fib_element(2))
print(nth_fib_element(3))
print(nth_fib_element(4))
print(nth_fib_element(5))
print(nth_fib_element(6))
print(nth_fib_element(7))
print(nth_fib_element(8))