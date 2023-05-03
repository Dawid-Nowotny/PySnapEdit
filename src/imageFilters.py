from PIL import Image, ImageQt, ImageOps
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
import cv2

from imageUtils import ImageUtils

class ImageFilters(ImageUtils):
    def __init__(self, scene):
        self.scene = scene
        self.iu = ImageUtils()

    def applyAdapt(self, pixmap, block_size, constant):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)
    
    def applyCanny(self, pixmap, min_threshold, max_threshold):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        img = cv2.GaussianBlur(img, (3,3), 0)
        img = cv2.Canny(img, min_threshold, max_threshold)
        qimg = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qimg)
        self.scene.applyFilter(pixmap)

    def applyDilation(self, pixmap, kernel_size):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        img = cv2.dilate(img, kernel)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyErosion(self, pixmap, kernel_size):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        img = cv2.erode(img, kernel)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyGaussianBlur(self, pixmap, kernel_size, sigma_x):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        img = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma_x)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyLaplacian(self, pixmap, kernel_size):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        img = cv2.Laplacian(img, cv2.CV_8U, kernel_size)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyMedian(self, pixmap, kernel_size):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        img = cv2.medianBlur(img, kernel_size)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)
    
    def applyMorphOpen(self, pixmap, kernel_size):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyNegative(self, pixmap):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        img = cv2.bitwise_not(img)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)

    def applyOtsu(self, pixmap):
        img = self.iu.pixmapToImage(pixmap)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        pixmap = self.iu.imageToPixmap(img)
        self.scene.applyFilter(pixmap)