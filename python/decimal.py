

decimal = 11
result=''

while(decimal > 0):
    remainder = decimal % 2;
    decimal= int(decimal/2)
    result= str(remainder)+ result

print(result)
