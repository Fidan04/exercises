# nPr= n!/(n-r)!
n=int(input("Enter n: "))
r=int(input("Enter r: "))


# def faktoriyal(n):
#     n_f=1
#     for i in range(n,0,-1):
#         n_f*=i
#     return n_f

# P=faktoriyal(n)/faktoriyal(n-r)
# print(P)

def faktoriyal_rek(n):
    if n==1:
        return n
    else:
        return n*faktoriyal_rek(n-1)

#print(faktoriyal_rek(5))
P=faktoriyal_rek(n)/faktoriyal_rek(n-r)
print(P)

def ededler(n,m):
    for i in range(n,m):
        print(i)

ededler(1,10)


    