from redstone.containers.IContainer import IContainer

class ContainerHopper(IContainer):
    CONTAINER_SLOTS = 4

    def __init__(self):
        IContainer.__init__(self)