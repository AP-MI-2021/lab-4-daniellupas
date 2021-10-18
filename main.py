def printMenu():
    print("1.Citire lista")
    print("2.Afișarea listei după eliminarea numerelor prime din listă")
    print("3.Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
    print("4.Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
    print("5.Afisarea listei in care fiecare element e inlocuit cu un tuplu cu propietatea data")
    print("x.Iesi din program")


def citire_lista():
    '''
    Folosind aceasta functie citim o lista
    :return: lista citita
    '''

    lst = []
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
    '''
    afisam lista din care se elimina elementele care sunt prime
    :param lst: lista initiala
    :return: o noua lista cu propietatea data
    '''

    rezultat = []
    for i in lst:
        if is_prime(int(i)) == False:
            rezultat.append(i)
    return rezultat


def test_afisare_lista_fara_el_prime():
    assert afisare_lista_fara_el_prime([8, 19, 17, 25]) == [8, 25]
    assert afisare_lista_fara_el_prime([12, 5, 7, 22]) == [12, 22]
    assert afisare_lista_fara_el_prime([121, 12, 14, 15]) == [121, 12, 14, 15]


def medie_aritmetica_numere(lst, n):
    '''
    verificam daca media aritmetica a numerelor din lista e mai mare decat un numar n dat
    :param lst: lista data
    :param n: numarul cu care comparam
    :return: valoarea de adevar (True/False)
    '''

    suma = sum(lst)
    if int(suma / len(lst)) > int(n):
        return True
    else:
        return False


def test_medie_aritmetica_numere():
    assert medie_aritmetica_numere([10, -3, 25, -1, 3, 25, 18], 10) == True
    assert medie_aritmetica_numere([1, 2, 3, 4], 3) == False
    assert medie_aritmetica_numere([10, -2, -6, 22], 4) == True


def numar_div_proprii(x):
    '''
    numaram divizorii propri a unui numar
    :param x: numarul dat
    :return: numarul de divizori propri
    '''

    count = 0
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            count = count + 1
    return count


def test_numar_div_proprii():
    assert numar_div_proprii(12) == 4
    assert numar_div_proprii(15) == 2
    assert numar_div_proprii(11) == 0


def adaugare_divizori_proprii_in_lista(lst):
    '''
    adaugam divizorii propri in lista data
    :param lst: lista initiala
    :return: o noua lista cu propietatea ceruta
    '''
    rezultat = []
    for i in lst:
        rezultat.append(i)
        rezultat.append(numar_div_proprii(i))
    return rezultat


def lista_tuplu(lst):
    '''
    creem tupl-uri care sa respecte propietatea ceruta si mai tarziu le afisam
    :param lst: lista initiala
    :return: o lista finala cu propietatea ceruta
    '''

    rezultat = []
    list_1 = []
    list_2 = []
    final = []
    for i in range(len(lst) + 1):
        list_1.append(i.__index__())
    for j in lst:
        list_2.append(lst.count(j))
    rezultat = list(zip(lst, list_1, list_2))

    return rezultat


def test_lista_tuplu():
    assert lista_tuplu([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert lista_tuplu([5, 1, 12, 2]) == [(5, 0, 1), (1, 1, 1), (12, 2, 1), (2, 3, 1)]
    assert lista_tuplu([12, 2, 3, 2]) == [(12, 0, 1), (2, 1, 2), (3, 2, 1), (2, 3, 2)]


def main():
    test_is_prime()
    test_afisare_lista_fara_el_prime()
    test_medie_aritmetica_numere()
    test_numar_div_proprii()
    test_lista_tuplu()
    l = []
    printMenu()

    while True:
        optiune = input("Alegeti optiunea dorita: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(afisare_lista_fara_el_prime(l))
        elif optiune == "3":
            n = input("Introduceti numarul pentru a verifica daca media aritmetica este mai  mare ca aceasta: ")
            if medie_aritmetica_numere(l, n) == True:
                print("DA")
            else:
                print("NU")
        elif optiune == "4":
            print(adaugare_divizori_proprii_in_lista(l))
        elif optiune == "5":
            print(lista_tuplu(l))
        elif optiune == "x":
            break
        else:
            print("Optiunea introdusa nu este una valida")


main()
