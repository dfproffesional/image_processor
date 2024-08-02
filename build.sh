#!/bin/bash

VERSION=1.0

# Build binary file
pyinstaller --onefile main.py

# Build .deb file
fpm -s dir -t deb -n main -v $VERSION -C dist main=/usr/bin/imagecv2-processor

# Move file
mv main*.deb dist/ 
