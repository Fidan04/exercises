#7
say=0
say1=0
a=0
b=0
for i in range(1,1000):
    if i%5==0:
        say+=1
        a=i+a
        print("{0} 5-e tam bölünür".format(i))
    if i%7!=0:
        say1+=1
        b=i+a
        print("{0} 7-ye tam bölüne bilmir".format(i))
        
print("toplam", a)
print("toplam", b)