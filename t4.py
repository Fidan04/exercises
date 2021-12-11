#abc==a**3+b**3+c**3 

for i in range(100,1000):
    a=i//100
    b=(i//10)%10
    c=i%10
    kub=a**3+b**3+c**3
    
    if i==kub:
        print(i)