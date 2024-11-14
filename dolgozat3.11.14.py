lista=[]

with open("ajandek.txt", "r", encoding="UTF-8") as file:
    next(file)
    for sor in file:
        item= sor.strip()
        item= sor.split(";")
        nev= item[0]
        osszeg= int(item[2])
        akcio=int((osszeg* 0.8))
        lista.append((nev,osszeg,akcio))

print(f"Ajándék lista teljes tartalma:")

for elem in lista:
    print(f" {elem[0]}, {elem[1]}, akciós ár: {elem[2]}")

legifjabb=("Béres Zoltán", 1996)
print(f"\nA legfiatalabb: {legifjabb[0]}, születési év: {legifjabb[1]}")

kategoria= set(item[1] for item in lista)
print("\nA a kategóriák száma:", {len(kategoria)})

print("\nNevek, összegek és akciós árak (20% kedvezmény):")

for elem in lista:
    print(f"{elem[0]}, eredeti ár: {elem[1]} Ft, kedvezményes ár: {elem[2]}")


with open("szbetuvelkezd.txt", "w", encoding="UTF-8") as file:
    for elem in lista:
        print(elem)
        nev=elem[0]
        if nev.lower().startswith("sz"):
            file.write(nev + "\n")
    file.write("\nSz-el kezdődő nevek mentve a szbetuvelkezd.txt fajlba.")
