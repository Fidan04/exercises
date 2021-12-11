x=int(input("Enter x: "))
y=int(input("Enter y: "))

for a in range(x, y+1):
    sum=0
    for i in range(1, a//2+1):
        if a%i==0:
            sum+=i

    if sum==a:
        print(a,"is perfect")

