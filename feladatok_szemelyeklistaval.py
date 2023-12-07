# Készíts metódusat, mely kiszámolja a személyek átlag életkorát

def atlageletkor(lista:[]):
    osszeg:int=0
    for i in range(0,len(lista),1):
        osszeg += lista[i].kor

    return osszeg/len(lista)

# Készíts metódust, mely megmondja a listában lévő nők számát
def nok(lista:[]):
    szamuk:int=0
    for i in range(0,len(lista),1):
        if lista[i].nem == " nő":
            szamuk += 1
    return szamuk