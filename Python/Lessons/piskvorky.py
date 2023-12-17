# pole 3x3 _ znaků X a O 

from colorama import Fore
def generate_array():
    result = []

    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append("_")
        result.append(row)
    return result

def print_array(array: list[list]): #parametr array je 2d pole
    result = ""
    for row in array:
        for col in row:
            result += col + " "
        result += "\n"

    print(result)

def check_if_can_draw(array:list[list], row: int, col: int):
    if row > 2 or col > 2:
        raise Exception(
            "Špatné hodnoty (hodnoty musí být 0, 1 nebo 2).")
    if array[row][col] != "_": 
        raise Exception("Toto pole je zaplněné")

# 0 - no winner, 1 - draw, 2 - winner
def check_winner(array: list[list], turn_character: str):

    # Výhry

    # řádky
    if array[0][0] == turn_character and array[0][1] == turn_character and array[0][2] == turn_character:
        return 2
    if array[1][0] == turn_character and array[1][1] == turn_character and array[1][2] == turn_character:
        return 2
    if array[2][0] == turn_character and array[2][1] == turn_character and array[2][2] == turn_character:
        return 2
    
    # Sloupce
    if array[0][0] == turn_character and array[1][0] == turn_character and array[2][0] == turn_character:
        return 2
    elif array[0][1] == turn_character and array[1][1] == turn_character and array[2][1] == turn_character:
        return 2
    elif array[0][2] == turn_character and array[1][2] == turn_character and array[2][2] == turn_character:
        return 2
    
    # diagonály
    if array[0][0] == turn_character and array[1][1] == turn_character and array[2][2] == turn_character:
        return 2
    if array[0][2] == turn_character and array[1][1] == turn_character and array[2][0] == turn_character:
        return 2
    
    # Remíza
    for i in range(0,3):
        for j in range(0,3):
            if array[i][j] == "_":
                return 1
    return 0

def game_over(winner_x, winner_o):
    if (winner_x == 2):
        print(Fore.GREEN + "Vyhrál X")
    elif (winner_o == 0):
        print(Fore.GREEN + "Vyhrál O")
    else:
        print("Remíza")

# Initialize starting array 
array = generate_array()

# main game loop
turn = 0
turn_character = ""
while True:
    print("Stav hry: ")
    print_array(array)
    turn_character = ""
    if turn % 2 == 0:
        turn_character = "X"
        print("Nyní je řada na X")
    else:
        turn_character = "O"
        print("Nyní je řada na O")

    while True:
        try:
            row = int(input("Napiš řádek kam chceš hrát: "))
            col = int(input("Napiš sloupec kam chceš hrát: "))
            check_if_can_draw(array, row, col)
            array[row][col] = turn_character
            break
        except Exception as e:
            print(e)

    winner_x = check_winner(array, "X")
    winner_o = check_winner(array, "O")

    if(winner_o != 1 or winner_x != 1):
        print_array(array)
        game_over(winner_x, winner_o)
        break

    # Increment current turn
    turn += 1
    