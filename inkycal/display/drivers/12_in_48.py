#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
12.48" driver class
Copyright by aceisace
"""
from inkycal.custom import images, top_level
from os.path import exists
from PIL import Image

# Display resolution
EPD_WIDTH       = 1200
EPD_HEIGHT      = 825

driver_dir = top_level+'/inkycal/display/drivers/9_in_7_drivers/'

class EPD:

  def __init__(self):
    """12.48" epaper class"""
    # Check if zipped folders are present, if yes, assume
    # drivers have not been installed yet

    if exists(f'{driver_dir}EPD_12in48b.zip'):
      print('Additional steps are required to install drivers for 12.48" E-Paper. '
            'Please run the following command in Terminal, then retry:\n'
            f'bash {driver_dir}install.sh')

  def init(self):
    pass

  def display(self, command):
    """displays an image"""
    try:
      run_command = command.split()
      run(run_command)
    except:
      print("oops, something didn't work right :/")

  def getbuffer(self, image):
    """ad-hoc"""
    image = image.rotate(90, expand=True)
    image.convert('RGB').save(images+'canvas.bmp', 'BMP')
    command = 'sudo {}EPD_12in48b/EPD_12in48b 0 0 {}'.format(driver_dir, images+'canvas.bmp')
    #print(command)
    return command

  def sleep(self):
    pass

