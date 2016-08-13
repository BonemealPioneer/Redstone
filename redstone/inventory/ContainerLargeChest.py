from redstone.containers.IContainer import IContainer

class ContainerLargeChest(IContainer):
    CONTAINER_SLOTS = 53

    def __init__(self):
        IContainer.__init__(self)