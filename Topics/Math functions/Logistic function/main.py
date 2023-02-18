import math


x = int(input())
def logistic_function(x):
    print(round(1 / (1 + math.exp(-x)), 2))

logistic_function(x)
