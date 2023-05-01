from PyQt5.QtWidgets import QMessageBox
import pytesseract
import numpy as np

from recognizedDialog import RecognizedDialog
from imageUtils import ImageUtils

from config import showAlert

class TextRecognizer(ImageUtils):
    def recognize(self, pixmap):
        img = self.pixmapToImage(pixmap)
        text = pytesseract.image_to_string(img, lang='eng')

        if not text.strip():
            showAlert("Informacja", "Nie udało się rozpoznać żadnego tekstu na obrazie", QMessageBox.Information)
            print("Nie udało się rozpoznać żadnego tekstu na obrazie")
        else:
            dialog = RecognizedDialog(text)
            dialog.exec_()