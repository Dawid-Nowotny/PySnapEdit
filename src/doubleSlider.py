from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSlider, QPushButton
from PyQt5.QtCore import Qt

class DoubleSlider(QDialog):
    def __init__(self, window_title, title1, min_value1, max_value1, default_value1,
                 title2, min_value2, max_value2, default_value2):
        super().__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        layout = QVBoxLayout()
        
        self.setWindowTitle(window_title)

        self.label1 = QLabel(str(default_value1))
        self.label2 = QLabel(str(default_value2))

        self.label1_name = QLabel(title1)
        self.label2_name = QLabel(title2)

        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label1_name.setAlignment(Qt.AlignCenter)
        self.label2_name.setAlignment(Qt.AlignCenter)
        
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMinimum(min_value1)
        self.slider1.setMaximum(max_value1)
        self.slider1.setValue(default_value1)
        self.slider1.valueChanged.connect(self.updateLabel1)
        
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMinimum(min_value2)
        self.slider2.setMaximum(max_value2)
        self.slider2.setValue(default_value2)
        self.slider2.valueChanged.connect(self.updateLabel2)
            
        button = QPushButton("OK")
        button.clicked.connect(self.accept)

        layout.addWidget(self.label1_name)
        layout.addWidget(self.label1)
        layout.addWidget(self.slider1)
        layout.addWidget(self.label2_name)
        layout.addWidget(self.label2)
        layout.addWidget(self.slider2)
        layout.addWidget(button)

        self.setLayout(layout)
        
    def updateLabel1(self, value):
        self.label1.setText(str(value))
        
    def updateLabel2(self, value):
        self.label2.setText(str(value))