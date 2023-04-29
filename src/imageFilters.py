from PIL import Image, ImageQt, ImageOps
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import cv2

class ImageFilters:
    def __init__(self, scene):
        self.scene = scene

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
        self.scene.applyFilter(pixmap)
    
    def applyDilation(self, pixmap, kernel_size):
        img = self.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        img = cv2.dilate(img, kernel)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        pixmap = self.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyErosion(self, pixmap, kernel_size):
        img = self.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        img = cv2.erode(img, kernel)
        pixmap = self.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyNegative(self, pixmap):
        img = self.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        img = cv2.bitwise_not(img)
        pixmap = self.imageToPixmap(img)
        self.scene.applyFilter(pixmap)