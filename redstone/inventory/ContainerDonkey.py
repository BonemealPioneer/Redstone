from redstone.containers.IContainer import IContainer

class ContainerDonkey(IContainer):
    CONTAINER_SLOTS = 16

    def __init__(self):
        IContainer.__init__(self)