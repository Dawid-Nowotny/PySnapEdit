from PyQt5.QtWidgets import QMenu, QAction

class MenubarView(QMenu):
    def __init__(self, parent):
        super().__init__("Widok", parent)

        zoom_in = QAction("Przybliż", self)
        zoom_out = QAction("Oddal ", self)

        self.addAction(zoom_in)
        self.addAction(zoom_out)