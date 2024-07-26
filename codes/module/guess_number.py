import random
a = False
while a != True:
    guess_num= int(input("Guess a number between 1 and 10 \ until you get it right:"))
    target_num= random.randint(1,10)
    print(target_num)
    if guess_num == target_num:
        a = True
        pass
    else:
        a = False
print('Well guessed!')
             
