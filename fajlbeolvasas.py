from Szemely import Szemely

#itt tárolom a létrehozott osztálypéldányokat
szemeleyek_lista=[]

fajlom = open("teszt.txt", "r", encoding='utf-8')
fajlom.readline()
string_lista=fajlom.readlines()
fajlom.close()
for i in range(0,len(string_lista),1):
    #minden sort szét kell bontani
    aktsor:str=string_lista[i].strip()
    #Eltávolítjuk a asorok végéről a sortörést
    print(aktsor)
    #Jenő, férfi, 16\n - ez egy eleme a listának
    sor_lista=aktsor.split(",")
    print(sor_lista[0])
    print(sor_lista[1])
    print(sor_lista[2])

    szemely=Szemely(sor_lista[0], sor_lista[1], int(sor_lista[2]))
    szemeleyek_lista.append(szemely)

for i in range(0,len(szemeleyek_lista),1):
    print(f"{szemeleyek_lista[i].nev}, {szemeleyek_lista[i].nem}, {szemeleyek_lista[i].kor}")


import feladatok_szemelyeklistaval
atlageletkor=feladatok_szemelyeklistaval.atlageletkor(szemeleyek_lista)
print(atlageletkor)

nok=feladatok_szemelyeklistaval.nok(szemeleyek_lista)
print(f"A listában {nok} db nő szerepel.")