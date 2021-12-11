sum=0
a=""
for i in range(40,4,-1):
    if i%2==0:
        sum+=i
        a+=(str(i)+"+")
print(a,"0=",sum)
