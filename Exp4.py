#Create an interactive function given x using the pseduo code below

number = -1

while number != 0:

    number = eval(input('Input a number, or enter 0 to end: '))

    if number != 0:
        if number % 2 == 0:
            print('ON')
        else:
            print('OFF')

