from abc import ABCMeta, abstractmethod

class BaseController:

    def __init__(self, conn, exceptionHandler = None):
        self._conn = conn
        self.refresh()
        if exceptionHandler is None:
            self._exceptionHandler = defaultHandler()
        else:
            self._exceptionHandler = exceptionHandler

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


class defaultHandler:

    def handle(self, e):
        print("[error]", e)