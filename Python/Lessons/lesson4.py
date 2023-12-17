# znacka = ["mercedes", "skoda", "bmw"]
# model = ["c63", "octavia", "e36"]

# vysledek = {}

# for i in znacka:
#     for j in model:
#         vysledek.update({i : j})

# print (vysledek)


# slovnik1 = {
#     "a": 2,
#     "b": 15,
#     "c": 4,
# }
# slovnik2 = {
#     "d": 7,
#     "e": 12,
#     "f": 21,
# }

# for key, value in slovnik2.items():
#     slovnik1.update({key : value}) # anebo slovnik1.update(slovnik2) bez for loopuž

# print(slovnik1)


# Vyuziti slovniku

    # uzivatel = [0, 1]
    # jmeno = ["Petr"]
    # heslo = ["gsigo575"]

    # # vnořený slovník
    # uzivatele = {
    #     "uzivatel-0": {
    #         "jmeno": "Petr",
    #         "heslo": "gspjpo654"  # šifra
    #     }
    # }

    # print(uzivatele["uzivatel-0"])


# není slovník ale set - skupina neměných hodnot, ve kterých nejsou povoleny duplikáty
        # set1 = {"apple", "nevim", True, 2}


# hodnoty skóre uživatelů
uzivatele = {
    "Petr": 500,
    "Jikra": 240,
    "Klara": 700,
    "David": 380
}

def find_max_score_user(input:dict):
    max = 0 #zacneme od minima a budeme postupne hledat maximum pomoci loopu
    for value in input.values():
        if value > max:
            max = value
    for key, value in input.items():
        if value == max:
            return {key : value}
x = find_max_score_user(uzivatele)
print(x)