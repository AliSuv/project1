# # Nekonečný cyklus pro získání dat od uživatele, který skoční při správném zadaní (číslo ne text)
# while True:
#     try:
#         vstup = int(input("Zadej svůj věk:"))

#         # custom podmínka pro vyhazování chyby (věk nemůže být méně než 0)
#         if vstup < 0:
#             raise Exception("Věk nemůže být méně než 0")
#         print(vstup)
#         break
#     except:
#         print("Špatný formát")

# jmeno, vek, a kolik ma penez

vstup_jmeno = ("")
vstup_vek = 0
vstup_penize = 0
while True:
    try:
        vstup_jmeno = input("Zadej svoje jméno: ")
        if vstup_jmeno.isnumeric():
            raise Exception("Jméno nemůže být číslovka")
        vstup_vek = int(input("Zadej svůj věk: "))
        if vstup_vek < 0:
            raise Exception("Jméno nemůže být menší než číslovka")
        vstup_penize = int(input("Zadej kolik máš peněz: "))
        if vstup_penize < 0:
            raise Exception ("Jste ve dluhu")
        break
    except Exception as e:
        print(e)
if vstup_vek < 18:
    print("Jses prilis mlady.")
elif vstup_penize < 500:
    print("Mas malo penez.")
else: 
    vstup_penize -= 500
    print(vstup_vek, vstup_jmeno, vstup_penize)

