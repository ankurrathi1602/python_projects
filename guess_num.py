# this is the game for guessing the number
import random
guess = int(input())
random_num = 0
while guess != random_num:
    random_num = random.randint(1, 9)
    if random_num == guess:
        print("exactly right", random_num)
    elif guess > random_num:
        print("too high", random_num)
    else:
        print("too low", random_num)
