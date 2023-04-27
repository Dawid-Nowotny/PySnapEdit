from PyQt5.QtWidgets import QMessageBox

MENU_STYLE = " QMenuBar {padding: 0px; } \
    QMenuBar::item { padding: 2px 10px; background-color: transparent; color: black; text-align: left; } \
    QMenuBar::item:selected { background-color: #90c8f6; }"

def showAlert(title, message, icon):
    alert = QMessageBox()
    alert.setWindowTitle(title)
    alert.setText(message)
    alert.setIcon(icon)
    alert.exec_()