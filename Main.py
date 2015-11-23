import sys
from views.LoginDialog import LoginDialog
from PyQt5.QtWidgets import QApplication

# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)

    login_dialog = LoginDialog()
    login_dialog.show()

    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
