from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDesktopWidget, QDialog
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class ColorAnalysisDisplay(QWidget):
    def __init__(self, hist, image_array, parent):
        super().__init__()
        self.hist = hist
        self.image_array = image_array

        self.combieDiagrams(parent)

    def combieDiagrams(self, parent):
        self.setParent(parent)
        self.setMinimumSize(1350, 470)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint | Qt.Dialog)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint & ~Qt.WindowMaximizeButtonHint)
        
        layout = QHBoxLayout(self)
        self.setLayout(layout)
        layout.addWidget(self._plot_histogram())
        layout.addWidget(self._generate_color_palette())
        
        self.setWindowTitle("PySnapEdit - analiza kolorów")
        self.setWindowIcon(QtGui.QIcon("files\\icon.png"))

        return self
    
    def _plot_histogram(self):
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.plot(self.hist)
        ax.set_title('Histogram kolorów')
        ax.set_xlabel('Odcień')
        ax.set_ylabel('Liczba pikseli')
        ax.set_xlim([0, 180])
        return canvas

    def _generate_color_palette(self):
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        unique_colors = np.unique(self.image_array.reshape(-1, self.image_array.shape[2]), axis=0)
        palette = np.zeros((len(unique_colors), 1, 3), dtype=np.uint8)
        palette[:, 0, :] = unique_colors[:, :3]
        ax.imshow(palette, aspect='auto')
        ax.set_title('Paleta kolorów')
        ax.axis('off')
        return canvas
    
    def closeEvent(self, event):
        if self.parentWidget() is not None:
            self.parentWidget().color_result = None
        self.close()
        event.accept()