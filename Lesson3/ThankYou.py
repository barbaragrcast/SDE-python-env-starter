def thank_you(name):
    print(f'Dear {name},\nThank you so much for your gift for my ' \
    'birthday. \nIt means so much to me!\nYours Truly,\nBarbara\n')
          
def print_thank_you_card():
    family_gifts = ['Mom', 'Dad', 'Sister', 'Grandma']
    friend_gifts = ['Dennisia','Andrea','Joselyn', 'All']
    for name in family_gifts:
        thank_you(name)
    for name in friend_gifts:
        thank_you(name)

print_thank_you_card()