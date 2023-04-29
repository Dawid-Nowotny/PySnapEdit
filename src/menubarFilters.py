from PyQt5.QtWidgets import QMenu, QAction, QMessageBox, QDialog, QGraphicsPixmapItem

from imageFilters import ImageFilters

from oddSlider import OddSlider
from oddDoubleSlider import OddDoubleSlider
from doubleSlider import DoubleSlider
from limitedRangeSlider import LimitedRangeSlider

TOP_KERNEL = 33
LOW_KERNEL = 3
START_KERNEL = 5

class MenubarFilters(QMenu):
    def __init__(self, parent, scene):
        super().__init__("Filtry", parent)
        self.scene = scene
        self.filterApplicator = ImageFilters(self.scene)

        binary_adapt_filter = QAction("Adaptacyjne progowanie", self)
        binary_adapt_filter.triggered.connect(lambda: self.updateFilter("Adapt"))

        canny_filter = QAction("Detektor krawędzi Canny'ego", self)
        canny_filter.triggered.connect(lambda: self.updateFilter("Canny"))

        dilate_filter = QAction("Dylatacja ", self)
        dilate_filter.triggered.connect(lambda: self.updateFilter("Dilate"))

        erode_filter = QAction("Erozja", self)
        erode_filter.triggered.connect(lambda: self.updateFilter("Erode"))

        gauss_filter = QAction("Rozmycie Gaussa", self)
        gauss_filter.triggered.connect(lambda: self.updateFilter("Gauss"))

        laplace_filter = QAction("Laplace'a", self)
        laplace_filter.triggered.connect(lambda: self.updateFilter("Laplace"))

        median_filter = QAction("Medianowy", self)
        median_filter.triggered.connect(lambda: self.updateFilter("Median"))

        morph_open_filter = QAction("Otwarcie morfologiczne", self)
        morph_open_filter.triggered.connect(lambda: self.updateFilter("Morph"))

        negative_filter = QAction("Negatyw", self)
        negative_filter.triggered.connect(lambda: self.updateFilter("Negative"))

        otsu_filter = QAction("Otsu", self)
        otsu_filter.triggered.connect(lambda: self.updateFilter("Otsu"))

        self.addAction(binary_adapt_filter)
        self.addAction(canny_filter)
        self.addAction(dilate_filter)
        self.addAction(erode_filter)
        self.addAction(gauss_filter)
        self.addAction(laplace_filter)
        self.addAction(median_filter)
        self.addAction(morph_open_filter)
        self.addAction(negative_filter)
        self.addAction(otsu_filter)

    def updateFilter(self, fil_type):
        if self.scene.checkEmpty():
            return
        
        pixmap = self.scene.graphicsScene.items()[0].pixmap()
        
        match fil_type:
            case "Adapt":
                slider = OddDoubleSlider("Adaptacyjne progowanie", "Rozmiar bloku", LOW_KERNEL, TOP_KERNEL, START_KERNEL, "Stała C", -95, -5, -10)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyAdapt(pixmap, int(slider.label1.text()), int(slider.label2.text()))
            case "Canny":
                double_slider = LimitedRangeSlider("Detektor krawędzi Canny'ego", "Pierwszy próg", 0, 255, 50, "Drugi próg", 0, 255, 150)
                result = double_slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyCanny(pixmap, int(double_slider.label1.text()), int(double_slider.label2.text()))
            case "Dilate":
                slider = OddSlider("Dylatacja", "Rozmiar maski", LOW_KERNEL, TOP_KERNEL, START_KERNEL)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyDilation(pixmap, int(slider.label.text()))
            case "Erode":
                slider = OddSlider("Erozja", "Rozmiar maski", LOW_KERNEL, TOP_KERNEL, START_KERNEL)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyErosion(pixmap, int(slider.label.text()))
            case "Median":
                slider = OddSlider("Filtr Medianowy", "Rozmiar maski", LOW_KERNEL, TOP_KERNEL, START_KERNEL)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyMedian(pixmap, int(slider.label.text()))
            case "Gauss":
                double_slider = DoubleSlider("Rozmycie Gaussa", "Rozmiar maski", LOW_KERNEL, TOP_KERNEL, START_KERNEL, "sigma X", 0, 10, 1)
                result = double_slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyGaussianBlur(pixmap, int(double_slider.label1.text()), int(double_slider.label2.text()))
            case "Laplace":
                slider = OddSlider("Filtr Laplace'a", "Rozmiar maski", LOW_KERNEL, TOP_KERNEL, START_KERNEL)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyLaplacian(pixmap, int(slider.label.text()))
            case "Morph":
                slider = OddSlider("Otwarcie morfologiczne", "Rozmiar maski", LOW_KERNEL, TOP_KERNEL, START_KERNEL)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    self.filterApplicator.applyMorphOpen(pixmap, int(slider.label.text()))
            case "Otsu":
                self.filterApplicator.applyOtsu(pixmap)
            case "Negative":
                self.filterApplicator.applyNegative(pixmap)