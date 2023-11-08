# to import build in function just
# import math
# print(dir(math))
from math import sqrt
# from math import * # for all the function
print(sqrt(4))

# to take print the sum of two using function
def add_Numbers(num1,num2 = 3):
    print(num1 + num2)

# add_Numbers(3,4)
# if not pass we can set default also
add_Numbers(3)