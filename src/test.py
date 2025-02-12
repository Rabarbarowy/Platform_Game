def elo(n):
    szukana = n
    mnoznik = 1
    nieparzysta = 0
    m = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 10
        else:
            nieparzysta = n % 10
            m = nieparzysta * mnoznik + m
            mnoznik = mnoznik * 10
            n = n // 10

    if m == 0:
        return szukana
    else:
        return

def siema():
    szukane_liczby = []
    ilosc_liczb = 0
    najwieksza_liczba = 0
    plik =open('/home/krzysztof/Pobrane/informatyka-2024-maj-matura-rozszerzona-zalaczniki/Dane-NF-2405/skrot.txt', 'r')
    for i in plik:
        szukane_liczby.append(elo(int(i)))

    for i in szukane_liczby:
        if i:
            ilosc_liczb += 1
            if najwieksza_liczba < i:
                najwieksza_liczba = i

    print('Ilość liczb:' + str(ilosc_liczb))
    print('Najwieksza liczba:' + str(najwieksza_liczba))

siema()
