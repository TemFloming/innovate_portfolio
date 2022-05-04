
# ----------
# Acivity 1
# ----------

# greeting = "Welcome to Code Nation."

# print(len(greeting))

# greeting_len = (len(greeting))

# if greeting_len/2:
#     print("Welcome to Code Nationon.")
#     print:greeting_len
# else:
#     print("No Code Nation for you!")

# -----------
# Activity 2
# -----------

# alphabet=[
#     "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
# ]

# for (i) in alphabet: 
#     print(i)

# in_num = input("Select a number from 1 to 26. ")
# in_num = int(in_num)
# in_num -=1

# print("The corresponding character is...")
# print(alphabet[in_num])

# -----------
# Activity 3
# -----------

# print("   |   |   ")
# print("   |   |   ")
# print("   |   |   ")
# print("-----------")
# print("   |   |   ")
# print("   |   |   ")
# print("   |   |   ")
# print("-----------")
# print("   |   |   ")
# print("   |   |   ")
# print("   |   |   ")

# space1 = "x"
# space2 = "x"
# space3 = "o"
# space4 = "x"
# space5 = "o"
# space6 = "o"
# space7 = "x"
# space8 = "x"
# space9 = "o"

# print("-------------")
# print("   |    |    ")
# print("{}  | {}  | {} ".format(space1, space2, space3))
# print("   |    |    ")
# print("-------------")
# print("   |    |    ")
# print("{}  | {}  | {} ".format(space4, space5, space6))
# print("   |    |    ")
# print("-------------")
# print("   |    |    ")
# print("{}  | {}  | {} ".format(space7, space8, space9))
# print("   |    |    ")
# print("-------------")

# GLOBAL VARIABLES
M = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

S = True
C = 0



# FUNCTIONS
def board_show():
    print()
    for y in range(3):
        print(" ", end="")
        for x in range(3):
            print(M[y][x], end=" ")
        print()
    print()

def check_hr(y):
    return M[y][0] == M[y][1] == M[y][2] != '_'

def check_vr(x):
    return M[0][x] == M[1][x] == M[2][x] != '_'

def check_dig():
    return M[0][0] == M[1][1] == M[2][2] != '_' or \
           M[0][2] == M[1][1] == M[2][0] != '_'

def big_check():
    win = False
    for i in range(3):
        if check_hr(i) or check_vr(i):
            win = True
    if check_dig():
        win = True
    return win

def turn():
    global S, C
    pos = [ ( int(i) - 1 ) for i in input("Your move: ").split() ]
    x, y = pos[0], pos[1]
    if M[y][x] == '_':
        M[y][x] = 'X' if S else 'O'
        S = not S
        C += 1
        board_show()
    else:
        print("Invalid move!")



# MAIN
def xo():
    board_show()
    while C < 9:
        turn()
        if big_check():
            print(f"{'X' if not S else 'O'} wins!", end="\n\n")
            break
    else:
        print("It's a tie!", end="\n\n")



xo()