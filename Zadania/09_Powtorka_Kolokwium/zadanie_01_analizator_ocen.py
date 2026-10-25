"""
Zadanie 1: Analizator ocen i stypendiów

Zakres materiału:
- Wprowadzanie danych: input() oraz konwersja do float/int
- Operatory arytmetyczne: dodawanie, dzielenie
- Instrukcje warunkowe: if / elif / else oraz operatory logiczne (and, or)
- Operator ternarny (zapis jednolinijkowy: wartosc_gdy_prawda if warunek else wartosc_gdy_falsz)
- Formatowanie tekstu f-string (zaokrąglanie liczb: :.2f)

Polecenie:
1. Pobierz od użytkownika imię (jako string).
2. Pobierz od użytkownika 3 oceny ze sprawdzianów (jako liczby float).
3. Oblicz średnią arytmetyczną tych trzech ocen.
4. Wyświetl powitanie z imieniem i średnią zaokrągloną do 2 miejsc po przecinku (f-string z :.2f).
5. Za pomocą if / elif / else przypisz do zmiennej opis_oceny:
   - "Wyróżniająca" gdy średnia >= 4.5
   - "Dobra" gdy 3.5 <= średnia < 4.5
   - "Dostateczna" gdy 3.0 <= średnia < 3.5
   - "Niedostateczna" gdy średnia < 3.0
6. Za pomocą JEDNOLINIJKOWEGO OPERATORA TERNARNEGO ustal zmienną stypendium:
   "Przyznane" jeśli średnia >= 4.5, w przeciwnym razie "Brak".
7. Wypisz status oceny oraz stypendium.

Kolokwialny Pro-Tip:
- Pamiętaj: input() ZAWSZE zwraca napis (str)! Jeśli nie skonwertujesz go przez float(),
  dodawanie ocen zadziała jak łączenie napisów ('4' + '5' = '45').
- W f-stringu {srednia:.2f} zaokrągla wynik tylko wizualnie na ekranie.
"""

# --- TUTAJ WPISZ SWÓJ KOD ---

