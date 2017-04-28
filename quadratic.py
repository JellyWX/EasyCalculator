from math import sqrt

def quadformula():
  print('Enter values for a, b and c (ax^2 + bx + c = 0) by each in when prompted and pressing enter.')
  a = int(input('a='))
  b = int(input('b='))
  c = int(input('c='))

  d = ((-1*b) + sqrt((b**2) - (4*a*c)))/(2*a)
  e = ((-1*b) - sqrt((b**2) - (4*a*c)))/(2*a)

  print('x is equal to' + str(d) + ', ' + str(e))
