#!/bin/env bash

set -e

ffmpeg -loglevel repeat+error -y \
	-i ./tmp/0000.png \
	-i ./tmp/0001.png \
	-i ./tmp/0002.png \
	-i ./tmp/0003.png \
	-i ./tmp/0004.png \
	-i ./tmp/0005.png \
	-i ./tmp/0006.png \
	-i ./tmp/0007.png \
	-i ./tmp/0008.png \
	-i ./tmp/0009.png \
	-i ./tmp/0010.png \
	-i ./tmp/0011.png \
	-filter_complex 'vstack=12' \
	./tmp/dreloc-sheet.png

rm ./tmp/00*.png
