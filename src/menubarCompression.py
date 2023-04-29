from PyQt5.QtWidgets import QMenu, QAction, QDialog, QMessageBox

from compresser import Compresser
from slider import Slider

from config import showAlert

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
            
        pixmap = self.scene.graphicsScene.items()[0].pixmap()
        compressor = Compresser(self.file)

        if format in ("JPG", "PNG", "WEPB"):
            title = f"Kompresuj na {format}"
            message = "Stopień kompresji"
            compress_method = {
                "JPG": compressor.JPG_compression,
                "PNG": compressor.PNG_compression,
                "WEPB": compressor.WEBP_compression
            }[format]
            
            slider = Slider(title, message, 0, 100, 50)
            result = slider.exec_()
            if result == QDialog.Accepted:
                comp_factor = int(slider.label.text())
                compress_method(pixmap, comp_factor)