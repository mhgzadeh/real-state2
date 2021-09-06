from abc import ABC, abstractmethod


class Sell(ABC):
    def __init__(self, price_per_meter, discountable=True,
                 convertable=True, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    @abstractmethod
    def sell_abstract_description(self):
        pass

    def show_price(self):
        print(f"price: {self.price_per_meter}\t discount: {self.discountable}\t" +
              f"convert: {self.convertable}\n")


class Rent(ABC):
    def __init__(self, initial_price, monthly_price,
                 convertable=True, discountable=True, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)

    @abstractmethod
    def rent_abstract_description(self):
        pass
