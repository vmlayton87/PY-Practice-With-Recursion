# Write code for algorithm 2 below:
# Write a function that prints the natural numbers from 1 to n. A natural number is a positive whole number

# setting a default for count that can be changed when the function is called again becuase since there is a default value, the original call does not need both arguments.
def natural_count_up(n, count=1):

    if type(n) != int and type(n) != float:
        print("The value is not a number, pleas choose a number.")
    elif n < 1:
        print("The value is not a natural number, please choose a positive number.")    
    elif type(n) != int:
        print("Please choose an natural number, a whole number 1 or higher, for the count down.")
    elif n > count:
        print(count)
        natural_count_up(n, count+1)
    elif n == count:
        print(n)
    else:
        print("We have an error, please fix it.")

print("value is 5")
natural_count_up(5)

print("value is -4")
natural_count_up(-4)

print("value is a string")
natural_count_up("hello")

print("value is a decimal")
natural_count_up(4.2)

print("value is 0")
natural_count_up(0)

print("value is 1")
natural_count_up(1)