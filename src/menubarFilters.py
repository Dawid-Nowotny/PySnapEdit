from PyQt5.QtWidgets import QMenu, QAction

class MenubarFilters(QMenu):
    def __init__(self, parent):
        super().__init__("Analiza obrazu", parent)

        recognize_test = QAction("Rozpoznaj tekst na obrazie", self)
        recognize_test.triggered.connect(lambda: print("..."))

        self.addAction(recognize_test)