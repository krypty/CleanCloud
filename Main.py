import configparser
import sys
from views.LoginDialog import LoginDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from views.MainWindow import MainWindow


def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    return config


# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)

    login_dialog = LoginDialog()
    login_dialog.show()
    mv = MainWindow()
    mv.show()

    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
