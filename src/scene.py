from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QDesktopWidget, QGraphicsPixmapItem, QMessageBox

from config import showAlert

class Scene:
    def __init__(self, parent):
        self.graphicsScene = QGraphicsScene(parent)
        self.view = QGraphicsView(self.graphicsScene)
        self.view.setStyleSheet("background-color: #c0c0c0;")
        self.is_image_displayed = False
        self.window_width = 0
        self.window_height = 0

    def setImage(self, parent, file):
        try:
            item, img_height, img_width, file_name = file.openFile()
            img_height += 25
            img_width += 5
            print(self.is_image_displayed)

            if self.is_image_displayed:
                parent.openNewWindowWithImage(item, img_height, img_width, file_name)
                return
            else:
                self.graphicsScene.addItem(item)
                self.adjustWindowDimensions(parent, img_height, img_width, file_name)
        except:
            return

    def adjustWindowDimensions(self, parent, img_height, img_width, file_name):
        window_width = parent.width()
        window_height = parent.height()

        # ok
        if window_width >= img_width and window_height >= img_height:
            parent.setWindowTitle("PySnapEdit - " + file_name)

        # window too narrow
        if window_width < img_width and window_height >= img_height:
            parent.setGeometry(parent.window_x, parent.window_y, img_width, window_height)

        # window too short
        if window_height < img_height and window_width >= img_width:
            parent.setGeometry(parent.window_x, parent.window_y, window_width, img_height)

        # maximalize
        if img_height > QDesktopWidget().screenGeometry().height() or img_width > QDesktopWidget().screenGeometry().width():
            parent.showMaximized()
            parent.setWindowTitle("PySnapEdit - " + file_name)
            self.is_image_displayed = True
            return

        # too narrow and too short
        if window_width < img_width and window_height < img_height:
            parent.setGeometry(self.window_x, self.window_y, img_width, img_height)

        qr = parent.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        parent.move(qr.topLeft())

        parent.setWindowTitle("PySnapEdit - " + file_name)
        self.is_image_displayed = True

    def applyFilter(self, pixmap):
        item = QGraphicsPixmapItem(pixmap)
        self.graphicsScene.clear()
        self.graphicsScene.addItem(item)

    def checkEmpty(self):
        if len(self.graphicsScene.items()) == 0:   
            showAlert("Błąd!", "Brak zdjęcia do nałożenia filtra.", QMessageBox.Warning)
            print("Brak zdjęcia do nałożenia filtra")
            return True

    def clearPalette(self, parent, file):
        self.is_image_displayed = False

        self.graphicsScene.clear()
        file.restartImage()
        parent.restartWindowLocation()

        self.graphicsScene = QGraphicsScene()
        self.view.setScene(self.graphicsScene)
        parent.setWindowTitle("PySnapEdit")