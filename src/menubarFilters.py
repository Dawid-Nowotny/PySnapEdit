from PyQt5.QtWidgets import QMenu, QAction, QMessageBox, QDialog, QGraphicsPixmapItem

from imageFilters import ImageFilters

from oddSlider import OddSlider

from oddDoubleSlider import OddDoubleSlider
from doubleSlider import DoubleSlider

class MenubarFilters(QMenu):
    def __init__(self, parent, scene):
        super().__init__("Filtry", parent)
        self.scene = scene
        self.filterApplicator = ImageFilters(self.scene)

        binary_adapt_filter = QAction("Adaptacyjne progowanie", self)
        binary_adapt_filter.triggered.connect(lambda: self.updateFilter("Adapt"))

        dilate_filter = QAction("Dylatacja ", self)
        dilate_filter.triggered.connect(lambda: self.updateFilter("Dilate"))

        erode_filter = QAction("Erozja", self)
        erode_filter.triggered.connect(lambda: self.updateFilter("Erode"))

        negative_filter = QAction("Negatyw", self)
        negative_filter.triggered.connect(lambda: self.updateFilter("Negative"))

        self.addAction(binary_adapt_filter)
        self.addAction(dilate_filter)
        self.addAction(erode_filter)
        self.addAction(negative_filter)

    def updateFilter(self, fil_type):
        if self.scene.checkEmpty():
            return
        
        pixmap = self.scene.graphicsScene.items()[0].pixmap()
        
        match fil_type:
            case "Adapt":
                oddDS = OddDoubleSlider("Adaptacyjne progowanie", "Rozmiar bloku", 3, 33, 5, "Stała C", -95, -5, -10)
                result = oddDS.exec_()
                if result == QDialog.Accepted:
                    pixmap = self.filterApplicator.applyAdapt(pixmap, int(oddDS.label1.text()), int(oddDS.label2.text()))
            case "Dilate":
                slider = OddSlider("Dylatacja", "Rozmiar maski", 3, 33, 5)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    pixmap = self.filterApplicator.applyDilation(pixmap, int(slider.label.text()))
            case "Erode":
                slider = OddSlider("Erozja", "Rozmiar maski", 3, 33, 5)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    pixmap = self.filterApplicator.applyErosion(pixmap, int(slider.label.text()))
            case "Negative":
                pixmap = self.filterApplicator.applyNegative(pixmap)