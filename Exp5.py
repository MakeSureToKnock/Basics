#Given 5v source, write a function to calculate both Ohm's law and power transferred by a circuit element

voltage = 5 #input('Input voltage amount: )

resistance = -1
amps = -1


while resistance != 0 or amps != 0:

    resistance = eval(input('Input resistor resistance, or 0 to end: '))
    amps = 0

    if resistance != 0:

        amps = eval(input('Input circuit current, or 0 to end: '))

    if resistance != 0 and amps != 0:

        amps = voltage/resistance
        power = amps*voltage
        voltage = amps*resistance

        print(voltage, 'volts.')
        print(amps, 'amps.')
        print(power, 'watts.')


