import boto.ec2
import boto.exception
from PyQt5.QtWidgets import QDialog, QMessageBox
from gen.gui.login_dialog import Ui_Dialog
from views.MainWindow import MainWindow
from tools.ReadConfig import read_config
from controllers.InstanceController import InstanceController


# inflate the mainwindow.py gui (generated from res/gui/mainwindow.ui)
class LoginDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.cbx_region.addItems([r.name for r in boto.ec2.regions()])

        # Signals and Slots
        self.ui.btn_login.clicked.connect(self._btn_login_clicked)

    def _btn_login_clicked(self):

        # here we ask the user to give us its credentials
        # access_key_id = self.ui.le_access_key_id.text()
        # secret_key_id = self.ui.le_secret_key_id.text()

        # note: for us select: eu-central-1
        region = self.ui.cbx_region.itemText(self.ui.cbx_region.currentIndex())

        # or we can imagine that if a file credentials.ini is present we use it directly
        config = read_config(r'credentials/credentials.ini')
        access_key_id = config["auth"]["ACCESS_KEY"]
        secret_key_id = config["auth"]["SECRET_KEY"]

        print("access_key_id:", access_key_id)
        print("secret_key_id:", secret_key_id)
        print("region:", region)

        try:
            conn = boto.ec2.connect_to_region(region,
                                              aws_access_key_id=access_key_id,
                                              aws_secret_access_key=secret_key_id)

            mv = MainWindow(conn)
            mv.show()
            self.close()

        except boto.exception.EC2ResponseError:
            msg = "Impossible to log in using these credentials.\n" \
                  "Please check your credentials and regions"

            QMessageBox.critical(self, "Cannot login!", msg)