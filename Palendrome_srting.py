# Python program to find the Palindrome of the String using recursion.
def is_palindrome(l, r, S):
    # Base case: if the left index is greater than or equal to the right index, it is a palindrome.
    if l >= r:
        return True
    # If not, then check whether the first and last characters are the same or not.
    if S[l] != S[r]:
        return False
    # Recursive call with updated indices (moving towards the center of the string)
    return is_palindrome(l + 1, r - 1, S)

# Taking the User Input
my_string = input("Enter Your String: ")

# Initializing left and right indices for the initial check
l = 0
r = len(my_string) - 1

# Calling the function is_palindrome
check = is_palindrome(l, r, my_string)

# if-else statement is used for printing.
if check:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
