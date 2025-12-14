#!/bin/env python

# Generates a lookup array for sine function

import math
import sys

RESOLUTION = 30
PI = 3.141592654
START = 0

no_grapth = len(sys.argv) >= 2

output = bytearray()

for i in range(RESOLUTION):
    num = 0

    if i >= START:
        a = (i - START) * (PI / (RESOLUTION - START + 2))
        s = math.sin(a)
        c = math.sin(a*4)/4
        num = math.ceil((s + c) / 1.5 * 255)

    output.append(num)

    if not no_grapth:
        maxw = 120
        width = int(num / 255 * maxw)
        for i in range(maxw):
            if i == width:
                print("#", end="")
            elif i < width:
                print("-", end="")
            else:
                print(" ", end="")

        print("")

with open("assets/sine.bin", "wb") as f:
    f.write(output)
