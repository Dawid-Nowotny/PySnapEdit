from PyQt5.QtWidgets import QSlider, QVBoxLayout, QLabel, QDialog, QPushButton
from PyQt5.QtCore import Qt

from doubleSlider import DoubleSlider 

class OddDoubleSlider(DoubleSlider):
    def __init__(self, window_title, title1, min_value1, max_value1, default_value1,
                 title2, min_value2, max_value2, default_value2):
        super().__init__(window_title, title1, min_value1, max_value1, default_value1,
                 title2, min_value2, max_value2, default_value2)
        self.slider1.setTickInterval(2)
        self.slider1.setSingleStep(2)

    def updateLabel1(self, value):
        if value % 2 == 0:
            value -= 1
            self.slider1.setValue(value)
        self.label1.setText(str(value))