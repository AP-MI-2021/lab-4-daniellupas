def printMenu():
    print("1.Citire lista")
    print("2.Afișarea listei după eliminarea numerelor prime din listă")
    print("3.Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
    print("4.Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
    print("5.Cerinta 4")
    print("x.Iesi din program")


def citire_lista():
    '''
    Folosind aceasta functie citim o lista
    :return: lista citita
    '''

    lst =[]
    givenString = input("Introduceti elementele listei insirate prin virgula: ")
    numbersAsStrig = givenString.split(",")

    for x in numbersAsStrig:
        lst.append(int(x))
    return lst


def is_prime(x):
    """
    Determina daca un numar este sau nu este prim.
    :return:returneaza True daca numarul  este prim, sau False in caz contrar.
    """
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
            break
    return True

def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(22) == False
    assert is_prime(1) == False

def afisare_lista_fara_el_prime(lst):

    rezultat=[]
    for i in lst:
        if is_prime(int(i)) == False:
            rezultat.append(i)
    return rezultat

def test_afisare_lista_fara_el_prime():
    assert afisare_lista_fara_el_prime([8, 19, 17, 25]) == [8, 25]


def medie_aritmetica_numere(lst,n):

    suma= sum(lst)
    if int(suma/len(lst)) > int(n):
        return True
    else:
        return False

def test_medie_aritmetica_numere():
    assert medie_aritmetica_numere([10, -3, 25, -1, 3, 25, 18],10) == True
    assert medie_aritmetica_numere([1, 2, 3 ,4],3) == False
    assert medie_aritmetica_numere([10, -2, -6 , 22],4) == True

def numar_div_proprii(x):

     count=0
     for i in range(2,x//2+1):
         if x%i==0:
             count=count+1
     return count

def test_numar_div_proprii():
    assert numar_div_proprii(12) == 4
    assert numar_div_proprii(15) == 2
    assert numar_div_proprii(11) == 0

def main():

    test_is_prime()
    test_afisare_lista_fara_el_prime()
    test_medie_aritmetica_numere()
    test_numar_div_proprii()
    l=[]
    printMenu()


    while True:
        optiune = input("Alegeti optiunea dorita: ")
        if optiune == "1":
            l=citire_lista()
        elif optiune == "2":
            print(afisare_lista_fara_el_prime(l))
        elif optiune == "3":
             n=input("Introduceti numarul pentru a verifica daca media aritmetica este mai  mare ca aceasta: ")
             if medie_aritmetica_numere(l,n) == True:
                 print("DA")
             else:
                 print("NU")
        elif optiune == "4":
            print("functia 3")
        elif optiune == "5":
            print("functia 4")
        elif optiune == "x":
            break
        else:
            print("Optiunea introdusa nu este una valida")



main()