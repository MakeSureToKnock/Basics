#Display the change for a dollar

# dollar = str(float(round(eval(input('Enter money: ')), 2))).split('.')

# if dollar[1] == '0':
#     dollar[1] = '0'
# elif len(dollar[1]) < 2:
#     dollar[1] += '0'

# dollar = int(dollar[0] + dollar[1])

dollar = float(round(eval(input('Enter money: ')), 2))*100

quarter = 0
dime = 0
nickel = 0
penny = 0

while dollar > 0:
    if dollar >= 25:
        dollar -= 25
        quarter += 1
    elif dollar >= 10:
        dollar -= 10
        dime += 1
    elif dollar >= 5:
        dollar -= 5
        nickel += 1
    elif dollar >= 1:
        dollar -= 1
        penny += 1

print(str(quarter) + ' quarters,', str(dime) + ' dimes,', str(nickel) + ' nickels,', str(penny) + ' pennies.')



