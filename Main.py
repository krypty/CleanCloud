import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow


# inflate the mainwindow.py gui (generated from res/gui/mainwindow.ui)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signals and Slots
        self.ui.btnHelloWorld.clicked.connect(self._handle_button)

    def _handle_button(self):
        self.ui.btnRefreshInstances.setText("HELLO COCHON !!!")


# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)

    mv = MainWindow()
    mv.show()

    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
