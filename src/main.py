import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

from scene import Scene
from fileOperations import File
from zoom import Zoom

from sideMenu import SideMenu
from menubar import Menubar
from menubarFilters import MenubarFilters
from menubarCompression import MenubarCompression
from menubarAnalizer import MenubarAnalize
from menubarView import MenubarView
from menubarManageDock import MenubarManageDock

from config import MENU_STYLE

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file = File()
        self.scene = Scene(self, self.file)
        self.zoom = Zoom(self.scene)

        self.window_list = []

        self.initGUI()
        self.show()

    def initGUI(self):
        self.setWindowTitle("PySnapEdit")
        self.setWindowIcon(QtGui.QIcon("files\\icon.png"))

        side_menu = SideMenu(self, self.scene)
        menubar = Menubar(self, self.scene, self.file, self.zoom)
        menubar.setStyleSheet(MENU_STYLE)
        self.setMenuBar(menubar)
        menubar.addMenu(MenubarFilters(self, self.scene))
        menubar.addMenu(MenubarCompression(self, self.scene, self.file))
        menubar.addMenu(MenubarAnalize(self, self.scene))
        menubar.addMenu(MenubarView(self, self.zoom))
        menubar.addMenu(MenubarManageDock(self, self.scene, side_menu))

        self.restartWindowLocation()
        self.setMinimumSize(400, 100)
        self.setCentralWidget(self.scene.view)

    def restartWindowLocation(self):
        self.showNormal()

        screen_size = QApplication.primaryScreen().size()
        window_width = int(screen_size.width() * 0.5)
        window_height = int(screen_size.height() * 0.5)
        self.window_x = int((screen_size.width() - window_width) / 2)
        self.window_y = int((screen_size.height() - window_height) / 2)

        self.setGeometry(self.window_x, self.window_y, window_width, window_height)

    def openNewWindow(self):
        new_window = Main()
        self.window_list.append(new_window)
        new_window.show()

    def openNewWindowWithImage(self, item, img_height, img_width, file_name):
        new_window = Main()
        self.window_list.append(new_window)
        new_window.scene.graphicsScene.addItem(item)
        new_window.scene.is_image_displayed = True
        new_window.scene.adjustWindowDimensions(new_window, img_height, img_width, file_name)
        
        if file_name is not None:
            new_window.file.image_path = file_name

        new_window.show()

if __name__ == '__main__':
   App = QApplication(sys.argv)
   window = Main()
   sys.exit(App.exec())