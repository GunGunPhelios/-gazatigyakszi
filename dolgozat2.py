szavak = ["A", "nap", "ragyog", "az", "égen", "és", "a", "madarak", "vidáman", "csiripelnek", "a", "fákon", "amíg", "az", "emberek", "sétálnak", "a", "parkban", "és", "élvezik", "a", "szép", "időt", "tavasz", "tarka", "tulipánok", "tündökölnek"]


while True:
    bekérés=input("Kérek egy szót: ")
    if len(bekérés)>3: 
        szavak.append(bekérés)
    break

tbetusszavak=[szo for szo in szavak if szo.lower().startswith("t")]

print(f"A hozzáadott szó: {bekérés}")
print(f"A t-vel kezdődő szavak száma: {len(tbetusszavak)}")
print(f"A T-vel kezdődő szavak:{";".join(tbetusszavak)} ")

