#Zad 1
paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    print("Pozostale jednostki paliwa:", paliwo)
    paliwo -= paliwo_zużyte_na_s
    czas +=1
    print("Koniec lotu")

#Zad 2

liczba=2
licznik=0
lista_pierwsza = []

while licznik < 10:
    for i in range(2,liczba):
        if liczba % i == 0:
            break
    else:
        lista_pierwsza.append(str(liczba))
        licznik +=1
    liczba +=1
print ("," .join(lista_pierwsza))

#Zad 3
print("\n")

ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
numery = [1,2,3,4,5]
mieszkania = ["/1", "/2", "/3","/4","/5","/6","/7","/8","/9","/10"]
adresses = []

for ulica in ulice:
    for numer in numery:
        for mieszkanie in mieszkania:
            print("Ulica",ulica, "Numer", numer, "mieszkanie", mieszkanie)

#Zad 4

liczba_gosci = int(input("Podaj liczbę gości: "))
liczba_straw = int(input("Podaj liczbę zamówionych potraw: "))

suma_cen = 0
licznik = 0

while licznik < liczba_straw:
    cena = float(input(f"Podaj cenę potrawy {licznik + 1}: "))
    suma_cen += cena
    licznik += 1

srednia_cena = suma_cen / liczba_straw
print(f"Średnia cena zamówionej potrawy: {srednia_cena:} zł")

rachunek_na_osobe = suma_cen / liczba_gosci
print(f"Każdy z {liczba_gosci} gości powinien zapłacić: {rachunek_na_osobe:} zł")



#Zad 5

numbers = list(range(80,-1,-4))
print(numbers)

#Zad 6

while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        print("Wprowadzono liczbę ujemną. Kończę działanie.")
        break
    else:
        print("Wprowadzona liczba to:",liczba)

#Zad 7
n = int(input("Podaj liczbę studentów: "))

suma_punktow = 0
licznik = 0

while licznik < n:
    punkty = int(input(f"Podaj liczbę punktów dla studenta {licznik + 1}: "))
    if punkty < 0 or punkty > 100:
        print("Liczba punktów spoza przedziału 0-100. Pomijam.")
        continue 
    suma_punktow += punkty
    licznik += 1
srednia = suma_punktow / n
print(f"Średnia liczba punktów w grupie wynosi: {srednia}")   

#Zad 7b
n = int(input("Podaj liczbę studentów: "))

suma_punktow = 0
licznik = 0

while True:
    punkty = int(input(f"Podaj liczbę punktów dla studenta {licznik + 1}: "))
    
    if punkty < 0 or punkty > 100:
        print("Liczba punktów spoza przedziału 0-100. Pomijam.")
        continue 
    suma_punktow += punkty
    licznik += 1

    if licznik == n:
        break
srednia = suma_punktow / n
print(f"Średnia liczba punktów w grupie wynosi: {srednia}")

#Zad 8

text = "Python jest super"

print("Znak o indeksie zerowym:", text[0])
print("Znak o indeksie ostatnim:", text[-1])
print("Znaki co drugi, zaczynając od zerowego:", text[::2])
print("Znaki co trzeci, zaczynając od pierwszego:", text[1::3])
print("Znaki od dziesiątego do ostatniego:", text[10:])  
print("Tekst od końca do początku:", text[::-1])

#Zad 9

imie = input("Podaj swoje imię: ")
print("Witaj", imie)

wiek = input("Podaj swój wiek: ")
print("Twój wiek to:", wiek)

nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0].upper() + nazwisko[0].upper()
print("Twoje inicjały to:", inicjaly)

lancuch = input("Podaj łańcuch znaków: ")
print("Łańcuch pięć razy:", lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
polaczony_lancuch = lancuch1 + lancuch2
print("Polączone łańcuchy:", polaczony_lancuch)

polowa1 = lancuch1[:len(lancuch1) // 2]
polowa2 = lancuch2[:len(lancuch2) // 2]
polaczony_polowy_lancuch = polowa1 + polowa2
print("Polączone połówki łańcuchów:", polaczony_polowy_lancuch)

