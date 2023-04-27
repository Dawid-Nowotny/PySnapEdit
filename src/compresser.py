from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
import numpy as np
import cv2

from config import showAlert

class Compresser():
    def __init__(self, file):
        self.file = file

    def decode_pixmap(self, pixmap, format):
        image = pixmap.toImage()
        buffer = QByteArray()
        qbuffer = QBuffer(buffer)
        qbuffer.open(QIODevice.WriteOnly)
        image.save(qbuffer, format)
        data = np.frombuffer(buffer, dtype=np.uint8)
        img = cv2.imdecode(data, cv2.IMREAD_COLOR)
        return img
    
    def JPG_compression(self, pixmap, comp_factor):
        try:
            img = self.decode_pixmap(pixmap, "JPEG")
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), comp_factor]
            result, encimg = cv2.imencode(".jpg", img, encode_param)

            self.file.saveCompressed(encimg, "JPEG Files (*.jpg)")
            
        except Exception as e:
            showAlert("Błąd!", f"{e}.", QMessageBox.Warning)
            print(f"{e}")
            return

    def PNG_compression(self, pixmap, comp_factor):
        try:
            img = self.decode_pixmap(pixmap, "PNG")
            encode_param = [int(cv2.IMWRITE_PNG_COMPRESSION), comp_factor]
            result, encimg = cv2.imencode(".png", img, encode_param)

            self.file.saveCompressed(encimg, "PNG Files (*.png)")

        except Exception as e:
            showAlert("Błąd!", f"{e}.", QMessageBox.Warning)
            print(f"{e}")
            return

    def WEBP_compression(self, pixmap, comp_factor):
        try:
            img = self.decode_pixmap(pixmap, "WEBP")
            encode_param = [int(cv2.IMWRITE_WEBP_QUALITY), comp_factor]
            result, encimg = cv2.imencode(".webp", img, encode_param)

            self.file.saveCompressed(encimg, "WEBP Files (*.webp)")

        except Exception as e:
            showAlert("Błąd!", f"{e}.", QMessageBox.Warning)
            print(f"{e}")
            return