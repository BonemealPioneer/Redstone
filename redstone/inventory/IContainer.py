from zope.interface import interface
from zope.interface.declarations import implements

class IContainer(object):
    """
    Base class for containers
    """

    implements(Interface)

    CONTAINER_SLOTS = 0

    def __init__(self):
        self.slots = {}

        for x in xrange(-1, self.CONTAINER_SLOTS):
            self.slots[x] = -1

    def get_slot_exists(self, slot_id):
        if slot_id in self.slots.keys():
            return True

        return False

    def get_item(self, slot_id):
        if self.slot_exists(slot_id):
            return self.slots[slot_id]

        return None