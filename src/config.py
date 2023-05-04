from PyQt5.QtWidgets import QMessageBox

MENU_STYLE = " QMenuBar {padding: 0px; } \
    QMenuBar::item { padding: 2px 10px; background-color: transparent; color: black; text-align: left; } \
    QMenuBar::item:selected { background-color: #90c8f6; }"

SCENE_STYLE = "background-color: #c0c0c0;"

RED_BUTTON = "background-color: #FFCCCB"

GREEN_BUTTON = "background-color: #006400"

def showAlert(title, message, icon):
    alert = QMessageBox()
    alert.setWindowTitle(title)
    alert.setText(message)
    alert.setIcon(icon)
    alert.exec_()