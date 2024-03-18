row = 0
col = 4
if row in range(0, 3):
    print("yes")

if row in range(0, 3):
    row_index = [i for i in range(0, 3)]
elif row in range(3, 6):
    row_index = [i for i in range(3, 6)]
elif row in range(6, 9):
    row_index = [i for i in range(6, 9)]  
print(row_index)