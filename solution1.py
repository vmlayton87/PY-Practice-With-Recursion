# Write code for algorithm 1 below: 
# Write a program that takes a positive number as an argument and prints the numbers from n to zero

def count_down(n):
    if type(n) != int and type(n) != float:
        print("The value is not a number, pleas choose a number.")
    elif n < 0:
        print("The value is not a positive number, please choose a positive number.")    
    elif type(n) != int:
        print("Please choose an integer, a whole number, for the count down.")
    elif n == 0:
        print(n)
    elif n > 0:
        print(n)
        count_down(n-1)
    else:
        print("We have an error, please fix it.")


print('value of 0')
count_down(0)

print('value of 8')
count_down(8)

print('value of -4')
count_down(-4)

print('value of a string')
count_down('hello')

print('value of a decimal')
count_down(4.7)

