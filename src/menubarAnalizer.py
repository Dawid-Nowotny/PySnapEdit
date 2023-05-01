from PyQt5.QtWidgets import QMenu, QAction

from imageUtils import ImageUtils
from textRecognizer import TextRecognizer

class MenubarAnalize(QMenu):
    def __init__(self, parent, scene):
        super().__init__("Analiza obrazu", parent)
        self.scene = scene

        recognize_test = QAction("Rozpoznaj tekst na obrazie", self)
        recognize_test.triggered.connect(self.callRecognizer)

        self.addAction(recognize_test)
    
    def callRecognizer(self):
        if self.scene.checkEmpty():
            return
        
        pixmap = ImageUtils.sceneToPixmap(self.scene)
        TextRecognizer().recognize(pixmap)