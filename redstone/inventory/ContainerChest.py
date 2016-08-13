from redstone.containers.IContainer import IContainer

class ContainerChest(IContainer):
    CONTAINER_SLOTS = 26

    def __init__(self):
        IContainer.__init__(self)