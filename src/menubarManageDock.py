from PyQt5.QtWidgets import QMenu, QAction, QMessageBox
from PyQt5.QtGui import QKeySequence

class MenubarManageDock(QMenu):
    def __init__(self, parent, scene, side_menu):
        super().__init__("Okna", parent)
        self.visability_dock = True
        self.side_menu = side_menu
        
        self.side_menu.dock.visibilityChanged.connect(self.handleDockVisibilityChanged)

        visability_dock = QAction("Ukrycie doków", self)
        visability_dock.triggered.connect(self.toggleHideDock)
        visability_dock.setShortcut(QKeySequence("Tab"))
        visability_dock.setCheckable(True)
        visability_dock.setChecked(self.side_menu.dock.isVisible())

        self.addAction(visability_dock)
        self.visability_dock_action = visability_dock

    def toggleHideDock(self):
        self.visability_dock = not self.visability_dock
        self.side_menu.dock.setVisible(self.visability_dock)
        self.visability_dock_action.setChecked(self.visability_dock)

    def handleDockVisibilityChanged(self, visible):
        self.visability_dock = visible
        self.visability_dock_action.setChecked(visible)
