"""
Zadanie 4: Magazyn i zliczanie koszyka produktów

Zakres materiału:
- Słowniki (dict): tworzenie par {klucz: wartosc}, unikalność i niezmienność kluczy
- Metody słowników: .get(), .items(), .keys(), .values(), .update()
- Krotki (tuple): niezmienność, rozpakowywanie (unpacking)
- Pętle iterujące po słownikach

Polecenie:
Dany jest cennik sklepu:
cennik = {
    "chleb": 4.50,
    "mleko": 3.20,
    "jajka": 10.00,
    "ser": 8.50
}

Oraz lista produktów wrzuconych do koszyka przez klienta:
koszyk = ["mleko", "chleb", "mleko", "jajka", "mleko", "czekolada"]

1. Utwórz pusty słownik o nazwie zliczenia.
2. Przejdź pętlą for po liście koszyk i zlicz, ile razy każdy produkt występuje w koszyku.
   * UWAGA: Zastosuj metodę zliczenia.get(produkt, 0) + 1, aby bezpiecznie dodawać elementy
     bez wyrzucenia błędu KeyError.
3. Przejdź pętlą for po parach (produkt, ilosc) ze słownika zliczenia za pomocą metody .items():
   * Dla każdego produktu pobierz jego cenę z cennika metodą cennik.get(produkt, 0.0).
   * Oblicz koszt cząstkowy (ilosc * cena) i dodaj do sumy całkowitej.
   * Jeśli cena wynosiła 0.0 (produkt niedostępny w cenniku, np. czekolada), wypisz ostrzeżenie:
     f"Produkt '{produkt}' jest niedostępny w cenniku!"
   * Wypisz podsumowanie pozycji: f"{produkt}: {ilosc} szt. x {cena:.2f} zł = {koszt_czesciowy:.2f} zł"
4. Wypisz łączny koszt całego koszyka (zaokrąglony do 2 miejsc po przecinku).
5. Dodaj do słownika cennik nowość za pomocą metody .update():
   nowe_produkty = {"czekolada": 6.00, "kawa": 18.50}

Kolokwialny Pro-Tip:
- Dlaczego krotka może być kluczem w słowniku, a lista NIE może?
  Klucz w słowniku musi być NIEZMIENNY (hashable). Lista jest mutowalna (można zmieniać jej elementy),
  a krotka (tuple) jest niezmienna (immutable)!
- cennik["czekolada"] powoduje błąd programu KeyError, jeśli klucza nie ma w słowniku.
  cennik.get("czekolada", 0.0) bezpiecznie zwróci 0.0 bez błędu.
"""

# --- DANE POCZĄTKOWE ---
cennik = {
    "chleb": 4.50,
    "mleko": 3.20,
    "jajka": 10.00,
    "ser": 8.50
}

koszyk = ["mleko", "chleb", "mleko", "jajka", "mleko", "czekolada"]

# --- TUTAJ WPISZ SWÓJ KOD ---

