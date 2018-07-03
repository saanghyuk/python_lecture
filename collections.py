


cs50_cafe = {"greentea":32, "coffee":25, "chocolate":17, "icecream":59}

a = cs50_cafe.items()
b = cs50_cafe.keys()
c = cs50_cafe.values()


Mydict = { '1' : 1, '2' : 2 }
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print (result)
