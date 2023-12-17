slovnik = {
    "a": 5,
    "b": 12
}

slovnik["a"]  # získavá hodnotu podle klíče
slovnik["a"] = 0  # upraví hodnotu

x = slovnik.keys()  # získá pole všech klíčů
y = slovnik.values()  # získá pole všech hodnot
y = slovnik.items()  # získá pole všech klíčů a hodnot

for key, value in slovnik.items():
    if value == 12:
        print(key)  # získám klíč který má hodnotu 12

slovnik.update({"c": 21})  # přidávám hodnotu
print(slovnik)

# slovnik.clear() - smaže celý slovník

# slovnik.pop("b")  # maže na základě klíče

for key, value in slovnik.items():
    # maže na základě hodnoty
    if value == 12:
        slovnik.pop(key)
        break  # ukonční for loop, když jsme našli a smazali to co jsme chtěli

print(slovnik)
