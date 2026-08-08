#Grid maker

#Takes user input for rows, columns, and symbol
rows = input('Enter number of rows: ').strip()
cols = input('Enter number of columns: ').strip()
sym = input('Enter symbol: ').strip()

rows = int(rows)
cols = int(cols)

#Computes top, bottom, and sides of grid
borders = sym*rows
sides = (sym+(' '*(rows-2))+sym+'\n')*cols

print(borders+'\n'+sides+borders)