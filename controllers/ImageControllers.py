from .BaseController import BaseController


class ImageController(BaseController):

    def __init__(self, conn, exceptionHandler = None):
        super(ImageController, self).__init__(conn, exceptionHandler)
        self._listPertinentTags = ['name', 'description', 'state']

    def get_item_details(self, item):
        result = dict()
        try:
            if item is not None:
                print(item.__dict__)
                for key in item.__dict__.keys():
                    if key in self._listPertinentTags:
                        info = getattr(item, key)
                        result[key] = info
        except Exception as e:
            self._exceptionHandler.handle(e);
        return result

    def delete(self, listItems):
        for image in listItems:
            try:
                image.deregister(delete_snapshot=True)
            except Exception as e:
                self._exceptionHandler.handle(e)

    def _build_items_dict(self):
        itemsDict = dict()
        images = self._conn.get_all_images(owners=["self"])
        for image in images:
            try:
                itemsDict[image.id] = image
            except Exception as e:
                self._exceptionHandler.handle(e)
        return itemsDict
