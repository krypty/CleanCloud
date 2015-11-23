from abc import ABCMeta, abstractmethod

class BaseController:

    def __init__(self, conn, exceptionHandler):
        self._conn = conn
        self._itemsDict = self._build_items_dict()
        self._exceptionHandler = exceptionHandler

    @abstractmethod
    def get_simple_names(self):
        pass

    @abstractmethod
    def get_selected_items(self, listNames):
        pass

    @abstractmethod
    def get_item_details(self, item):
        pass

    @abstractmethod
    def delete(self, listItems):
        pass

    @abstractmethod
    def _build_items_dict(self):
        pass
        # try:
        #     print("todo lol")
        #     return None
        # except Exception as e:
        #     print(e)
        #     # TODO call exception handler