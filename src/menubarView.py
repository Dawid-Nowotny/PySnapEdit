from PyQt5.QtWidgets import QMenu, QAction, QGraphicsView, QApplication
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class MenubarView(QMenu):
    def __init__(self, parent, zoom):
        super().__init__("Widok", parent)

        zoom_in = QAction("Przybliż", self)
        zoom_in.triggered.connect(zoom.zoomIn)
        zoom_in.setShortcut(QKeySequence("+"))

        zoom_out = QAction("Oddal ", self)
        zoom_out.triggered.connect(zoom.zoomOut)
        zoom_out.setShortcut(QKeySequence("-"))

        zoom_restart = QAction("Ponów powiększenie (100%)", self)
        zoom_restart.triggered.connect(zoom.zoomRestart)
        zoom_restart.setShortcut(QKeySequence("`"))

        self.addAction(zoom_in)
        self.addAction(zoom_out)
        self.addAction(zoom_restart)