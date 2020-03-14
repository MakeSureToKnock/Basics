#Write 2 conversio programs using the while and for loop with the range statment for converting fahrenheit to celsius

#To make is eaiser to read
celsius = []
celsius1 = []

for i in range(6):
    convert = ((9/5)*i) + 32
    celsius.append(str(convert))
print(celsius)

count = 0
while count < 6:
    convert = ((9/5)*count) + 32
    celsius1.append(str(convert))
    count += 1
print(celsius1)