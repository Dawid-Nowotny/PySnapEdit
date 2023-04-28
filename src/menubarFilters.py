from PyQt5.QtWidgets import QMenu, QAction, QMessageBox, QDialog, QGraphicsPixmapItem

from imageFilters import ImageFilters

from oddDoubleSlider import OddDoubleSlider
from doubleSlider import DoubleSlider

from config import showAlert

class MenubarFilters(QMenu):
    def __init__(self, parent, scene):
        super().__init__("Filtry", parent)

        binary_adapt_filter = QAction("Adaptacyjne progowanie", self)
        binary_adapt_filter.triggered.connect(lambda: self.updateFilter("Adapt", scene))

        self.addAction(binary_adapt_filter)

    def updateFilter(self, fil_type, scene):
        if len(scene.graphicsScene.items()) == 0:   
            showAlert("Błąd!", "Brak zdjęcia do nałożenia filtra.", QMessageBox.Warning)
            print("Brak zdjęcia do nałożenia filtra")
            return
        
        pixmap = scene.graphicsScene.items()[0].pixmap()
        filterApplicator = ImageFilters()

        match fil_type:
            case "Adapt":
                oddDS = OddDoubleSlider("Adaptacyjne progowanie", "Rozmiar bloku", 3, 33, 5, "Stała C", -95, -5, -10)
                result = oddDS.exec_()
                if result == QDialog.Accepted:
                    pixmap = filterApplicator.applyAdapt(pixmap, int(oddDS.label1.text()), int(oddDS.label2.text()))

        scene.applyFilter(pixmap)