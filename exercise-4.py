# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# triangle = input("Enter the lengths of three side of a triangle: ")


# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length

def triangle_type(a, b, c):
  if a==b and b==c:
    triangle = 'equilateral'
    print(f'A triangle with sides of {a}{b}{c} is a {triangle} triangle')
  elif a==b or b==c or a==c:
    triangle = 'isosceles'
    print(f'A triangle with sides of {a}{b}{c} is a {triangle} triangle')
  else: 
    triangle = 'scalene'
    print(f'A triangle with sides of {a}{b}{c} is a {triangle} triangle')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

triangle_type(a, b, c)

# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
