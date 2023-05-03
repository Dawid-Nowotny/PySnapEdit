import cv2
import numpy as np
import matplotlib.pyplot as plt

from imageUtils import ImageUtils

class ImageColorAnalize():
    def analyzeColors(self, pixmap):
        iu = ImageUtils()
        
        image_array = iu.pixmapToImage(pixmap)
        hsv_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv_image], [0], None, [180], [0, 180])

        return hist, image_array
    
    def colorHue(self, hue_color):
        hue = hue_color * (180 / 256)
        hsv_color = np.uint8([[[hue, 255, 255]]])
        rgb_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2RGB)[0, 0]

        return rgb_color