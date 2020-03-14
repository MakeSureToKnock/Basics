#Write a function that displays all odd numbers from 5 to 35

#To make is eaiser to read
numbers = []

for i in range(5,36):
    if i % 2 == 1:
        numbers.append(str(i))
print(' '.join(numbers))