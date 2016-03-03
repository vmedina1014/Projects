import math
def nDigitPI(number):
  PI=str(math.pi)
  return PI[0:number+2]
print nDigitPI(4)
