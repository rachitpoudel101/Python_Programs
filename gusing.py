import random
num = random.randint(1, 10)
guess =None

while guess != num:
    guess =input("guess the number betweeen 1-10: ")
    guess = int (guess)
    
    if guess == num:
        print("Congratulation !! You have guess the right nuber")
    else:
        print("Please try again !!!!!......")