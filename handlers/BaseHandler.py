from abc import ABCMeta, abstractmethod
from datetime import datetime

class BaseHandler():

    def __init__(self, size):
        self._listMessages = list()
        self._size = 10
        self._internCounter = 0
        try:
            if int(size) > 0:
                self._size = size
        except:
            pass

    @abstractmethod
    def handle_message(self, message):
        pass

    @abstractmethod
    def handle_warning(self, warning):
        pass

    @abstractmethod
    def handle_info(self, info):
        pass

    @abstractmethod
    def handle_error(self, error):
        pass

    def get_messages_list(self):
        return self._listMessages

    def _add_message(self, message):

        self._listMessages.append(self._add_time_to_message(message))
        self._internCounter += 1
        if self._internCounter == self._size:
            self._listMessages = self._listMessages[1:]
            self._internCounter -= 1

    def _add_time_to_message(self, message):
        time = datetime.now().time()
        time = "[" + str(time).split('.')[0] + "] "
        return time + message
