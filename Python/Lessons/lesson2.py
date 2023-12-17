# array = [0, 5, 2, 6]
# tuple = (2, 5, 1)
# dictionary = {
#     "pes": 1,
#     "kocka": 5

# array[1]
# array.append(2)  # přidá prvek nakonec
# array.pop(1)  # smaže item na indexu (defaultně poslední předmět)
# array.remove(6)  # smaže prnví výskyt hodnoty
# array.insert(2, 7)  # vloží hodnotu na daný index
# array.sort()  # seřadí pole
# array.reverse()  # převratí

# pocetDvojek = array.count(2)
# print(pocetDvojek)
# # tuple[1] = 6

# print(array)

# dictionary = {
#     "pes": 1,
#     "kocka": 5
# }
# # for(int i = 1; i <= 10; i++)
# for i in range(1, 10):  # cyklus od 1 do 9
#     print(i)

# for key, value in dictionary.items():
#     print(key, value)

# x = 0
# while x < 10:
#     print(x)
#     x += 1


# array = [0, 5, 7, 13]
# # implentace .append()

# def Append(arr, value):
#     # len(array) -> 4; poslední index -> 3
#     delkaPole = len(arr)
#     vystup = [0] * (delkaPole + 1)  # -> [0, 0, 0, 0, 0]
#     for i in range(delkaPole + 1):
#         if i < delkaPole:
#             vystup[i] = arr[i]
#         else:  # else musí být aby jsme si nepřapsali to co jsme tam zrovna dali
#             vystup[i] = value

#     return vystup

# array = Append(array, 2)
# print(array)


# Je písmeno v zadání ?, bonus: kde ?
zadani = "needle"
pismeno = "e"

def find_e(pismeno, needle):
    pocitadlo = 1
    for i in needle:
        if i == pismeno:
            return pocitadlo
        pocitadlo += 1
    return False

x=find_e(pismeno, zadani)
print(x)
