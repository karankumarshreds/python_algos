# r = range && n = num 
def div(r, n):
  spam = []
  result = []
  for i in range(1,r):
    spam.append(i)
  for i in spam:
    if i % n == 0:
      result.append(i)
  return result

print(div(100,5))
      

