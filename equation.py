'''
# This program in Python solves quadratic equations of the form ax^2 + bx + c = 0.
# @author https://www.programiz.com/python-programming/examples/quadratic-roots
# @modified 26. 5. 2024, atibaut
# @version 1.1

@author: andrejt
'''

#
#

# import complex math module
import cmath

# variable values for coefficient
#a = 1
#b = 2
#c = 3

# To take coefficient input from the users (test a=1,b=1,c=-2)
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution for the quadratic equation are {0} and {1}'.format(sol1,sol2))
