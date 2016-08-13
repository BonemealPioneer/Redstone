from abc import ABCMeta, abstractmethod

class ObjectListRegistry(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.object_registry = []
    
    def register_object(self, obj):
        if obj not in self.object_registry:
            self.object_registry.append(obj)

    def unregister_object(self, obj):
        if obj in self.object_registry:
            self.object_registry.remove(obj)