import math
print("1.feladat")
print()
a=float(input("1.befogó:"))
b=float(input("2.befogó:"))
c=a**2+b**2
c2=math.sqrt(c)
print(math.sqrt(c))
c2=math.sqrt(c)
print(c2%1.0)
print(1.5%1==0)
print(c2%1==0)


print("2.feladat")

for a in range(1,100):
    for b in range(a,100):
        c=math.sqrt(a*a+b*b)
        if c%1==0:
            if b-a>=10:
                print(a,b,int(c))






        
