from math import sqrt

def pythagoras():
  a = 0
  b = 0
  h = 0

  print('You will be asked to enter values for a (short side), b (short side) and h (hypotenuse). Press ENTER for the value you do not know.')
  try:
    a = float(input('a='))
  except:
    a = 0
  try:
    b = float(input('b='))
  except:
    b = 0
  try:
    h = float(input('h='))
  except:
    h = 0

  if h == 0:
    print('You said: \na=' + str(a) + '\nb=' + str(b) + '\n----' + '\nh=' + str(sqrt(a**2 + b**2)))
  else:
    if a == 0:
      print('You said: \nb=' + str(b) + '\nh=' + str(h) + '\n----' + '\na=' + str(sqrt(h**2 - b**2)))
    if a == 0:
      print('You said: \na=' + str(a) + '\nh=' + str(h) + '\n----' + '\nb=' + str(sqrt(h**2 - a**2)))
