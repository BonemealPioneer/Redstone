from redstone.containers.IContainer import IContainer

class ContainerDispenser(IContainer):
    CONTAINER_SLOTS = 8

    def __init__(self):
        IContainer.__init__(self)