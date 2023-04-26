import random
# swap two variables by using a temporary variable and, 
# without using temporary variable

# temp variable
a = random.seed(7)
b = 3

# create temp variable and swap values
temp = a
a = b
b = temp

print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))

#w/o temp variables
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)