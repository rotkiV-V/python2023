for i in range(10):
    negyzet= i ** 2
    print(i,negyzet)
print()
print("2.feladat")
print()
for x in range(100):
    negyzet2= x ** 2
    if 1000>negyzet2>99:
        print(x,negyzet2,end="\t")
print()
print("3.feladat")
print()

for y in range(20):
    if y%2==0:
        print(y,end="\t")

print()
print("4.feladat")
print()

for v in range(100,201):
    if v%5==0:
        print(v,end="\t")

print()
print("5.feladat")
print()

darab=0
szam=0
for z in range(100,1001):
    darab+=1
    szam+=1
    if darab==1000:
        szam-100
    print(szam)
    





