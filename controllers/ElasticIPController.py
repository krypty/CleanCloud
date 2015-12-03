from .BaseController import BaseController
import boto.ec2


class ElasticIPController(BaseController):

    def __init__(self, conn, handler=None):
        super(ElasticIPController, self).__init__(conn, handler)
        self._listPertinentTags = ['public_ip', 'instance_id', 'allocation_id' 'private_ip_address', 'region']

    def get_item_details(self, item):
        result = dict()
        try:
            if item is not None:
                for key in item.__dict__.keys():
                    info = getattr(item, key)
                    if key in self._listPertinentTags:
                        if isinstance(info, boto.ec2.RegionInfo):
                            info = info.name
                        result[key] = str(info)
        except Exception as e:
            self._handler.handle_error(e.message);
        return result

    def delete(self, listItems):
        for ip in listItems:
            try:
                if ip.instance_id:
                    ip.disassociate()
                ip.release()
                self._handler.handle_message("Elastic IP %s has been released"%ip.public_ip)
            except Exception as e:
                self._handler.handle_error(e.message);

    def _build_items_dict(self):
        itemsDict = dict()
        addresses = self._conn.get_all_addresses()
        for addr in addresses:
            try:
                itemsDict[addr.public_ip] = addr
            except Exception as e:
                self._handler.handle_error(e.message);
        return itemsDict
