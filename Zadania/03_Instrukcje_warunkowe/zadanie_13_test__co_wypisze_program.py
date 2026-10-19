"""
Zadanie 13: Test: co wypisze program?

Bez uruchamiania określ wynik i sprawdź:

 x = 7
 if x > 5:
     print("A")
 if x > 6:
     print("B")
 elif x > 3:
     print("C")
 else:
     print("D")
 print("E") if x % 2 == 0 else print("F")
 y = "big" if x > 10 else "mid" if x > 5 else "small"
 print(y)
 print(not(x > 2 and x < 5), 2 < x < 8, x == 7 or 1/0)

 Wyjaśnij, dlaczego ostatnia linia nie zgłasza ZeroDivisionError (skrócona ewaluacja).
"""

