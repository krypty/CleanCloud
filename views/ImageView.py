from views.BaseBlockView import BaseBlockView
from controllers.ImageControllers import ImageController


class ImageView(BaseBlockView):
    def __init__(self, conn, handler):
        super(ImageView, self).__init__(conn, ImageController, handler)

    def _replace_default_text(self):
        self.ui.lbl_title.setText("Images")
        self.ui.gbx_list.setTitle("Images list")


