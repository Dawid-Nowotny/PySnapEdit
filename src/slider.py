from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSlider, QPushButton
from PyQt5.QtCore import Qt

class Slider(QDialog):
    def __init__(self, window_title, label_title, min_value, max_value, default_value):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setWindowTitle(window_title)

        self.label_name = QLabel(label_title)
        self.label = QLabel(str(default_value))
        self.label_name.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)
        
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(default_value)
        slider.valueChanged.connect(self.updateLabel)
        
        button = QPushButton("OK")
        button.clicked.connect(self.accept)
        
        layout.addWidget(self.label_name)
        layout.addWidget(self.label)
        layout.addWidget(slider)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def updateLabel(self, value):
        self.label.setText(str(value))