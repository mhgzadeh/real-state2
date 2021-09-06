from abc import abstractmethod, ABC


class __EstateAstract(ABC):

    def __init__(self, user, area, rooms_count, built_year, region,
                 address, *args, **kwargs):
        self.user = user
        self.area = area
        self.rooms_count = rooms_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)


class Apartment(__EstateAstract):

    def __init__(self, floor, has_elavator=True, has_parking=True, *args, **kwargs):
        self.has_elavator = has_elavator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)

    @abstractmethod
    def apartment_abstract_description(self):
        pass


class House(__EstateAstract):

    def __init__(self, has_yard, floor_counts, *args, **kwargs):
        self.has_yard = has_yard
        self.floor_counts = floor_counts
        super().__init__(*args, **kwargs)

    @abstractmethod
    def house_abstract_description(self):
        pass


class Store(__EstateAstract):

    # print('Store {self.id}, Seller: {self.user.full_name}, Seller ID: {self.user.id}')
    # It has the Id error due to changing the parent of EstateAbstract to ABC instead of
    # BaseClass

    @abstractmethod
    def store_abstract_descriptions(self):
        pass
