from redstone.containers.IContainer import IContainer

class ContainerBrewingStand(IContainer):
    CONTAINER_SLOTS = 4

    def __init__(self):
        IContainer.__init__(self)