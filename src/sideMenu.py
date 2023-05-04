from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox, QSpacerItem
from PyQt5.QtWidgets import QColorDialog, QFrame
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDesktopWidget, QDialog
from PyQt5.QtGui import QPen, QColor, QBrush, QPainterPath, QIntValidator
from PyQt5.QtWidgets import QColorDialog, QSizePolicy
from PyQt5 import QtWidgets, QtCore

from config import showAlert, GREEN_BUTTON, RED_BUTTON

class SideMenu(QObject):
    def __init__(self, parent, scene):
        super().__init__(parent)
        self.scene = scene
        self.dock = QDockWidget("Opcje narzędzi", parent)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        parent.addDockWidget(Qt.LeftDockWidgetArea, self.dock)

        self.previous_color = "#000000"

        self.initUI()

    def initUI(self):
        dockWidgetContents = QWidget()
        dockWidgetContents.setMaximumWidth(200)
        self.dock.setWidget(dockWidgetContents)
        dockLayout = QVBoxLayout(dockWidgetContents)
        
        self.draw_button = QPushButton("Rysuj")
        self.draw_button.setCheckable(True)
        self.draw_button.clicked.connect(self.handleDrawButton)
        self.draw_button.setStyleSheet(RED_BUTTON)

        self.eraser_button = QPushButton("Gumka")
        self.eraser_button.setCheckable(True)
        self.eraser_button.clicked.connect(self.handleEraserButton)
        self.eraser_button.setStyleSheet(RED_BUTTON)

        self.color_frame = QFrame()
        self.color_frame.setFrameShape(QFrame.NoFrame)
        self.color_frame.setFixedSize(50, 30)
        self.color_frame.setStyleSheet("background-color: black;")
        self.color_frame.mousePressEvent = self.showColorDialog

        thickness_combobox = QComboBox()
        thickness_combobox.setEditable(True)
        thickness_combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        thickness_combobox.setValidator(QIntValidator(2, 72, thickness_combobox))
        for i in range(2, 73, 2):
            thickness_combobox.addItem(str(i))
        thickness_combobox.currentIndexChanged.connect(self.handleThicknessChange)
                
        dockLayout.addWidget(self.draw_button, alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(self.eraser_button, alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(QLabel("Kolor pędzla:",), alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(self.color_frame, alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(QLabel("Grubość pędzla:"), alignment=QtCore.Qt.AlignCenter)
        dockLayout.addWidget(thickness_combobox, alignment=QtCore.Qt.AlignCenter)

        spacer_item = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        dockLayout.addItem(spacer_item)

    def showColorDialog(self, event):
        if self.eraser_button.isChecked():
            showAlert("Informacja!", "Nie można zmienić koloru kiedy używana jest gumka.", QMessageBox.Information)
            print("Nie można zmienić koloru kiedy używana jest gumka")
            return

        if event.button() == Qt.LeftButton:
            color_dialog = QColorDialog.getColor()
            if color_dialog.isValid():
                color = color_dialog.name()
                self.previous_color = color
                self.scene.drawing_view.brush_color = QColor(color)
                self.color_frame.setStyleSheet("background-color: " + color + ";")

    def handleThicknessChange(self):
        thickness_combobox = self.sender()
        thickness = int(thickness_combobox.currentText())
        self.scene.drawing_view.line_thickness = thickness

    def handleDrawButton(self):
        if self.draw_button.isChecked():
            self.draw_button.setStyleSheet(GREEN_BUTTON)
            self.eraser_button.setStyleSheet(RED_BUTTON)

            self.scene.drawing_view.is_drawing_enabled = True
            self.eraser_button.setChecked(False)
            
            self.scene.drawing_view.brush_color = QColor(self.previous_color)
            color = self.previous_color
            self.color_frame.setStyleSheet("background-color: " + color + ";")
        else:
            self.draw_button.setStyleSheet(RED_BUTTON)
            self.scene.drawing_view.is_drawing_enabled = False

    def handleEraserButton(self):
        if self.eraser_button.isChecked():
            self.eraser_button.setStyleSheet(GREEN_BUTTON)
            self.draw_button.setStyleSheet(RED_BUTTON)
            self.previous_color = self.scene.drawing_view.brush_color.name()
            self.scene.drawing_view.brush_color = QColor("#ffffff")
            self.color_frame.setStyleSheet("background-color: white;")

            self.scene.drawing_view.is_drawing_enabled = True
            self.draw_button.setChecked(False)
        else:
            self.eraser_button.setStyleSheet(RED_BUTTON)
            self.scene.drawing_view.is_drawing_enabled = True

            self.scene.drawing_view.brush_color = QColor(self.previous_color)
            color = self.previous_color
            self.color_frame.setStyleSheet("background-color: " + color + ";")