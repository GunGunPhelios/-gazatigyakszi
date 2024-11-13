lista=[]

with open("cuki.txt", "r", encoding="UTF8") as fajl:
    sorok= fajl.readlines()
    
    for sor in sorok:
     sor=sor.strip()
     sor= sor.split(";")

     nev= sor[0]
     típus= sor[1]
     értéke= int(sor[2])
     lista.append([nev,típus,értéke])
megszamol=0
for item in lista:
    #  print(f"{item[0]}, {item[1]}, {item[2]}")
   if item[1]=="vegyes":
        megszamol+=item[2]
        print(megszamol)

with open ("akciostortak.txt", "w", encoding="UTF8") as file:
    for akcio in lista:
       if akcio[2]< 10000:
          osszeg= akcio[2] - (akcio[2] * 0.1)
          file.write(f"/n {akcio[0]}, {round(osszeg)}")





print(f"A cuki.txt-ben összesen {len(lista)} setemény található")
print(f"A vegyes setemények ára összesen {megszamol} Ft.")


