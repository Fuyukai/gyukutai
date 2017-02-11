# The two lines to ruin it all.
import gyukutai
gyukutai.apply()

from math import sqrt

# apply
print("Squares of the first 10 integers:", range(1, 11).apply | (lambda x: x ** 2))

# find
print("First square number:", range(2, 100).find | (lambda x: sqrt(x) % 1 == 0))

# filter
print("Factors of 234:", range(0, 234).filter | (lambda x: x != 0 and 234 % x == 0))

# sample
print("Random number [0, 1000):", range(0, 1000).sample)
