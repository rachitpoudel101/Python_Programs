import string
import random

if __name__=="__main__":
    # Get all the lowercase letters
    s1= string.ascii_lowercase
    
    # Get all the uppercase letters
    s2 = string.ascii_uppercase
    
    # Get all the digits
    s3 = string.digits
    
    # Get all the punctuation marks
    s4 = string.punctuation
    
    # Get the desired length of the password from user input
    passlen = int(input("Enter the password length: "))
    
    # Create an empty list `s`
    s = []
    # Extend the list `s` with all the characters from `s1`
    s.extend(list(s1))
    # Extend the list `s` with all the characters from `s2`
    s.extend(list(s2))
    # Extend the list `s` with all the characters from `s3`
    s.extend(list(s3))
    # Extend the list `s` with all the characters from `s4`
    s.extend(list(s4))
    
    # Shuffle the elements in the list `s` randomly
    random.shuffle(s)
    
    # Take the first `passlen` characters from the shuffled list `s`
    # and concatenate them into a string separated by spaces.
    # The resulting string is the generated password.
    print("".join(s[0:passlen]))