from PyQt5.QtWidgets import QMenu, QAction, QGraphicsView, QApplication
from PyQt5.QtGui import QKeySequence, QWheelEvent
from PyQt5.QtCore import Qt

class Zoom:
    def __init__(self, scene):
        self.scene = scene
        self.scene.view.wheelEvent = self.wheelEvent

    def zoomIn(self):
        current_scale = self.scene.view.transform().m11()
        if current_scale >= 10:
            return
        self.scene.view.scale(1.2, 1.2)

    def zoomOut(self):
        current_scale = self.scene.view.transform().m11()
        if current_scale <= 0.1:
            return
        self.scene.view.scale(1/1.2, 1/1.2)

    def zoomRestart(self):
        self.scene.view.resetTransform()

    def wheelEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self.zoomIn()
            else:
                self.zoomOut()
        else:
            QGraphicsView.wheelEvent(self.scene.view, event)