from redstone.containers.IContainer import IContainer

class ContainerCraftingTable(IContainer):
    CONTAINER_SLOTS = 9

    def __init__(self):
        IContainer.__init__(self)