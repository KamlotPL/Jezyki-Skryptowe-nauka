"""
Zadanie 3: Czyszczenie i analiza listy wyników

Zakres materiału:
- Listy: tworzenie, modyfikowalność (mutowalność)
- Płytka kopia (shallow copy: .copy() lub [:]) vs zwykła referencja (=)
- Indeksowanie ujemne (np. lista[-1], lista[-2])
- Wycinki (slicing: [start:stop], [:stop], [start:], [::step], [::-1])
- Metody list: .count(), .remove(), .append(), .pop()
- Pętla for z range() oraz parametr end w funkcji print()

Polecenie:
Dana jest początkowa lista zanieczyszczonych danych laboratoryjnych:
pomiary = [12, -999, 15, 18, -999, 20, 22, 18, 25, 30]

1. Użyj metody .count(), aby sprawdzić i wypisać, ile razy w liście pojawia się wartość -999 (kod błędu).
2. Stwórz KOPIĘ listy pomiary o nazwie czyste_pomiary (użyj .copy() lub wycinka [:]).
   * W komentarzu jednolinijkowym wyjaśnij, dlaczego NIE wolno zrobić po prostu: czyste_pomiary = pomiary.
3. Za pomocą pętli while i metody .remove() usuń wszystkie wartości -999 z listy czyste_pomiary.
   (Wskazówka: while -999 in czyste_pomiary: ...)
4. Korzystając z wycinków (slicing) na liście czyste_pomiary:
   a) Wypisz pierwsze 3 elementy.
   b) Wypisz ostatnie 2 elementy (użyj indeksów ujemnych).
   c) Wypisz całą listę odwróconą od tyłu (krok -1).
5. Za pomocą pętli for oraz funkcji range() z odpowiednim krokiem, wypisz co drugi element
   listy czyste_pomiary w jednej linii oddzielony spacją (użyj argumentu end=' ').
6. Użyj metody .pop() bez argumentu, aby usunąć i wypisać ostatni pomiar.

Kolokwialny Pro-Tip:
- Zapis b = a kopiuje jedynie WSKAŹNIK (referencję). Jeśli zrobisz b.append(100), to w 'a' też pojawi się 100!
  Aby mieć niezależną kopię, ZAWSZE używamy b = a.copy() lub b = a[:].
- .remove(x) usuwa TYLKO PIERWSZE napotkane wystąpienie x. Jeśli chcesz usunąć wszystkie,
  musisz wywołać remove w pętli.
"""

# --- DANE POCZĄTKOWE ---
pomiary = [12, -999, 15, 18, -999, 20, 22, 18, 25, 30]

# --- TUTAJ WPISZ SWÓJ KOD ---

