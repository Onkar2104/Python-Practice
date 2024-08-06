#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9)
from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 7))
print(x)