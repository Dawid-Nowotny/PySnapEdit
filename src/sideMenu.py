from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QSpacerItem
from PyQt5.QtWidgets import QColorDialog, QFrame
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDesktopWidget, QDialog
from PyQt5.QtGui import QPen, QColor, QBrush, QPainterPath, QIntValidator, QIcon, QPixmap
from PyQt5.QtWidgets import QColorDialog, QSizePolicy
from PyQt5 import QtWidgets, QtCore

from config import GREEN_BUTTON, RED_BUTTON

class SideMenu(QObject):
    def __init__(self, parent, scene):
        super().__init__(parent)
        self.scene = scene
        self.dock = QDockWidget("Opcje narzędzi", parent)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        parent.addDockWidget(Qt.LeftDockWidgetArea, self.dock)
        self.color1 = "#000000"
        self.color2 = "#ffffff"

        self.initUI()

    def initUI(self):
        dockWidgetContents = QWidget()
        dockWidgetContents.setMaximumWidth(125)
        self.dock.setWidget(dockWidgetContents)
        dockLayout = QVBoxLayout(dockWidgetContents)
        
        self.draw_button = QPushButton()
        self.draw_button.setIcon(QIcon(QPixmap("files\\pen.png")))
        self.draw_button.setCheckable(True)
        self.draw_button.clicked.connect(self.handleDrawButton)
        self.draw_button.setStyleSheet(RED_BUTTON)

        self.eraser_button = QPushButton()
        self.eraser_button.setIcon(QIcon(QPixmap("files\\eraser.png")))
        self.eraser_button.setCheckable(True)
        self.eraser_button.clicked.connect(self.handleEraserButton)
        self.eraser_button.setStyleSheet(RED_BUTTON)

        self.color_frame = QFrame()
        self.color_frame.setFrameShape(QFrame.NoFrame)
        self.color_frame.setFixedSize(50, 30)
        self.color_frame.setStyleSheet("background-color: black;")
        self.color_frame.mousePressEvent = self.showColorDialog

        self.color_frame_eraser = QFrame()
        self.color_frame_eraser.setFrameShape(QFrame.NoFrame)
        self.color_frame_eraser.setFixedSize(50, 30)
        self.color_frame_eraser.setStyleSheet("background-color: white;")
        self.color_frame_eraser.mousePressEvent = self.showColorDialogEraser

        hbox = QHBoxLayout()
        hbox.addWidget(self.draw_button)
        hbox.addWidget(self.eraser_button)

        dockLayout.addLayout(hbox)
        dockLayout.addWidget(QLabel("Kolor 1:",), alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(self.color_frame, alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(QLabel("Kolor 2:",), alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(self.color_frame_eraser, alignment=QtCore.Qt.AlignCenter)

        spacer_item = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        dockLayout.addItem(spacer_item)

    def showColorDialog(self, event):
        if event.button() == Qt.LeftButton:
            color_dialog = QColorDialog.getColor()
            if color_dialog.isValid():
                self.color1 = color_dialog.name()
                self.scene.drawing_view.brush_color = QColor(self.color1)
                self.color_frame.setStyleSheet("background-color: " + self.color1 + ";")
    
    def showColorDialogEraser(self, event):
        if event.button() == Qt.LeftButton:
            color_dialog = QColorDialog.getColor()
            if color_dialog.isValid():
                self.color2 = color_dialog.name()
                self.scene.drawing_view.brush_color = QColor(self.color2)
                self.color_frame_eraser.setStyleSheet("background-color: " + self.color2 + ";")

    def handleDrawButton(self):
        if self.draw_button.isChecked():
            self.draw_button.setStyleSheet(GREEN_BUTTON)
            self.eraser_button.setStyleSheet(RED_BUTTON)
            self.scene.drawing_view.brush_color = QColor(self.color1)

            self.scene.drawing_view.is_drawing_enabled = True
            self.eraser_button.setChecked(False)
        else:
            self.draw_button.setStyleSheet(RED_BUTTON)
            self.scene.drawing_view.is_drawing_enabled = False

    def handleEraserButton(self):
        if self.eraser_button.isChecked():
            self.eraser_button.setStyleSheet(GREEN_BUTTON)
            self.draw_button.setStyleSheet(RED_BUTTON)
            self.scene.drawing_view.brush_color = QColor(self.color2)

            self.scene.drawing_view.is_drawing_enabled = True
            self.draw_button.setChecked(False)
        else:
            self.eraser_button.setStyleSheet(RED_BUTTON)
            self.scene.drawing_view.is_drawing_enabled = True
    
    def restartSideMenu(self):
        self.draw_button.setStyleSheet(RED_BUTTON)
        self.draw_button.setChecked(False)

        self.eraser_button.setStyleSheet(RED_BUTTON)
        self.draw_button.setChecked(False)

        self.scene.drawing_view.is_drawing_enabled = False
        
        self.color_frame.setStyleSheet("background-color: " + self.color1 + ";")
        self.color_frame_eraser.setStyleSheet("background-color: " + self.color2 + ";")