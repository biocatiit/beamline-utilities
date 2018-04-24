import numpy as np
import math
import sys

sourceFile = sys.argv[1]
factor = int(sys.argv[2])

def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def calculate_error(errorlist):
  variance = 0
  for i in errorlist:
    variance += i**2
  return math.sqrt(variance/len(errorlist))

number_lines =[]
f = open(sourceFile, 'r')
for line in f:
  columns = line.split()
  if len(columns) == 3:
    if (is_number(columns[0]) and is_number(columns[2]) and is_number(columns[2])):
      #print columns[0], columns[1], columns[2]
      number_lines.append(columns)

data = np.array(number_lines)
print data
rebinned = []
for i in range(0, len(data), factor):
  bin = data[i:i+factor]
  q = bin[:,0].astype(float)
  I = bin[:,1].astype(float)
  error = bin[:,2].astype(float)
  #print q, q.mean()
  #print I, I.mean()
  #print error, calculate_error(error) 
  print i
  rebinned.append([q.mean(), I.mean(), calculate_error(error)]) 

print rebinned
rebinned_data = np.array(rebinned)
np.savetxt('mer_' + sourceFile, rebinned, fmt='%.6e') 
