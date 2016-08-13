from redstone.containers.IContainer import IContainer

class ContainerEnchantmentTable(IContainer):
    CONTAINER_SLOTS = 1

    def __init__(self):
        IContainer.__init__(self)