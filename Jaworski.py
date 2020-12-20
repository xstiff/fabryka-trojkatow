import os
import time
import itertools

liczby = [] #zbior liczb
result_unq = []
x = 0
y = 0

def wejscie(error=None):      # x,y
    os.system('cls')
    errortag = "ERROR!| "
    if error:
        print(error)
        error = None
        print("\n\n")
    x = int(input("Podaj x:  "))
    y = int(input("\nPodaj y:  "))

    if x > 0 and y > 0:
        if x != y:
            if y > x:
                for p in range(x,y+1,1):
                    liczby.append(p)
                
                print("\n(",x, ";" ,y,")")
                #return(x,y)
                time.sleep(1)
                os.system('cls')
            else:
                wejscie(errortag + "Y musi byc wiekszy od X")
        else:
            wejscie(errortag + "X nie moze byc rowny Y")
    else:
            wejscie(errortag + "Obie liczby musza byc wieksze od zera")

def has_dupes(listaaa):
    for elem in listaaa:
        if listaaa.count(elem) > 1:
            return True
    return False

def unique():
    unq = set(list(itertools.combinations_with_replacement(liczby, 3))) #długości do sprawdzenia
    
    
    
    
    for item in unq:
        if has_dupes(item) == False:
            result_unq.append(item)
    #print(result_unq)

    final_check()

def final_check():
    wynik = []
    for item in result_unq:
        for x in range(0,2):
            a = item[0]
            b = item[1]
            c = item[2]
        if (a<b+c) and (b<a+c) and (c<a+b):
            wynik.append(item)
    print(wynik)
    time.sleep(0.4)
    os.system('cls')
    print("ODP: ", len(wynik))


wejscie()
start_time = time.time()
unique()
print("%s sek. " % round((time.time() - start_time),2))
time.sleep(1)