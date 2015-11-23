from .BaseController import  BaseController
import boto.ec2

class InstanceController(BaseController):

    def __init__(self, conn, exceptionHandler):
        super(InstanceController, self).__init__(conn, exceptionHandler)
        self._listPertinentTags = ['id', 'image_id', 'region', 'instance_type', 'ip_address', 'private_ip_address', 'state']

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

    def get_item_details(self, item):
        result = dict()
        try:
            if item is not None:
                result['name'] = item.tags['Name']
                info = None
                for key in item.__dict__.keys():
                    info = item.__dict__[key]
                    if key in self._listPertinentTags:
                        if isinstance(info, boto.ec2.RegionInfo):
                            result[key] = info.name
                        else:
                            result[key] = info
        except Exception as e:
            self._exceptionHandler.handle(e)

        return result

    def delete(self, listItems):
        listIds = list()
        for instance in listItems:
            listIds.append(instance.id)

        try:
            self._conn.terminate_instances(instance_ids=listIds)
        except Exception as e:
            self._exceptionHandler.handle(e)

    def _build_items_dict(self):
        itemsDict = dict()
        try:
            reservations = self._conn.get_all_instances()
            instances = [i for r in reservations for i in r.instances]
            for instance in instances:
                if instance.state != "terminated":
                    itemsDict[instance.id] = instance
        except Exception as e:
            self._exceptionHandler.handle(e)
        return itemsDict