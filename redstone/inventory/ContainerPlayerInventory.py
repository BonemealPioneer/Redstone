from redstone.containers.IContainer import IContainer

class ContainerPlayerInventory(IContainer):
    CONTAINER_SLOTS = 45

    def __init__(self):
        IContainer.__init__(self)