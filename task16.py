num = 14
user_num = int(input("guess a number:"))
while user_num != num:
    print("try again")
    user_num = int(input("guess a number:"))
if user_num == num:
    print("Congrats. You guessed the number")