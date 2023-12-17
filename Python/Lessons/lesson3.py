vstup = [4, 6, 5, 7, 9, 0, 5, 6]

def is_in_array(array:list, value): # :list řekne array že se má brát jako list
    index=0
    pole = []
    for i in array:
        if value == i:
            pole.append(index)
        index += 1
    if len(pole) == 0:
        return -1
    return pole
    
final = is_in_array(vstup, 5)
print(final)