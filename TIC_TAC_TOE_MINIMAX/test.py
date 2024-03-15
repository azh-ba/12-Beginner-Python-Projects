board = [' ' for _ in range(9)]

my = [i for i, x in enumerate(board) if x == ' ']

yours = [board[i] for i in range(9) if board[i] == ' ']

print(my)
print()
print(yours)