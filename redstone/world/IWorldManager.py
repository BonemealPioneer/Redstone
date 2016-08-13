from zope.interface import Interface
from zope.interface import implements

from redstone.world.World import World

class IWorldManager(object):
    """
    A class for managing multiple worlds
    """

    implements(Interface)

    def __init__(self):
        self.loaded_worlds = {}

    def get_world_loaded(self, world_name):
        if world_name in self.loaded_worlds.keys():
            return True

        return False

    def get_player_in_world(self, player_name, world_name):
        if player_name in self.loaded_worlds[world_name \
            ].players.keys():

            return True

        return False

    def load_world(self):
        """
        Stores as {World Name}: World Instance
        """

    def unload_world(self, world_name):
        """
        Unloads a loaded world by world_name
        """

        pass