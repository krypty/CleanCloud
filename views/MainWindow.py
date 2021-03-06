from PyQt5.QtWidgets import QMainWindow, QListView
from gen.gui.mainwindow import Ui_MainWindow
from views.InstancesView import InstancesView
from views.ElasticIPView import ElasticIPView
from views.ImageView import ImageView
from views.VolumesView import VolumesView
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot
from handlers.GuiHandler import GuiHandler


# inflate the mainwindow.py gui (generated from res/gui/mainwindow.ui)


class MainWindow(QMainWindow):
    def __init__(self, conn):
        super(MainWindow, self).__init__()

        # private attributes
        self._conn = conn

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._handler = GuiHandler(30, self._on_new_console_message)
        self._instances_view = InstancesView(conn=self._conn, handler=self._handler)
        self._elastic_ip_view = ElasticIPView(conn=self._conn, handler=self._handler)
        self._image_view = ImageView(conn=self._conn, handler=self._handler)
        self._volumes_view = VolumesView(conn=self._conn, handler=self._handler)

        self._views = [
            self._instances_view,
            self._elastic_ip_view,
            self._image_view,
            self._volumes_view
        ]

        self._add_blocks_into_grid()

        # debuging purpose
        # sc_groups = conn.get_all_security_groups()
        # print(sc_groups)

        # Signals and Slots
        self.ui.btn_delete_all.clicked.connect(lambda: self._on_btn_delete_all_clicked())
        self.ui.btn_refresh_all.clicked.connect(lambda: self._on_btn_refresh_all_clicked())
        self.ui.action_menu_logout.triggered.connect(self._on_logout_clicked)
        self.ui.action_menu_quit.triggered.connect(self._on_quit_clicked)
        self.ui.gbx_console.toggled.connect(self._on_console_toggled)

    def _on_btn_delete_all_clicked(self):
        for view in self._views:
            view.delete_all()
            view.refresh_gui()

    def _on_btn_refresh_all_clicked(self):
        for view in self._views:
            view.refresh_gui()

    def _on_console_toggled(self, toogled):
        if not toogled:
            self._show_console()
        else:
            self._hide_console()

    @pyqtSlot(list)
    def _on_new_console_message(self, listMessage):
        htmlText = "<br />".join(listMessage)
        self.ui.tb_console.setHtml(htmlText)

    def _add_blocks_into_grid(self):
        self.ui.gl_blocks.addWidget(self._instances_view, 0, 0)
        self.ui.gl_blocks.addWidget(self._elastic_ip_view, 1, 0)
        self.ui.gl_blocks.addWidget(self._image_view, 0, 1)
        self.ui.gl_blocks.addWidget(self._volumes_view, 1, 1)

    def _on_logout_clicked(self):
        self.close()

    def _on_quit_clicked(self):
        QCoreApplication.instance().quit()

    def _show_console(self):
        self.ui.tb_console.setVisible(False)

    def _hide_console(self):
        self.ui.tb_console.setVisible(True)
