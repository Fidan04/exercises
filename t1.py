"""
#1
for i in range (0,12,3):
    i**=3
    print(i)
    
 """
"""
#3    
a=int(input("Enter a number: "))
a_f=1

for i in range(1,a+1):
    a_f=a_f*i
    
print(a_f)

"""

"""
#4
for a in range(1,500):
    if a!=1:
        for i in range(2,a):
            if (a%i)==0:
                print("{0} asal sayı değil".format(a))
        else:
            print("{0} asal sayıdır".format(a))
            
"""

"""
#5
a=int(input("Enter a: "))
b=int(input("Enter b: "))
for i in range(a, b+1):
    print(i)

"""

#6
a=0
for i in range(40,4,-1):
    if i%2!=0:
        break
    else:
        a+=i
print(a)