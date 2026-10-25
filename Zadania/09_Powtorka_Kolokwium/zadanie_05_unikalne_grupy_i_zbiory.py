"""
Zadanie 5: Unikalne grupy projektowe i operacje na zbiorach (set)

Zakres materiału:
- Zbiory (set): unikalność elementów, brak indeksowania i gwarancji kolejności
- Konwersja: lista -> zbiór (set(lista)) oraz zbiór -> lista (list(zbior))
- Modyfikacja zbiorów: metoda .add()
- Usuwanie elementów: różnica między .remove() a .discard()
- Działania na zbiorach:
  - Przecięcie / część wspólna: .intersection(inny) lub operator &
  - Suma zbiorów: .union(inny) lub operator |
  - Różnica zbiorów: .difference(inny) lub operator -
- Sprawdzanie relacji: .issubset(inny) lub operator <=

Polecenie:
Na zajęcia laboratoryjne zapisały się dwie grupy studentów (w listach występują duplikaty):
grupa_a = ["Anna", "Bartek", "Kasia", "Michał", "Anna", "Tomek"]
grupa_b = ["Kasia", "Michał", "Ola", "Piotr", "Ola"]

1. Przekonwertuj listy grupa_a i grupa_b na zbiory o nazwach set_a i set_b, eliminując duplikaty.
   Wypisz oba zbiory oraz ich rozmiary (funkcja len()).
2. Do zbioru set_a dodaj nowego studenta: "Zofia" (metoda .add()).
3. Użyj metody .discard("Nieznany_Student") na zbiorze set_a.
   * W komentarzu jednolinijkowym wyjaśnij, dlaczego użycie .remove("Nieznany_Student")
     spowodowałoby awarię programu (KeyError), a .discard() jest bezpieczne.
4. Wyznacz i wypisz:
   a) Część wspólną (studentów, którzy są zapisani do grupy A i do grupy B jednocześnie)
      - użyj metody .intersection() lub operatora &.
   b) Wszystkich unikalnych uczestników obu grup łącznie (suma)
      - użyj metody .union() lub operatora |.
   c) Studentów, którzy są TYLKO w grupie A (różnica A - B)
      - użyj metody .difference() lub operatora -.
5. Sprawdź za pomocą metody .issubset() (lub operatora <=), czy zbiór studentów wspólnych (z punktu 4a)
   jest podzbiorem grupy set_a. Wypisz wynik testu logicznego (True / False).

Kolokwialny Pro-Tip:
- Zbiory w Pythonie są niemutowalne czy mutowalne? Zbiór (set) JEST mutowalny (można dodawać i usuwać),
  ale jego ELEMENTY muszą być niemutowalne (nie można włożyć listy do zbioru!).
- Zbiór nie zachowuje kolejności ani nie ma indeksów: set_a[0] spowoduje TypeError: 'set' object is not subscriptable.
"""

# --- DANE POCZĄTKOWE ---
grupa_a = ["Anna", "Bartek", "Kasia", "Michał", "Anna", "Tomek"]
grupa_b = ["Kasia", "Michał", "Ola", "Piotr", "Ola"]

# --- TUTAJ WPISZ SWÓJ KOD ---

