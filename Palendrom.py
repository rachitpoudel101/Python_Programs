# Python program for the number is Palenfrom or not?

#Taking the Input form the user

num = int(input("Enter number: "))
#Put the value of the num in the Temp
temp = num
#At first the reverse is Zero
rev = 0

#Adding the While loop 

while temp > 0 :
    # Dividing the last digit from the number and storing it into the variable remainder
    remainder = temp % 10
    # Adding the remainder to the reversed number
    rev = (rev * 10) + remainder
    temp//= 10 # It perform division and round up to nearest interger.

#Now Adding the IF ELSE comdition  And printing it.
if num == rev:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")