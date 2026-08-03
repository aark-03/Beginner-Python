#Nickname Generator

print('Create your nickname!')
name = input('Enter your first name: ').strip()

nickname = name[0]+name[-1]+name[0]+name[-1]
nickname = nickname.lower().capitalize()
print('Your nickname is: {}!'.format(nickname))