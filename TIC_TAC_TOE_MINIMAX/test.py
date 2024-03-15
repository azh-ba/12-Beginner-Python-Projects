board = [' ' for _ in range(9)]

yours = [i for i, x in enumerate(board) if x == ' ']

yours2 = [' ' in board]

my = [board[i] for i in range(9) if board[i] == ' ']

print(my)
print()
print(yours)
print()
print(yours2)