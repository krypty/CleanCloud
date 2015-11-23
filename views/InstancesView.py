from PyQt5.QtCore import pyqtSlot
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

        # Signals and Slots
        self.ui.btn_refresh.clicked.connect(self._refresh_gui)
        self.ui.lw_instances.itemSelectionChanged.connect(self._on_item_selection_changed)
        self.ui.btn_delete.clicked.connect(self._on_btn_delete_clicked)

        self._refresh_gui()

    def _handle_button(self, args):
        self.ui.btn_refresh.setText(args)

    def _refresh_gui(self):
        self.controller.refresh()
        names = self.controller.get_simple_names()
        print("refresh_gui", names)
        self.ui.lw_instances.clear()
        self.ui.lw_instances.addItems(names)

    def _on_btn_delete_clicked(self):
        selected_items_str = [item.text() for item in self.ui.lw_instances.selectedItems()]
        selected_items = self.controller.get_selected_items(selected_items_str)
        self.controller.delete(selected_items)

        self._refresh_gui()

    def _on_item_selection_changed(self):
        self.ui.lbl_details_data.clear()

        selected_item_count = len(self.ui.lw_instances.selectedItems())
        self._update_item_count_in_gui(selected_item_count)

        if selected_item_count == 1:
            selected_item_str = self.ui.lw_instances.selectedItems()[0].text()
            selected_items = self.controller.get_selected_items([selected_item_str])
            item_details = self.controller.get_item_details(selected_items[0])

            # TODO better string formatting
            item_details_str = ""
            for key, value in item_details.items():
                item_details_str += "%s, %s\n" % (key, value)

            self.ui.lbl_details_data.setText(item_details_str)

    def _update_item_count_in_gui(self, count):
        if count > 0:
            self.ui.btn_delete.setText("Delete (%s)" % count)
            self.ui.btn_stop.setText("Stop (%s)" % count)

        else:
            self.ui.btn_delete.setText("Delete")
            self.ui.btn_stop.setText("Stop")
