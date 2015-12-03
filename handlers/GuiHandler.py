from .BaseHandler import BaseHandler
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore


class GuiHandler(BaseHandler):

    def __init__(self, size, callbackMethod):
        super(GuiHandler, self).__init__(size)
        self._callback = callbackMethod

    def handle_message(self, message):
        self._add_message(message)

    def handle_info(self, info):
        info = "<span style=\"color: blue\">" + info + "</span>"
        self._add_message(info)

    def handle_error(self, error):
        error = "<span style=\"color: red\">" + error + "</span>"
        self._add_message(error)

    def handle_warning(self, warning):
        warning = "<span style=\"color: orange\">" + warning + "</span>"
        self._add_message(warning)

    def new_message_signal(self):
        return self._signalSender.signal()

    def _add_message(self, message):
        super(GuiHandler, self)._add_message(message)
        self._callback(self._listMessages)

