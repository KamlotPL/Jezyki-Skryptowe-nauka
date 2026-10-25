"""
Zadanie 2: Interaktywny terminal bankomatu / menu operacji

Zakres materiału:
- Pętla nieskończona: while True
- Sterowanie pętlą: break (zakończenie pętli) oraz continue (przejście do nowej iteracji)
- Instrukcja dopasowania wzorca: match-case (w tym alternatywa case 1 | 2 oraz domyślny case _:)
- Operatory przypisania: +=, -=
- Formatowanie f-string

Polecenie:
1. Ustaw początkowe saldo na 1000.0 zł.
2. W pętli while True wyświetl menu:
   ====================
   1 - Sprawdź saldo
   2 - Wpłata środków
   3 - Wypłata środków
   0 - Wyjście
   ====================
3. Pobierz wybór użytkownika (skonwertuj na int lub operuj na str).
4. Za pomocą konstrukcji match ... case obsłuż wybór:
   - case 1: wyświetl bieżące saldo w formacie np. "Twoje saldo: 1000.00 zł".
   - case 2: pobierz kwotę do wpłaty. Jeśli kwota <= 0, wyświetl "Kwota musi być dodatnia!"
             i użyj instrukcji continue, aby od razu wrócić na początek pętli.
             W przeciwnym wypadku dodaj kwotę do salda (saldo += kwota).
   - case 3: pobierz kwotę do wypłaty. Sprawdź, czy kwota <= saldo:
             - jeśli tak: odejmij kwotę od salda (saldo -= kwota) i potwierdź wypłatę.
             - jeśli nie: wyświetl "Brak wystarczających środków!".
   - case 0: wyświetl komunikat pożegnalny i ZAKOŃCZ pętlę instrukcją break.
   - case _: wyświetl "Nieznana opcja, spróbuj ponownie!".

Kolokwialny Pro-Tip:
- Zwróć uwagę na typy danych przy match-case! Jeśli wczytujesz opcja = int(input()),
  twoje przypadki to case 1:, case 2: itd. Jeśli opcja = input(), to case "1":, case "2":.
- Różnica między break a continue: break wyskakuje z pętli całkowicie, continue natychmiast
  pomija resztę kodu w bieżącym obrocie i zaczyna kolejną iterację pętli od góry.
"""

# --- TUTAJ WPISZ SWÓJ KOD ---

saldo = 1000.0

