#!/bin/env python

# Converts PNG into CHR image format
# https://wiki.xxiivv.com/site/chr_format.html

from PIL import Image
import sys

if len(sys.argv) < 3:
    print("USAGE: ./png2chr.py <icn|chr> <image>")
    exit(1)

typ = sys.argv[1]
if typ != "icn" and typ != "chr":
    print("ERROR: Unknown image type")
    exit(1)

path = sys.argv[2]

sys.argv[1]

img = Image.open(path)
w, h = img.size
pixels = img.load()

output = []

for row in range(h):
    for col in range(w):
        pixel = pixels[col, row]
        value = min(pixel[0], pixel[3])

        output.append(value * 3 // 255)

def a():
    bytes_list = bytearray()

    for slice_row_idx in range(h // 8):
        for slice_col_idx in range(w // 8):
            left_bytes = bytearray()
            right_bytes = bytearray()

            for row_idx in range(8):
                left = ""
                right = ""

                for col_idx in range(8):
                    idx = slice_col_idx*8 + slice_row_idx*8*w + row_idx*w + col_idx
                    if idx >= len(output):
                        return bytes_list

                    if typ == "chr":
                        if output[idx] == 0 or output[idx] == 2:
                            left += "0"
                        else:
                            left += "1"

                        if output[idx] == 0 or output[idx] == 1:
                            right += "0"
                        else:
                            right += "1"
                    elif typ == "icn":
                        if output[idx] != 0:
                            left += "1"
                        else:
                            left += "0"

                if typ == "chr":
                    assert len(left) == 8
                    assert len(right) == 8
                    left_bytes.append(int(left, base=2))
                    right_bytes.append(int(right, base=2))
                elif typ == "icn":
                    bytes_list.append(int(left, base=2))

            if typ == "chr":
                bytes_list.extend(left_bytes)
                bytes_list.extend(right_bytes)

    return bytes_list

with open(path + "." + typ, "wb") as file:
    file.write(a())

img.close()
