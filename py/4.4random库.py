import random
#[0,1)
random.seed(10)
print(random.random())
print(random.random())
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
print(random.random())

print(random.randint(10,100))

print(random.randrange(10,100,10))

print(random.getrandbits(16))

print(random.uniform(10,100))

print(random.choice([1,2,3,4,5]))

s = [1,2,3,4,5,6,7,8,9]
random.shuffle(s)
print(s)

