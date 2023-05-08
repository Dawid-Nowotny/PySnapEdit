from PyQt5.QtWidgets import QMenuBar, QAction, QApplication, QDialog
from PyQt5.QtGui import QKeySequence

from resolutionPickerDialog import ResolutionPickerDialog

class Menubar(QMenuBar):
    def __init__(self, parent, scene, file, zoom, side_menu):
        super().__init__()
        file_menu = self.addMenu("Plik")
        open_file = QAction("Otwórz", self)
        open_file.triggered.connect(lambda: scene.setImage(parent, file))
        open_file.setShortcut(QKeySequence("Ctrl+O"))

        create_file = QAction("Utwórz", self)
        create_file.triggered.connect(lambda: self.showResDialog(parent, scene))
        create_file.setShortcut(QKeySequence("Ctrl+R"))

        new_window = QAction("Nowe okno", self)
        new_window.triggered.connect(parent.openNewWindow)
        new_window.setShortcut(QKeySequence("Ctrl+N"))

        save_file = QAction("Zapisz", self)
        save_file.triggered.connect(lambda: file.saveToOriginal(scene))
        save_file.setShortcut(QKeySequence("Ctrl+S"))

        save_fileAs = QAction("Zapisz jako", self)
        save_fileAs.triggered.connect(lambda: file.saveFileAs(self, scene))
        save_fileAs.setShortcut(QKeySequence("Ctrl+Shift+S"))

        clear_image = QAction("Wyczyść płótno", self)
        clear_image.triggered.connect(lambda: scene.clearPalette(parent, file, zoom, side_menu))
        clear_image.setShortcut(QKeySequence("Ctrl+X"))

        close_window = QAction("Zamknij okno", self)
        close_window.triggered.connect(lambda: parent.close())
        close_window.setShortcut(QKeySequence("Ctrl+W"))

        close_app = QAction("Zakończ", self)
        close_app.triggered.connect(lambda: QApplication.quit())
        close_app.setShortcut(QKeySequence("Ctrl+Q"))

        file_menu.addAction(open_file)
        file_menu.addAction(create_file)
        file_menu.addAction(new_window)
        file_menu.addSeparator()
        file_menu.addAction(save_file)
        file_menu.addAction(save_fileAs)
        file_menu.addSeparator()
        file_menu.addAction(clear_image)
        file_menu.addSeparator()
        file_menu.addAction(close_window)
        file_menu.addAction(close_app)

    def showResDialog(slef, parent, scene):
        dialog = ResolutionPickerDialog(parent)
        if dialog.exec_() == QDialog.Accepted:
            x = int(dialog.x_input.text())
            y = int(dialog.y_input.text())
            color = dialog.selected_color.name()
            scene.addColorField(parent, x, y, color)