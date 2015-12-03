from .BaseController import BaseController
import boto.ec2


class VolumesController(BaseController):

    def __init__(self, conn, handler=None):
        super(VolumesController, self).__init__(conn, handler)
        self._listPertinentTags = ['id', 'size', 'type', 'status']

    def delete(self, listItems):
        for volume in listItems:
            try:
                state = volume.attachment_state()
                if state == u"attaching" or state == u"attached":
                    filter = {'block-device-mapping.volume-id': volume.id}
                    volumesReservations = self._conn.get_all_instances(filters=filter)
                    volumesInstances = [i for r in volumesReservations for i in r.instances]
                    ids = [i.id for i in volumesInstances]
                    self._conn.terminate_instances(instance_ids=ids)
                    for id in ids:
                        try:
                            self._conn.detach_volume(volume_id=volume.id, instance_id=id, force=True)
                            self._handler.handle_message("Volume %s has been detached before deletion" % volume.id)
                        except:
                            pass
                self._conn.delete_volume(volume.id)
                self._handler.handle_message("Volume %s has been deleted"%volume.id)
            except Exception as e:
                self._handler.handle_error(e.message)

    def get_item_details(self, item):
        result = dict()
        try:
            if item is not None:
                for key in item.__dict__.keys():
                    info = getattr(item, key)
                    if key in self._listPertinentTags:
                        if key == 'size':
                            info = str(info) + "GB"
                        if isinstance(info, boto.ec2.RegionInfo):
                            info = info.name
                        result[key] = str(info)
        except Exception as e:
            self._handler.handle_error(e.message);
        return result

    def _build_items_dict(self):
        itemsDict = dict()
        volumes = self._conn.get_all_volumes()
        for vol in volumes:
            itemsDict[vol.id] = vol
        return itemsDict
