board = [f"{i}" for i in range(9)]
print(board)
print()

for row in [board[i*3:(i + 1)*3] for i in range(3)]:
    print(row)
print()

for row in [board[i*3:(i + 1)*3] for i in range(3)]:
    print('| ' + ' | '.join(row) + ' |')
print()

number_board = [[f"{i}" for i in range(j*3, (j + 1)*3)] for j in range(3)]
print(number_board)
for row in number_board:
    print('| ' + ' | '.join(row) + ' |')
print()

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(', '.join(thislist[2:5]))
print()

square = 4
# check row
row_index = square // 3
row = board[row_index*3:(row_index + 1)*3]
print('| ' + ' | '.join(row) + ' |')
print()
        
# check column
col_index = square % 3
col = [board[col_index + i*3] for i in range(3)]
print('| ' + ' | '.join(col) + ' |')
print()