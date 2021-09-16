# Which one is better, find(low, mid-1, answer) or # find(low, mid, answer) on line 19?
# After run 100M, the first one only very slighly better than the second. 
# I think it depends on the data distribution. 0-100 and 1-100 might get different result. 
# Amazon. 

# Another drawback: 
# if range is [4,5], then mid is 4, the next lower winder is [4,3], not intuitive
# for case like findname, we might not find anything and return -1. in that case
# range_size = (high - low) + 1
# range_size == 1:  # Base case 2: Not found
#   pos = -1
# Prefer to have range size == 1. easy to understand. 

import random
total = 0
n = 100000000

def find(low, high, answer):
    global total

    mid = (high + low) // 2
    guess = mid
    total += 1
#    print("the middle is ", mid)

    if (guess == answer):  # Base case
#        print('The answer is {}, and cumulated total counts is {}'.format(answer, total))
        return True
    else:
        if guess > answer:
            find(low, mid, answer)                      
        else:
            find(mid+1, high, answer)

for i in range(n):
    answer = random.randint(1,100)
    find(1, 100, answer)
#    print(i, find(0, 100, answer))
    
print("average guess is", total/n)    