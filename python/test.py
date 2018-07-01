list_a = ['Gachon', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b=[]

for i in range(len(list_a)):
    # print(list_a[i])
  if i%2!=1:
    list_b.append(list_a[i])
