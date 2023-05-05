from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsPathItem
from PyQt5.QtGui import QPen, QColor, QBrush, QPainterPath, QPainter

class DrawingTool:
    def __init__(self, scene):
        self.scene = scene
        self.last_pos = QPointF()
        self.brush_color = QColor("#000000")

        self.drawing = False
        self.path_item = None
        self.is_drawing_enabled = False

    def mousePressEvent(self, event):
        if self.is_drawing_enabled and self.scene.is_image_displayed and event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_pos = self.scene.view.mapToScene(event.pos())

            self.path_item = QGraphicsPathItem()
            pen = QPen(self.brush_color, self.calculateBrushSize(), Qt.SolidLine)
            self.path_item.setPen(pen)
            self.scene.view.scene().addItem(self.path_item)
            self.path_item.setPos(self.last_pos)

    def mouseMoveEvent(self, event):
        if self.drawing and self.scene.is_image_displayed:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if self.scene.is_image_displayed and event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            self.drawLineTo(event.pos())
            self.path_item = None

    def drawLineTo(self, end_pos):
        scene_pos = self.scene.view.mapToScene(end_pos)
        image_rect = self.scene.view.sceneRect()
        if self.path_item:
            path = self.path_item.path()
            if image_rect.contains(scene_pos):
                pen = QPen(self.brush_color, self.calculateBrushSize(), Qt.SolidLine)
                self.path_item.setPen(pen)

                brush_radius = self.calculateBrushSize() / 2
                image_rect_adjusted = image_rect.adjusted(brush_radius, brush_radius, -brush_radius, -brush_radius)

                if image_rect_adjusted.contains(scene_pos):
                    path.lineTo(scene_pos - self.path_item.pos())
                    self.path_item.setPath(path)
            else:
                self.drawing = None

    def calculateBrushSize(self):
        image_rect = self.scene.view.sceneRect()
        width_ratio = image_rect.width() / self.scene.view.width()
        height_ratio = image_rect.height() / self.scene.view.height()
        ratio = max(width_ratio, height_ratio)
        return ratio*2