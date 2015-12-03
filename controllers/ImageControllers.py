from .BaseController import BaseController


class ImageController(BaseController):

    def __init__(self, conn, handler=None):
        super(ImageController, self).__init__(conn, handler)
        self._listPertinentTags = ['name', 'description', 'state', 'id']

    def get_item_details(self, item):
        result = dict()
        try:
            if item is not None:
                for key in item.__dict__.keys():
                    if key in self._listPertinentTags:
                        info = getattr(item, key)
                        result[key] = str(info)
        except Exception as e:
            self._handler.handle_error(e.message);
        return result

    def delete(self, listItems):
        for image in listItems:
            try:
                image.deregister(delete_snapshot=True)
                self._handler.handle_message("Image %s has been deleted" % image.id)
            except Exception as e:
                self._handler.handle_error(e.message);

    def _build_items_dict(self):
        itemsDict = dict()
        images = self._conn.get_all_images(owners=["self"])
        for image in images:
            try:
                itemsDict[image.id] = image
            except Exception as e:
                self._handler.handle_error(e.message);
        return itemsDict
