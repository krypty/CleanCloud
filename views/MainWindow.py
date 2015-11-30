from PyQt5.QtWidgets import QMainWindow, QListView
from gen.gui.mainwindow import Ui_MainWindow
from views.InstancesView import InstancesView


# inflate the mainwindow.py gui (generated from res/gui/mainwindow.ui)


class MainWindow(QMainWindow):
    def __init__(self, conn):
        super(MainWindow, self).__init__()

        # private attributes
        self._conn = conn

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._add_blocks_into_grid()


        # debuging purpose
        # sc_groups = conn.get_all_security_groups()
        # print(sc_groups)

        # Signals and Slots
        # TODO add signal/slots for delete all and refresh all
        self.ui.btn_delete_all.clicked.connect(lambda: self._handle_button("lala"))
        self.ui.btn_refresh_all.clicked.connect(lambda: self._handle_button("lala"))

    def _handle_button(self, args):
        self.ui.btn_refresh_all.setText(args)

    def _add_blocks_into_grid(self):
        instances_view = InstancesView(conn=self._conn)

        self.ui.gl_blocks.addWidget(instances_view, 0, 0)

        # TODO add reals views
        self.ui.gl_blocks.addWidget(QListView(), 0, 1)
        self.ui.gl_blocks.addWidget(QListView(), 1, 0)
        self.ui.gl_blocks.addWidget(QListView(), 1, 1)
