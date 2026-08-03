#Nickname Generator

#Gets user input
print('Create your nickname!')
name = input('Enter your first name: ').strip()

#Creates nickname with string arrays
nickname = name[0]+name[-1]+name[0]+name[-1]
nickname = nickname.lower().capitalize()

print('Your nickname is: {}!'.format(nickname))