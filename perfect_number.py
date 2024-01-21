# Get user input for the number
n = int(input("Enter a number: "))
sum = 0

# Calculate the sum of divisors
for i in range(1, n):
    if n % i == 0:
        sum = sum + i

# Check if the number is a perfect number
if sum == n:
    print(f"{n} is a Perfect number")
else:
    print(f"{n} is not a Perfect number")
