from PyQt5.QtWidgets import QWidget
from gen.gui.instances_view import Ui_Form
from controllers.InstanceController import InstanceController


class InstancesView(QWidget):
    def __init__(self, conn):
        super(QWidget, self).__init__()

        # Attributes
        self.controller = InstanceController(conn=conn)

        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._refresh_gui()

        # Signals and Slots
        # self.ui.btn.clicked.connect(lambda: self._handle_button("lala"))

    def _handle_button(self, args):
        self.ui.btn_refresh.setText(args)

    def _refresh_gui(self):
        names = self.controller.get_simple_names()
        self.ui.listWidget.addItems(names)
