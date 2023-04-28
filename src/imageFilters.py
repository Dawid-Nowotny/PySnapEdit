from PIL import Image, ImageQt, ImageOps
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import cv2

class ImageFilters:
    def imageToPixmap(self, img):
        h, w, ch = img.shape
        bytesPerLine = ch * w
        image = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        return pixmap
    
    def pixmapToImage(self, pixmap):
        image = pixmap.toImage()
        buffer = image.bits().asstring(image.byteCount())
        img = np.frombuffer(buffer, dtype=np.uint8).reshape((image.height(), image.width(), 4))
        return img
    
    def applyAdapt(self, pixmap, block_size, constant):
        img = self.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        pixmap = self.imageToPixmap(img)
        return pixmap