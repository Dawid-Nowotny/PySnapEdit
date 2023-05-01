from PyQt5.QtWidgets import QMenu, QAction, QDialog, QMessageBox

from compresser import Compresser

from dataStorage import DataStorage
from imageUtils import ImageUtils
from slider import Slider

class MenubarCompression(QMenu):
    def __init__(self, parent, scene, file):
        super().__init__("Kompresja", parent)
        self.scene = scene
        self.file = file

        compression_JPG = QAction("Kompresuj na JPG", self)
        compression_JPG.triggered.connect(lambda: self.getCompressed("JPG"))

        compression_PNG = QAction("Kompresuj na PNG", self)
        compression_PNG.triggered.connect(lambda: self.getCompressed("PNG"))

        compression_WEPB = QAction("Kompresuj na WEPB", self)
        compression_WEPB.triggered.connect(lambda: self.getCompressed("WEPB"))

        self.addAction(compression_JPG)
        self.addAction(compression_PNG)
        self.addAction(compression_WEPB)

    def getCompressed(self, format):
        if self.scene.checkEmpty():
            return
        
        pixmap = ImageUtils.sceneToPixmap(self.scene)
        data_storage = DataStorage()
        compressor = Compresser(self.file)

        if format in ("JPG", "PNG", "WEPB"):
            title = f"Kompresuj na {format}"
            message = "Stopień kompresji"
            compress_method = {
                "JPG": compressor.JPG_compression,
                "PNG": compressor.PNG_compression,
                "WEPB": compressor.WEBP_compression
            }[format]
            
            slider = Slider(title, message, 0, 100, data_storage.compression_rate)
            result = slider.exec_()
            if result == QDialog.Accepted:
                data_storage.compression_rate = int(slider.label.text())
                compress_method(pixmap, data_storage.compression_rate)