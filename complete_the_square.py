import math

def CompleteSquare():
  print('Enter your equation, which should be in the format ax^2 + bx + c')
  a = int(input('Enter the `a` value'))
  b = int(input('Enter the `b` value'))
  c = int(input('enter the `c` value'))

  b = b/a
  c = c/a

  b2 = -1*(b/2)
  c2 = abs(c - (b2**2))

  print(str(b2) + ' +/- sqrt' + str(c2) + ' = x')

  ans1 = b2 + math.sqrt(c2)
  ans2 = b2 - math.sqrt(c2)

  print('answers: \n' + str(ans1) + '\n' + str(ans2))
