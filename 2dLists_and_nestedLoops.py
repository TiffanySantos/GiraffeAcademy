number_grid = [ #list with element which are themselves lists
    [1, 2, 3], #list elements are mini-lists, thus creating a grid. 4 rows, 3 columns
    [4, 5, 6],
    [7,8, 9],
    [0]
]

print(number_grid[0][0]) 
#prints first element, top left = 0 in this case

for row in number_grid: 
    #loop within a loop
    for col in row:
        print(col)
        