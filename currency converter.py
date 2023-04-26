print('DIGITAL CURRENCY CONVERTER')
while True:
    instruction=input('''
             1. Press 1 if you can to convert from Dollar to Naira.
             2. Press 2 if you can to convert from Naira to Dollar.
             3. Press 3 if you can to convert from Euro to Naira.
             4. Press 4 if you can to convert from Naira to Euro.
             5. Press 5 if you can to convert from Pounds to Naira.
             6. Press 6 if you can to convert from Naira to Pounds.
             7. Press 7 if you can to convert from Euro to Dollar.
             8. Press 8 if you can to convert from Dollar to Euro.
             9. Press 9 if you can to convert from Pounds to Dollar.
             10. Press 10 if you can to convert from Dollar to Pounds.
             11. Press 11 if you can to convert from Euro to Pounds
             12. Press 12 if you can to convert from Pounds to Euro.
             13. Press 13 if you want to quit.
=''')
    if instruction == '1':
        a = int(input('Enter the amount of Dollar you want to convert to Naira: '))
        print('The conversion of $', a, 'is', '#', a * 441.69)
    elif instruction == '2':
        a = int(input('Enter the amount of Naira you want to convert to Dollar: '))
        print('The conversion of #', a, 'is', '$', a * 0.0023)
    elif instruction == '3':
        a = int(input('Enter the amount of Euro you want to convert to Naira: '))
        print('The conversion of ', a, 'Euro is', '#', a * 459.16)
    elif instruction == '4':
        a = int(input('Enter the amount of Naira you want to convert to Euro: '))
        print('The conversion of #', a, 'is', a * 0.0022, 'Euro')
    elif instruction == '5':
        a = int(input('Enter the amount of Pounds you want to convert to Naira: '))
        print('The conversion of ', a, 'pounds is', '#', a * 526.32)
    elif instruction == '6':
        a = int(input('Enter the amount of Naira you want to convert to Pounds: '))
        print('The conversion of #', a, 'is', a * 0.0019, 'pounds')
    elif instruction == '7':
        a = int(input('Enter the amount of Euro you want to convert to Dollar: '))
        print('The conversion of ', a, 'Euro is', '$', a * 1.04)
    elif instruction == '8':
        a = int(input('Enter the amount of Dollar you want to convert to Euro: '))
        print('The conversion of $', a, 'is', a * 0.96, 'Euro')
    elif instruction == '9':
        a = int(input('Enter the amount of Pounds you want to convert to Dollar: '))
        print('The conversion of ', a, 'pounds is', '$', a * 1.19)
    elif instruction == '10':
        a = int(input('Enter the amount of Dollar you want to convert to Pounds: '))
        print('The conversion of $', a, 'is', a * 0.84, 'pounds')
    elif instruction == '11':
        a = int(input('Enter the amount of Euro you want to convert to Pounds: '))
        print('The conversion of ', a, 'Euro is', a * 0.87, 'pounds')
    elif instruction == '12':
        a = int(input('Enter the amount of Pounds you want to convert to Euro: '))
        print('The conversion of ', a, 'pounds is', a * 1.15, 'Euro')
    elif instruction == '13':
        quit()
    else:
        print('Enter correct instruction')
