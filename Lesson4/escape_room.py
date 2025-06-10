name = input("What is your name? ")

print(f'Welcome to our escape room, {name}!')
Door_choice = input('Before you stand three doors: Door 1, Door 2,' \
'and Door 3. Which one will you choose? ')

if Door_choice == 'Door 1':
    print("Congrats! you escaped")

if Door_choice == 'Door 2':
    print('There was nothing behind the door, you lost' )

if Door_choice == 'Door 3':
    print('There was nothing behind the door, you lost' )

else:
    print('Please only type: Door 1, Door 2 or Door 3')