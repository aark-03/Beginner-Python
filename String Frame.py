#String frame

#Creates function to calculate borders and sides of frame
def frame_string(a):
    length = len(a) + 6
    borders = '*'*length
    sides = '*  '+a+'  *'
    print(borders,sides,borders,sep='\n')

#Gets user input and passes through function
a = input('Enter string: ').strip()
frame_string(a)