from PyQt5.QtWidgets import QDialog, QLabel, QSpinBox, QPushButton, QColorDialog, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class ResolutionPickerDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Dodaj pole koloru")
        self.layout = QVBoxLayout()

        self.x_label = QLabel("Szerokość:")
        self.x_input = QSpinBox()
        self.x_input.setRange(50, 2048)
        self.x_input.setValue(800)
        self.layout.addWidget(self.x_label)
        self.layout.addWidget(self.x_input)

        self.y_label = QLabel("Wysokość:")
        self.y_input = QSpinBox()
        self.y_input.setRange(50, 2048)
        self.y_input.setValue(800)
        self.layout.addWidget(self.y_label)
        self.layout.addWidget(self.y_input)

        self.selected_color = QColor("white")

        self.color_button = QPushButton("Wybierz kolor tła")
        self.color_button.clicked.connect(self.selectColor)
        self.layout.addWidget(self.color_button)

        self.add_button = QPushButton("Dodaj pole")
        self.add_button.clicked.connect(lambda: self.accept())
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)

    def selectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color