import math
def nDigitPI(n):
  PI=str(math.pi)
  return PI[0:n+2]  #print Pi up to n decimal places (n+2 to include the 3.)
print nDigitPI(4)
