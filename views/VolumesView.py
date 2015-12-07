from views.BaseBlockView import BaseBlockView
from controllers.VolumesController import VolumesController


class VolumesView(BaseBlockView):
    def __init__(self, conn, handler):
        super(VolumesView, self).__init__(conn, VolumesController, handler)

    def _replace_default_text(self):
        self.ui.lbl_title.setText("Volumes")
        self.ui.gbx_list.setTitle("Volumes list")


