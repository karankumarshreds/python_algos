list = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for i in range(0,len(list)):
  sum = sum + list[i]

print('Average: '+ str(sum/len(list)))
