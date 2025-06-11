def check_number(value):
    try:
        number = float(value)
        return int(number) if number.is_integer() else number
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

a = None
while a is None:
    a = check_number(input('Please provide a number: '))

b = None
while b is None:
    b = check_number(input('Please provide a second number: '))

operation = input('\nWhich operation do you want to perform:\n'\
'Addition, subtraction, multiplication or division: ').strip().lower()

if operation == 'addition':
    print(f'Your sum is {a + b}.')

elif operation == 'subtraction':
    print(f'Your subtraction is {a - b}.')

elif operation == 'multiplication':
    print(f'Your multiplication is {a * b}.')

elif operation == 'division':
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print(f'Your division is {a / b}.')

else:
    print("Invalid operation selected.")
