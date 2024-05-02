# Write code for algorithm 5 below:
# Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

# A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.

# w3schools.com
# slicing a part of a string use string[index1:index2], not including index1, but not including index2 
# Use negative indexes to start the slice from the end of the string. -1 is the last character.

def palindrome(string):
    # print(string)
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        # print(string[1:-1])
        return palindrome(string[1:-1])

print("a is a palindrome:", palindrome('a'))
print("at is a palindrome:", palindrome('at'))
print("racecar is a palindrome:", palindrome('racecar'))
print("noon is a palindrome:" , palindrome('noon'))
print("welcome is a palindrome", palindrome('welcome'))