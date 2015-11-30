from views.BaseBlockView import BaseBlockView
from controllers.ElasticIPController import ElasticIPController


class ElasticIPView(BaseBlockView):
    def __init__(self, conn):
        super(ElasticIPView, self).__init__(conn, ElasticIPController)

    def _replace_default_text(self):
        self.ui.lbl_title.setText("Elastic IPs")
        self.ui.gbx_list.setTitle("Elastic IPs list")


