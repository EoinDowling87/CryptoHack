state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(state, round_key):
    arr = []

    if len(state) != len(round_key):
        raise Exception("Not the same length")
 
    size = len(state)

    for i in range(size):
        row = []
        for j in range(size):
            row.append(state[i][j] ^ round_key[i][j])
        arr.append(row)
    return arr

def pro_matrix2bytes(matrix):
    
    return bytes(sum(matrix, []))

matrix = add_round_key(state, round_key)
print(matrix)

flag = pro_matrix2bytes(matrix)
print(flag.decode("utf-8"))