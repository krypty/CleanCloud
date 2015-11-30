from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont
from gen.gui.instances_view import Ui_Form


class BaseBlockView(QWidget):
    def __init__(self, conn, controller):
        super(QWidget, self).__init__()

        # Attributes
        self._controller = controller(conn=conn)
        self._form_label_font = QFont()
        self._form_label_font.setBold(True)

        # Set up the user interface from Designer.
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Signals and Slots
        self.ui.btn_refresh.clicked.connect(self._refresh_gui)
        self.ui.lw_instances.itemSelectionChanged.connect(self._on_item_selection_changed)
        self.ui.btn_delete.clicked.connect(self._on_btn_delete_clicked)
        self.ui.btn_select_all.clicked.connect(self._on_btn_select_all_clicked)

        self._replace_default_text()
        self._refresh_gui()

    def _handle_button(self, args):
        self.ui.btn_refresh.setText(args)

    def _refresh_gui(self):
        self._controller.refresh()
        names = self._controller.get_simple_names()
        print("refresh_gui", names)
        self.ui.lw_instances.clear()
        self.ui.lw_instances.addItems(names)

    def _on_btn_delete_clicked(self):
        selected_items_str = [item.text() for item in self.ui.lw_instances.selectedItems()]
        selected_items = self._controller.get_selected_items(selected_items_str)
        self._controller.delete(selected_items)

        self._refresh_gui()

    def _on_item_selection_changed(self):
        self._clear_layout(self.ui.fl_details_data)

        selected_item_count = len(self.ui.lw_instances.selectedItems())
        self._update_item_count_in_gui(selected_item_count)

        if selected_item_count == 1:
            selected_item_str = self.ui.lw_instances.selectedItems()[0].text()
            selected_items = self._controller.get_selected_items([selected_item_str])
            item_details = self._controller.get_item_details(selected_items[0])

            for key, value in item_details.items():
                lbl_name = QLabel(" ".join(key.split("_")).strip())  # remove underscores
                lbl_name.setFont(self._form_label_font)

                lbl_value = QLabel(value)

                self.ui.fl_details_data.addRow(lbl_name, lbl_value)

    def _update_item_count_in_gui(self, count):
        if count > 0:
            self.ui.btn_delete.setText("Delete (%s)" % count)

        else:
            self.ui.btn_delete.setText("Delete")

    def _on_btn_select_all_clicked(self):
        self.ui.lw_instances.selectAll()

    def _replace_default_text(self):
        raise NotImplemented()

    @staticmethod
    def _clear_layout(layout):
        while layout.count():
            child = layout.takeAt(0)
            child.widget().deleteLater()
