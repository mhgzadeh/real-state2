from abc import ABC, abstractmethod
from manager import Manager


class BaseClass(ABC):
    _id = 0
    object_list = None
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.__generate_id()
        self.store = self.__store(self)
        self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def __generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)

    @classmethod
    def __store(cls, obj):
        if cls.object_list == None:
            cls.object_list = list()
        cls.object_list.append(obj)
        return cls.object_list

    @abstractmethod
    def baseclass_abstract_description(self):
        pass
