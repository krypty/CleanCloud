from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from gen.gui.mainwindow import Ui_MainWindow

# inflate the mainwindow.py gui (generated from res/gui/mainwindow.ui)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signals and Slots
        self.ui.btnHelloWorld.clicked.connect(lambda: self._handle_button("lala"))

    def _handle_button(self, args):
        self.ui.btnRefreshInstances.setText(args)