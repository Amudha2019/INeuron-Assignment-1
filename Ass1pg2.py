#Python program to find numbers divisible by 7 not multiple of 5 between 2000 and 3200

a1=[]
for y in range(200,3201):
    if(y%7==0) and (y%5!=0):
        a1.append(str(y))
print(','.join(a1))
