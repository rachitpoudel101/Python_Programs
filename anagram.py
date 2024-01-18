# Taking String Input from the user
str1 = input("Enter the First String: ")
str2 = input("Enter the Second String: ")

# Convert the Strings into lowercase using .lower()
str1 = str1.lower()
str2 = str2.lower()

# Checking if the length is the same or not using len()
if len(str1) == len(str2):
    # Sort the strings in array form
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Using the IF-ELSE statement after sorting the strings in array form
    if sorted_str1 == sorted_str2:
        print(f"{str1} and {str2} are anagrams.")
    else:
        print(f"{str1} and {str2} are not anagrams.")
else:
    print("The length of both strings should be the same.")
