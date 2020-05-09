var=10
for i in range(10):
    for j in range(2,10,1):
        if var%2 ==0:
            continue
            var+=1
    var+=1
else:
    var+=1
    print(var)


f=none
for i in range(5):
    with open("data.txt","w") as f:
        if i>2:
            break
print(f.closed)
