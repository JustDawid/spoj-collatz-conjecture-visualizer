# Problem Collatza (PTCLTZ) - Wizualizacja

## Opis
Prosty skrypt w Pythonie demonstrujący działanie **Hipotezy Collatza** (znanej również jako problem $3x + 1$).
Jest to wizualizacja rozwiązania problemu [SPOJ PTCLTZ](https://pl.spoj.com/problems/PTCLTZ/).

## Na czym polega problem?
Dla dowolnej liczby naturalnej $x > 0$:
1.  Jeśli $x$ jest parzyste, dzielimy je przez 2.
2.  Jeśli $x$ jest nieparzyste, mnożymy przez 3 i dodajemy 1.

Program wypisuje każdy krok tej sekwencji, aż liczba osiągnie wartość 1.

## Uruchomienie
```bash
python main.py
