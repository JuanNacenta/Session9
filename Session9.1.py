import random

s = 0
for i in range (10):
    s += random.randint(-50,50)

print(f"The random sum is : {s}")