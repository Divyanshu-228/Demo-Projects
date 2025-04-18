#Number Guessing Game

print("--- A TWO PLAYER GAME ---")
print("\n----- Player 1 -----")

num = int(input("Enter a number here: "))
print("\n"*50)

print("\n--- Player 2 Turn now---")
attempts = 0
max_attempts = 8

while True:
    print(f"\nYou have {max_attempts-attempts} attempts!!")
    if max_attempts==attempts:
        break
    usr = int(input("Guess the number : "))
    attempts +=1
    if (usr == num):
        print("Congrats!!...your guess is Correct!!\n")
        break
    elif(usr < num-50):
        print("Think Big Bro!!")
    elif(usr > num+50):
        print("You have gone too far!!") 
    elif(usr < num-15):
        print("Too Low!!")
    elif(usr > num+15):
        print("Too Big")
    elif(usr in range(num-15,num)):
        print("keep trying ... litte bit more")
    elif(usr in range(num+1,num+15)):
        print("keep trying ... litte bit less")
        
if max_attempts==attempts and usr !=num:
    print("\nBetter Luck next time!!\n")
