vstup = [1, 2, 5, 7, 1, 2, 6]
# list(dict.fromkeys(vstup)) - řešení od pythonu


def RemoveDuplicates(vstup: list):
    # indexy pro kontrolu že duplikát je na jiném místě než zkoumané číslo
    controlledIndex = 0  # index zkoumaného čísla
    index = 0  # index jiného čísla
    toDolete = []  # pro ukládání nalezených duplikátů

    for i in vstup:
        # i = 1, j = 1, controlledIndex = 0, index = 0; -> neprojde protože indexy se shodují
        # i = 1, j = 2, controlledIndex = 0, index = 1; -> neprojde protože čísla se shodují
        # ...
        # i = 1, j = 1, controlledIndex = 0, index = 4; -> projde a 1 se zapíše do pole nalezených duplikátů
        for j in vstup:
            if i == j and controlledIndex != index and j not in toDolete:
                toDolete.append(j)
            index += 1  # zvedneme vnitřní index -> jdeme hledat další číslo jestli není duplikát
        controlledIndex += 1  # zvedneme vnější index -> jdeme kontrolovat jiné číslo pro duplicitu
        index = 0  # musíme nulovat protože při každém průchodu kontrolovaného čísla tato smyčka proleze celé pole

    # z pole smažeme věci které jsme našli jako duplicitní
    for x in toDolete:
        vstup.remove(x)
    return vstup


vstup = RemoveDuplicates(vstup)
print(vstup)
