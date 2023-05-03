from PyQt5.QtWidgets import QMenu, QAction, QMessageBox

from textRecognizer import TextRecognizer
from imageColorAnalize import ImageColorAnalize
from recognizedDialog import RecognizedDialog
from colorAnalysisDisplay import ColorAnalysisDisplay
from imageUtils import ImageUtils

from config import showAlert

class MenubarAnalize(QMenu):
    def __init__(self, parent, scene):
        super().__init__("Analiza obrazu", parent)
        self.scene = scene
        self.color_result = None
        
        color_analize = QAction("Analizuj kolory", self)
        color_analize.triggered.connect(lambda: self.callColorAnalysis(parent))

        recognize_test = QAction("Rozpoznaj tekst na obrazie", self)
        recognize_test.triggered.connect(self.callRecognizer)

        self.addAction(color_analize)
        self.addAction(recognize_test)
    
    def callColorAnalysis(self, parent):
        if self.scene.checkEmpty():
            showAlert("Błąd!", "Brak zdjęcia, nie można analizować kolorów bez zdjęcia.", QMessageBox.Warning)
            print("Brak zdjęcia, nie można analizować kolorów bez zdjęcia.")
            return
        
        pixmap = ImageUtils.sceneToPixmap(self.scene)
        hist, image_array = ImageColorAnalize().analyzeColors(pixmap)
        self.color_result = ColorAnalysisDisplay(hist, image_array, parent)
        self.color_result.show()

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