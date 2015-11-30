from .BaseController import BaseController
import boto.ec2


class InstanceController(BaseController):

    def __init__(self, conn, exceptionHandler = None):
        super(InstanceController, self).__init__(conn, exceptionHandler)
        self._listPertinentTags = ['id', 'image_id', 'region', 'instance_type', 'ip_address', 'private_ip_address', '_state']

    def get_item_details(self, item):
        result = dict()
        try:
            if item is not None:
                try:
                    if len(item.tags['Name']) > 0:
                        result['name'] = item.tags['Name']
                except:
                    pass

                for key in item.__dict__.keys():
                    if key in self._listPertinentTags:
                        info = getattr(item, key)
                        if isinstance(info, boto.ec2.RegionInfo):
                            info = info.name
                        result[key] = str(info)
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
                if instance.state != "terminated" and instance.state != "shutting-down":
                    itemsDict[instance.id] = instance
        except Exception as e:
            self._exceptionHandler.handle(e)
        return itemsDict

