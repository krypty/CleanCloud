from PyQt5.QtWidgets import QMainWindow, QListView
from gen.gui.mainwindow import Ui_MainWindow
from views.InstancesView import InstancesView
from views.ElasticIPView import ElasticIPView
from views.ImageView import ImageView
from views.VolumesView import VolumesView
from PyQt5.QtCore import QCoreApplication


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
        self.ui.action_menu_logout.triggered.connect(self._on_logout_clicked)
        self.ui.action_menu_quit.triggered.connect(self._on_quit_clicked)

    def _handle_button(self, args):
        self.ui.btn_refresh_all.setText(args)

    def _add_blocks_into_grid(self):
        instances_view = InstancesView(conn=self._conn)
        elastic_ip_view = ElasticIPView(conn=self._conn)
        image_view = ImageView(conn=self._conn)
        volumes_view = VolumesView(conn=self._conn)

        self.ui.gl_blocks.addWidget(instances_view, 0, 0)
        self.ui.gl_blocks.addWidget(elastic_ip_view, 1, 0)
        self.ui.gl_blocks.addWidget(image_view, 0, 1)
        self.ui.gl_blocks.addWidget(volumes_view, 1, 1)

    def _on_logout_clicked(self):
        self.close()

    def _on_quit_clicked(self):
        QCoreApplication.instance().quit()
