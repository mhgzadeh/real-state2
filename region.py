from base import BaseClass


class RegionClass(BaseClass):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    def baseclass_abstract_description(self):
        print(f'ID: {self.id}\tObject_list: {self.object_list}\tManager: {self.manager}')
        