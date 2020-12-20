  #Kategoria: Gremliny (Szkoła Średnia) 
  #Język programowania: C++/Python 
  #Fabryka trójkątów 

Dział kontroli jakości w fabryce trójkątów borykał się od dawna z problemami spędza jącymi sen z powiek dyrekcji. Wysoki popyt i stale rosnące zapotrzebowanie powinny właściwie stanowić powód do optymizmu – trójkąty potrzebne są bowiem wszędzie, od pomocy naukowych i podręczników do matematyki, przez odblaskowe trójkąty ostrzegaw cze, na komputerowej grafice 3D (opartej na siatkach wielokątów) kończąc. Nie zmieniało to jednak faktu, że z pewnych tajemniczych powodów duża część produkcji nie spełniała nawet elementarnych kryteriów jakościowych i lądowała w koszu, powodując znaczne straty finansowe i frustrację wśród pracowników. 
Nowo zatrudniony kierownik działu postanowił zmierzyć się z tym problemem i po wielu bezsennych nocach, w wyniku przeprowadzonych analiz i symulacji odkrył wreszcie straszną prawdę – z niektórych zestawów odcinków po prostu nie da się skonstruować trójkąta! Powołany w trybie pilnym sztab kryzysowy ustalił ponad wszelką wątpliwość, że z odcinków o długościach a, b, c, takich że a < b < c, można zbudować trójkąt tylko wtedy, gdy a + b > c. 
Aby w pełni ocenić powagę sytuacji, kierownik postanowił sprawdzić ile trójkątów da się zbudować przy założeniu, że dział zaopatrzenia dostarcza odcinki o długościach będących liczbami całkowitymi z pewnego przedziału. 

  #Zadanie
Wyznacz maksymalną liczbę różnych trójkątów, które można zbudować z różnych boków o długościach całkowitych pochodzących z zadanego przedziału [x, y]. 

  #Opis wejscia ´ 
Na standardowym wejściu znajdują się dwie liczby całkowite x, y zapisane w oddzielnych wierszach (0 < x < y < 10 000), określające krańce przedziału, z którego pochodzą długości odcinków do konstrukcji trójkątów. 

