from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QDesktopWidget, QGraphicsPixmapItem, QMessageBox
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPixmap
from functools import partial

from config import SCENE_STYLE, showAlert

class Scene:
    def __init__(self, parent, file):
        self.graphicsScene = QGraphicsScene(parent)
        self.view = QGraphicsView(self.graphicsScene)
        self.view.setStyleSheet(SCENE_STYLE)
        self.is_image_displayed = False
        self.window_width = 0
        self.window_height = 0

        self.view.setAcceptDrops(True)
        self.view.dragEnterEvent = self.dragEnterEvent
        self.view.dragMoveEvent = self.dragMoveEvent
        dropPartial = partial(self.dropEvent, parent=parent, file=file)
        self.view.dropEvent = dropPartial

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        event.setDropAction(Qt.MoveAction)
        event.accept()

    def addItemToScene(self, parent, item, img_height, img_width, file_name):
        img_height += 25
        img_width += 5

        if self.is_image_displayed:
            parent.openNewWindowWithImage(item, img_height, img_width, file_name)
            return
        else:
            self.graphicsScene.addItem(item)
            self.adjustWindowDimensions(parent, img_height, img_width, file_name)

    def dropEvent(self, event, parent, file):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            for url in event.mimeData().urls():
                file_name = url.toLocalFile()

                try:
                    if file.isImageFile(file_name):
                        item = QGraphicsPixmapItem(QPixmap(file_name))
                        img_height = int(item.boundingRect().height())
                        img_width = int(item.boundingRect().width())
                        self.addItemToScene(parent, item, img_height, img_width, file_name)
                    else:
                        event.ignore()
                except:
                    event.ignore()
        else:
            event.ignore()

    def setImage(self, parent, file):
        try:
            item, img_height, img_width, file_name = file.openFile()
            self.addItemToScene(parent, item, img_height, img_width, file_name)
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
            showAlert("Błąd!", "Brak zdjęcia, dodaj zdjęcie aby wykonać na nim operacje.", QMessageBox.Warning)
            print("Brak zdjęcia, dodaj zdjęcie aby wykonać na nim operacje.")
            return True

    def clearPalette(self, parent, file, zoom):
        zoom.zoomRestart()
        self.is_image_displayed = False
    
        self.graphicsScene.clear()
        file.restartImage()
        parent.restartWindowLocation()

        self.graphicsScene = QGraphicsScene()
        self.view.setScene(self.graphicsScene)
        parent.setWindowTitle("PySnapEdit")