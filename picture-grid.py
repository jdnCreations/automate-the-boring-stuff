grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],        
        ['O', 'O', 'O', 'O', '.', '.'],        
        ['O', 'O', 'O', 'O', 'O', '.'],        
        ['.', 'O', 'O', 'O', 'O', 'O'],        
        ['O', 'O', 'O', 'O', 'O', '.'],        
        ['O', 'O', 'O', 'O', '.', '.'],        
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range (0, 6):
    for x in range(0, 9):
        print(grid[x][i], end='')
    print()
