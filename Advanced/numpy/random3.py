#The choice() method allows you to generate a random value based on an array of values.

#The choice() method takes an array as a parameter and randomly returns one of the values.
from numpy import random
x = random.choice([3, 5, 7, 0])
print(x)