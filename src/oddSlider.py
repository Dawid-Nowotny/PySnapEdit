from PyQt5.QtWidgets import QSlider, QVBoxLayout, QLabel, QDialog, QPushButton
from PyQt5.QtCore import Qt

from slider import Slider 

class OddSlider(Slider):
    def __init__(self, window_title, label_title, min_value, max_value, default_value):
        super().__init__(window_title, label_title, min_value, max_value, default_value)
        self.slider.setTickInterval(2)
        self.slider.setSingleStep(2)

    def updateLabel(self, value):
        if value % 2 == 0:
            value -= 1
        self.label.setText(str(value))