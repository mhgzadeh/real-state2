from estate import Apartment, House, Store
from deal import Sell, Rent
from base import BaseClass


class ApartmentSell(BaseClass, Apartment, Sell):

    def show_detail(self):
        self.show_price()

    def house_price(self):
        return self.price_per_meter * self.area

    # Abstract Function for BaseClass, Apartment, Sell
    def baseclass_abstract_description(self):
        print(f'ID: {self.id}\tObject_list: {self.object_list}\t' +
              f'Manager: {self.manager}\n')

    def apartment_abstract_description(self):
        print(f'Floor: {self.floor}\tHas Elavator: {self.has_elavator}\t' +
              f'Has Parking: {self.has_parking}\n')

    def sell_abstract_description(self):
        print(f'Price Per Meter: {self.price_per_meter}\t' +
              f'Discountable: {self.discountable}\t' +
              f'Convertable: {self.convertable}\n')


class ApartmentRent(BaseClass, Apartment, Rent):
    pass


class HouseSell(House, Sell):
    pass


class HouseRent(House, Rent):
    pass


class StoreSell(Store, Sell):
    pass


class StoreRent(Store, Rent):
    pass
