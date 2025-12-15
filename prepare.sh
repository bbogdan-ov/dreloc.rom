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
	-i ./tmp/0012.png \
	-i ./tmp/0013.png \
	-i ./tmp/0014.png \
	-i ./tmp/0015.png \
	-i ./tmp/0016.png \
	-i ./tmp/0017.png \
	-i ./tmp/0018.png \
	-i ./tmp/0019.png \
	-i ./tmp/0020.png \
	-i ./tmp/0021.png \
	-i ./tmp/0022.png \
	-i ./tmp/0023.png \
	-filter_complex 'vstack=24' \
	./tmp/dreloc.png
