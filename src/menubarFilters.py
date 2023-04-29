from PyQt5.QtWidgets import QMenu, QAction, QMessageBox, QDialog, QGraphicsPixmapItem

from imageFilters import ImageFilters

from dataStorage import DataStorage

from oddSlider import OddSlider
from oddDoubleSlider import OddDoubleSlider
from doubleSlider import DoubleSlider
from limitedRangeSlider import LimitedRangeSlider

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
        data_storage = DataStorage()

        match fil_type:
            case "Adapt":
                slider = OddDoubleSlider("Adaptacyjne progowanie", "Rozmiar bloku", data_storage.LOW_KERNEL, data_storage.TOP_KERNEL, data_storage.binary_block, 
                                         "Stała C", data_storage.LOW_C, data_storage.HIGH_C, data_storage.binary_C)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.binary_block = int(slider.label1.text())
                    data_storage.binary_C = int(slider.label2.text())
                    self.filterApplicator.applyAdapt(pixmap, data_storage.binary_block, data_storage.binary_C)
            case "Canny":
                slider = LimitedRangeSlider("Detektor krawędzi Canny'ego", "Pierwszy próg", data_storage.LOW_THRESHHOLD, data_storage.HIGH_THRESHHOLD, data_storage.canny_treshhold1, 
                                            "Drugi próg", data_storage.LOW_THRESHHOLD, data_storage.HIGH_THRESHHOLD, data_storage.canny_treshhold2)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.canny_treshhold1 = int(slider.label1.text())
                    data_storage.canny_treshhold2 = int(slider.label2.text())
                    self.filterApplicator.applyCanny(pixmap, data_storage.canny_treshhold1, data_storage.canny_treshhold2)
            case "Dilate":
                slider = OddSlider("Dylatacja", "Rozmiar maski", data_storage.LOW_KERNEL, data_storage.TOP_KERNEL, data_storage.dilate_kernel)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.dilate_kernel = int(slider.label.text())
                    self.filterApplicator.applyDilation(pixmap, data_storage.dilate_kernel)
            case "Erode":
                slider = OddSlider("Erozja", "Rozmiar maski", data_storage.LOW_KERNEL, data_storage.TOP_KERNEL, data_storage.erode_kernel)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.erode_kernel = int(slider.label.text())
                    self.filterApplicator.applyErosion(pixmap, data_storage.erode_kernel)
            case "Gauss":
                slider = OddDoubleSlider("Rozmycie Gaussa", "Rozmiar maski", data_storage.LOW_KERNEL, data_storage.TOP_KERNEL, data_storage.gauss_kernel, 
                                         "sigma X", 0, 10, data_storage.gauss_sigma)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.gauss_kernel = int(slider.label1.text())
                    data_storage.gauss_sigma = int(slider.label2.text())
                    self.filterApplicator.applyGaussianBlur(pixmap, data_storage.gauss_kernel, data_storage.gauss_sigma)
            case "Laplace":
                slider = OddSlider("Filtr Laplace'a", "Rozmiar maski", data_storage.LOW_KERNEL, data_storage.TOP_KERNEL, data_storage.laplace_kernel)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.laplace_kernel = int(slider.label.text())
                    self.filterApplicator.applyLaplacian(pixmap, data_storage.laplace_kernel)
            case "Median":
                slider = OddSlider("Filtr Medianowy", "Rozmiar maski", data_storage.LOW_KERNEL, data_storage.TOP_KERNEL, data_storage.median_kernel)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.median_kernel = int(slider.label.text())
                    self.filterApplicator.applyMedian(pixmap, data_storage.median_kernel)
            case "Morph":
                slider = OddSlider("Otwarcie morfologiczne", "Rozmiar maski", data_storage.LOW_KERNEL, data_storage.TOP_KERNEL, data_storage.morph_kernel)
                result = slider.exec_()
                if result == QDialog.Accepted:
                    data_storage.morph_kernel = int(slider.label.text())
                    self.filterApplicator.applyMorphOpen(pixmap, data_storage.morph_kernel)
            case "Otsu":
                self.filterApplicator.applyOtsu(pixmap)
            case "Negative":
                self.filterApplicator.applyNegative(pixmap)