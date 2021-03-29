import random


def randInt(min=0, max=100):
    if min>max:
        return None
    if max<0:
        return None
        
    print(min,max)
    num = random.random()
    return num


print(randInt()) # should print a random integer between 0 to 100
print(randInt()) # should print a random integer between 0 to 50
print(randInt(50)) # should print a random integer between 50 to 100
print(randInt(50,500)) # should print a random integer between 50 and 500
