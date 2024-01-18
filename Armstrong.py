#Pyhton program to find the Armstrong number 

#Take the input from the user

num = int(input("Enter a Number: "))

#initize the sum

sum = 0
#Find the sum of the cube of each digit

temp = num

# applying the while loop 
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp//= 10 # It perform division and round up to nearest interger.

#Display the Result

if num == sum:
    print("%d is an Armstrong number" % num)
else:
    print("%d is not an Armstrong number" % num)