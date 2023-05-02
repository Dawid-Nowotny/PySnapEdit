from PyQt5.QtWidgets import QMessageBox
import pytesseract
import numpy as np

from imageUtils import ImageUtils

class TextRecognizer(ImageUtils):
    def recognize(self, pixmap):
        img = self.pixmapToImage(pixmap)
        text = pytesseract.image_to_string(img, lang='eng')

        return text