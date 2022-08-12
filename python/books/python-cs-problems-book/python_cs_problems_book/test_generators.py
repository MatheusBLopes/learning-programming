# a_list = [x for x in range(10)]

# for i in a_list:
#     print(i)



list_gener = (x for x in range(10))

print(next(list_gener))
print(next(list_gener))

for i in list_gener:
  print(i)
