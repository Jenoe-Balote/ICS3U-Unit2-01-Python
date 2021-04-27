#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on April 2021
# This program calculates the area and perimeter of a circle
#       with a radius of 15mm

import math


def main():
    # this function calculates the area and perimeter
    print("If a circle has a radius of 15mm:")
    print("")
    print("The area is: {} mm²".format(math.pi * 15 ** 2))
    print("")
    print("The perimeter is: {} mm".format(2 * math.pi * 15))
    print("")


if __name__ == "__main__":
    main()
