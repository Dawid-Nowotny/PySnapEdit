from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt

class RecognizedDialog(QDialog):
    def __init__(self, text):
        super().__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.setWindowTitle("Rozpoznany tekst")
        self.label = QTextEdit(self)
        self.label.setReadOnly(True)
        self.label.setText(text)

        self.button = QPushButton("Zamknij", self)
        self.button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)