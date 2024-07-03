def shift_rows(state):
    for i in range(1, 4):
        state[i] = state[i][i:] + state[i][:i]
    return state

def mix_columns(state):
    mix_column_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]

    result = []
    for i in range(4):
        column = [state[j][i] for j in range(4)]
        result.append([
            (0x02 * column[0]) ^ (0x03 * column[1]) ^ column[2] ^ column[3],
            column[0] ^ (0x02 * column[1]) ^ (0x03 * column[2]) ^ column[3],
            column[0] ^ column[1] ^ (0x02 * column[2]) ^ (0x03 * column[3]),
            (0x03 * column[0]) ^ column[1] ^ column[2] ^ (0x02 * column[3])
        ])

    return list(map(list, zip(*result))) 
state_matrix = [[0x32, 0x88, 0x31, 0xe0], [0x43, 0x5a, 0x31, 0x37],
                [0xf6, 0x30, 0x98, 0x07], [0xa8, 0x8d, 0xa2, 0x34]]


# ShiftRows
shifted_state = shift_rows(state_matrix)
print("ShiftRows Result:")
for row in shifted_state:
    print(row)

# MixColumns
mixed_state = mix_columns(shifted_state)
print("\nMixColumns Result:")
for row in mixed_state:
    print(row)
