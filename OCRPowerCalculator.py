from AbstractPowerCalculator import AbstractPowerCalculator
from SimpleCV import Image, Camera
import cv2
import subprocess


class OCRPowerCalculator(AbstractPowerCalculator):
    def __init__(self):
        super(OCRPowerCalculator, self).__init__()
        self.wheel_circumference = 2.122  # default value - can be overridden in config.py
	# configure the USB camera...
	self.cam = Camera(prop_set={'width':1280, 'height':720})

    def power_from_speed(self, revs_per_sec):
        if self._DEBUG: print "power_from_speed"
        img = cam.getImage()
        img = img.scale(640,360)
        img.save("power.jpg")
	power = subprocess.check_output(['ssocr', '-d-1', 'power.jpg', '-fwhite', '-bblack', '-t70'])
	power = power.strip('\n')
        return int(power)

    def set_wheel_circumference(self, circumference):
        self.wheel_circumference = circumference
