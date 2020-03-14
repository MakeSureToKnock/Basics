#Find you weight in stones?????????????????????????


def stones(weight):
    
    stoneWeight = (weight*2.2)/14

    return stoneWeight

try:
    yourWeight = eval(input('Enter your weight: '))

except:
    print('Please enter a weight.')

else:
    print(stones(yourWeight))