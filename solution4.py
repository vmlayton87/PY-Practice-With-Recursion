# Write code for algorithm 4 below
# Write a function that calculates the value of 'a' to the power of 'b
# technically there are fraction and negative powers, but this only handles positive whole numbers for a and b.

# a gets multiplied by itself b amount of times.
def base_exponent(a,b):
    if b==0:
        return 1
    elif b > 0:
        return a * base_exponent(a, b-1)
    else:
        return "Choose a base number that is a number, and an exponent that is a positive whole number."
print("2 to the power of 0 =", base_exponent(2,0))


print("2 to the power of 1 =", base_exponent(2,1))


print("2 to the power of 3 =", base_exponent(2,3))

print("0.5 to the power of 3 =", base_exponent(0.5,3))

print("-2 to the power of 3 =", base_exponent(-2,3))

print("2 to the power of -3 =", base_exponent(2,-3))