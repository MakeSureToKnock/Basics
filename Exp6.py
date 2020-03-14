#Write an interaction function that calculatse the volume of a sphere with radius r for only vaules above 0.

import math

radius = -1

while radius != 0:

    radius = eval(input('Input a radius, or enter 0 to end: '))

    if radius != 0:
        volume = (4/3)*math.pi*radius**3
        print(round(volume, 2))