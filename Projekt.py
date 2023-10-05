hosszusag=["mm","cm","dm","m","km"]
#a következőbe (jobbra lévóbe) mennyi a vátószám
hosszertek=[10,10,10,1000,1]

terulet=["mm2","cm2","dm2","m2","km2"]
#a következőbe (jobbra lévóbe) mennyi a vátószám
teruletmertek=[100,100,100,1000000,1]

terfogat=["mm3","cm3","dm3","m3","km3"]
#a következőbe (jobbra lévóbe) mennyi a vátószám
terfogatmertek=[1000,1000,1000,1000000000,1]

repeat="igen"
while(repeat=="igen"):
    #szám bekérés
    #szám ellenörzés, típus kiderítés
    rossz=True
    while rossz:
        try:
            szam=float(input("Írj be egy számot:"))
            rossz=False
        except:
            print("Ez nem jó˘!")

    #me bekérés        

    rossz=True
    while rossz:
        me1=input("Mértékegység:")
        #me ellenörzés, típus kiderítés
        if me1 in hosszusag:
            rossz=False
        else:
            print("Ismeretlen mértékegység: "+me1)

    #me bekérés

    rossz=True
    while rossz:
        me2=input("Mértékegység amibe szeretnéd:")
        #me ellenörzés, típus kiderítés
        if me2 in hosszusag:
            rossz=False
        else:
            print("ismeretlen mértékegység: "+me2)
    #kiszámítás

    me1in = hosszusag.index(me1)
    me2in= hosszusag.index(me2)
    #print(me1in,me2in)

    #print(hosszertek[me1in:me2in])

    if me1in<me2in:
        szorzo=1
        for valto in hosszertek[me1in:me2in]:
            szorzo= szorzo * valto

        szam=szam/szorzo
    else:
        szorzo=1
        for valto in hosszertek[me2in:me1in]:
            szorzo= szorzo * valto

        szam=szam*szorzo

    #kiírás
    print(szam,me2)
    #újra?

    repeat=input("Újra? (igen/nem)")
