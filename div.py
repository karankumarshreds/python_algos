def div(lower, upper, divide):
  empty = []
  for i in range(lower, upper):
    if i % divide == 0:
      empty.append(i)
  return empty

print(div(1,50,5))
