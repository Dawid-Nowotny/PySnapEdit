from PyQt5.QtWidgets import QMenu, QAction, QMessageBox

from textRecognizer import TextRecognizer
from recognizedDialog import RecognizedDialog
from imageUtils import ImageUtils

from config import showAlert

class MenubarAnalize(QMenu):
    def __init__(self, parent, scene):
        super().__init__("Analiza obrazu", parent)
        self.scene = scene

        recognize_test = QAction("Rozpoznaj tekst na obrazie", self)
        recognize_test.triggered.connect(self.callRecognizer)

        self.addAction(recognize_test)
    
    def callRecognizer(self):
        if self.scene.checkEmpty():
            showAlert("Błąd!", "Brak zdjęcia, dodaj zdjęcie aby wykonać na nim operacje.", QMessageBox.Warning)
            print("Brak zdjęcia, dodaj zdjęcie aby wykonać na nim operacje.")
            return
        
        pixmap = ImageUtils.sceneToPixmap(self.scene)
        text = TextRecognizer().recognize(pixmap)

        if not text.strip():
            showAlert("Informacja", "Nie udało się rozpoznać żadnego tekstu na obrazie", QMessageBox.Information)
            print("Nie udało się rozpoznać żadnego tekstu na obrazie")
        else:
            dialog = RecognizedDialog(text)
            dialog.exec_()