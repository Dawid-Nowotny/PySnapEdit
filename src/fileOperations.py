from os import path

from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QMessageBox
from PyQt5.QtGui import QPixmap

from config import showAlert

FILE_EX = "Image Files (*.png *.jpg *.webp)"

class File:
    def __init__(self):
        self.image_path = None

    def openFile(self):
        file_name, _ = QFileDialog.getOpenFileName(None, "Otwórz plik", "", FILE_EX)

        try:
            if file_name:
                self.image_path = file_name
                pixmap = QPixmap(file_name)
                height = pixmap.height()
                width = pixmap.width()

                item = QGraphicsPixmapItem(pixmap)
                return item, height, width, file_name
        except: return None, None, None, None

    def saveToOriginal(self, scene):
        if not self.image_path:
            showAlert("Błąd!", "Nie wczytano jeszcze żadnego pliku.", QMessageBox.Warning)
            print("Nie wczytano jeszcze żadnego pliku")
            return
        
        if not path.exists(self.image_path):
            showAlert("Błąd!", "Podana ścieżka do pliku nie istnieje.", QMessageBox.Critical)
            print("Podana ścieżka do pliku nie istnieje")
            return

        pixmap = scene.items()[0].pixmap()
        pixmap.save(self.image_path)
        print("Zapisano")

    def saveFileAs(self, parent, scene):
        if not self.image_path:
            showAlert("Brak zdjęcia!", "Nie ma zdjęcia do zapisania", QMessageBox.Warning)
            print("Nie ma zdjęcia do zapisania")
            return

        try:
            file_name, _ = QFileDialog.getSaveFileName(parent, "Zapisz plik", "", FILE_EX)

            if file_name:
                item = scene.items()[0]
                pixmap = item.pixmap()
                pixmap.save(file_name)
        except: pass
    
    def saveCompressed(self, encimg, format_filter):
        try:
            file_name, _ = QFileDialog.getSaveFileName(None, "Zapisz plik", "", format_filter)

            if file_name:
                with open(file_name, "wb") as f:
                    f.write(encimg)
        except: return

    def restartImage(self):
        if not self.image_path:
            showAlert("Brak zdjęcia!", "Nie można wyczyścić pustego płótna", QMessageBox.Information)
            print("Nie można wyczyścić pustego płótna")

        self.image_path = None