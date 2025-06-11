print('Feel like weather is stopping you from having fun?')

def weather_suggestion():
    weather = input('input your current weather and we can provide something fun to do! ').strip()
    if weather.lower() == 'sunny':
        print('\nLucky! you can do plenty of activities, such as have a picnic, go to the beach,\n'\
        'visit a park or even have a barbecue with friends!\n')
    elif weather.lower() == 'stormy':
        print('\nHope you are safe! Though the weather might seem glommy,\n'\
        'its the perfect time to have some inside fun. You can build a fort, play a board game,\n'\
        'bake, do some colouring or even make your own slime.\n')
    elif weather.lower() == 'rainy':
        print('\nYou can still do tons of fun activities during the rain! If its light rain \n' \
        'you can still go indoor places like museums, shopping malls or the movie theather\n' \
        'but if the rain is too heavy and preventing you to go outside, you can have a movie marathon,\n'\
        'bake, or even play board games with family.\n')
    elif weather.lower() == 'windy':
        print('\nHold on to your hat! Windy weather can still be exciting. You can fly a kite,'\
        'watch the trees sway,\nor take dramatic photos of the sky. If it’s too gusty, stay indoors' \
        'and try crafts, or read a book.\n')
    elif weather.lower() == 'snowy':
        print('\nIt’s a winter wonderland! Snowy weather is perfect for building a snowman,\n'\
        'going sledding, or having a snowball fight. If you’re staying indoors, you can sip hot chocolate,\n'\
        'make paper snowflakes, do puzzles, or cozy up with a good book or movie.\n')
    elif weather.lower() == 'cloudy':
        print('\nEven without sunshine, cloudy days have their own calm charm.\n'\
        'You can go for a relaxing walk, visit a cozy café, or take aesthetic photos of the sky.\n'\
        'Indoors, try journaling, painting, listening to music, or reorganizing your room for a fresh vibe.\n')
    else:
        print("\nSorry! We don't have that as a weather option for now. Our options so far are: \n" \
        "Sunny, stormy, rainy, windy, snowy and cloudy.\nPlease try again!\n")
        weather_suggestion()
weather_suggestion()