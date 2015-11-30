from views.BaseBlockView import BaseBlockView
from controllers.InstanceController import InstanceController
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon


class InstancesView(BaseBlockView):
    def __init__(self, conn):
        super(InstancesView, self).__init__(conn, InstanceController)

        # Attributes
        self._btn_stop = QPushButton()
        self._btn_stop.setText("Stop")
        self._btn_stop.setIcon(QIcon.fromTheme("process-stop"))
        self.ui.l_bottom.insertWidget(2, self._btn_stop)

        # Signals and Slots
        self._btn_stop.clicked.connect(self._on_btn_stop_clicked)

    def _on_btn_stop_clicked(self):
        # TODO...
        raise NotImplemented()

    def _replace_default_text(self):
        self.ui.lbl_title.setText("Instances")
        self.ui.gbx_list.setTitle("Instances list")

    def _update_item_count_in_gui(self, count):
        if count > 0:
            self.ui.btn_delete.setText("Delete (%s)" % count)
            self._btn_stop.setText("Stop (%s)" % count)

        else:
            self.ui.btn_delete.setText("Delete")
            self._btn_stop.setText("Stop")


