from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPathItem
from PyQt5.QtGui import QPen, QColor, QBrush, QPainterPath, QPainter

class DrawingTool:
    def __init__(self, view, scene_self):
        self.view = view
        self.s = scene_self
        self.scene = view.scene()
        self.drawing = False
        self.last_pos = QPointF()
        self.path_item = None

    def mousePressEvent(self, event):
        if self.s.is_image_displayed and event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_pos = self.view.mapToScene(event.pos())

            self.path_item = QGraphicsPathItem()
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            self.path_item.setPen(pen)
            self.scene.addItem(self.path_item)
            self.path_item.setPos(self.last_pos)

    def mouseMoveEvent(self, event):
        if self.drawing and self.s.is_image_displayed:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if self.s.is_image_displayed and event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            self.drawLineTo(event.pos())
            self.path_item = None

    def drawLineTo(self, end_pos):
        scene_pos = self.view.mapToScene(end_pos)
        image_rect = self.view.sceneRect()
        if image_rect.contains(scene_pos) and self.path_item:
            path = self.path_item.path()
            path.lineTo(scene_pos - self.path_item.pos())
            self.path_item.setPath(path)