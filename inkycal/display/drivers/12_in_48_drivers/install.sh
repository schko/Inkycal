#!/bin/bash

# Unzip C++ SPI library and driver files
echo "Unzipping files"
unzip bcm2835-1.68
unzip EPD_12in48b
rm bcm2835-1.68.zip
rm EPD_12in48b.zip

# Install C++ SPI library for Raspberry
echo "Installing C++ SPI library"
cd bcm2835-1.68
chmod +x configure
./configure
make
sudo make check
sudo make install

# Install 12.48" E-Paper drivers
echo "Installing 12.48 inch E-Paper drivers"
cd ..
cd EPD_12in48b
make clean
make

# Show image to check if it works
echo "Showing demo image"
sudo ./EPD_12in48b 0 0 pika.bmp

echo "If you see a pikachu on the E-Paper, the install"
echo "was successful. If not, please report this issue."