sikeres= False
while not sikeres:
    szam= int(input("Kérek egy egyjegyű pozitív számot(0-9):"))
    if szam > 0 and szam <=9:
        if szam % 2 ==0: 
            print(f"A bekért szám {szam} páros.")
        sikeres= True
    else:
      print(f"A bekért szám {szam} páratlan.")
      sikeres=True
      

