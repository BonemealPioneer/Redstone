from redstone.containers.IContainer import IContainer

class ContainerVillagerTrading(IContainer):
    CONTAINER_SLOTS = 2

    def __init__(self):
        IContainer.__init__(self)