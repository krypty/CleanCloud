from abc import ABCMeta, abstractmethod
from handlers.BaseHandler import BaseHandler

class BaseController:

    def __init__(self, conn, handler=None):
        self._conn = conn
        self.refresh()
        if handler is None:
            self._handler = defaultHandler()
        else:
            self._handler = handler

    def get_simple_names(self):
        if self._itemsDict is not None:
            return list(self._itemsDict.keys())
        return list()

    def get_selected_items(self, listIds):
        listObjects = list()
        try:
            if self._itemsDict is not None:
                for id in listIds:
                    if id in list(self._itemsDict.keys()):
                        listObjects.append(self._itemsDict[id])
        except Exception as e:
            self._exceptionHandler.handle(e)

        return listObjects

    @abstractmethod
    def get_item_details(self, item):
        pass

    @abstractmethod
    def delete(self, listItems):
        pass

    def refresh(self):
        self._itemsDict = self._build_items_dict()

    @abstractmethod
    def _build_items_dict(self):
        pass


class defaultHandler(BaseHandler):

    def handle_warning(self, warning):
        print(warning)

    def handle_info(self, info):
        print(info)

    def handle_error(self, error):
        print(error)

    def handle_message(self, message):
        print(message)