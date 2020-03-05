def rev(a):
  x = []  
  y = ''

  for i in str(a):
    x.append(i)
  for i in range(0,len(x)):
    y = y+ str(((x[(len(x)-1 )-i])))
  
  return int(y)

print(rev(123456789))

#### short way #### 

a = 123456
rev = 0 

while (a>0):
  last = a % 10 
  rev = rev * 10 + last
  a = a//10

print(rev) 
