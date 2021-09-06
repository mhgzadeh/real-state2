from random import choice
from user import User
from region import RegionClass
from advertisment import ApartmentSell, ApartmentRent
from manager import Manager


FIRST_NAME = ['Mohammad', 'ALi', 'Amin', 'Farahnaz']
LAST_NAME = ['Mohammadi', 'Alavi', 'Amini', 'Farahnazi']
MOBILES = ['09124636466', '09123456789',
           '09397645678', '09123423234', '09025645781']


def create_samples():
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    r1 = RegionClass('Stuttgart')
    r2 = RegionClass('Veihingen')
    r3 = RegionClass('Veihingen2')
    r4 = RegionClass('Veihingen3')

    ap_sell = ApartmentSell(floor=10, user=User.object_list[2], rooms_count=5, area=500,
                            built_year=2009, region=r1, address='In Der Au 16B',
                            price_per_meter=20)
    # User error occurs due to the object_list = None in base.py

    ap_sell2 = ApartmentSell(floor=5, user=User.object_list[1], rooms_count=3, area=100,
                             built_year=1999, region=r4, address='In Der Au 10B',
                             price_per_meter=105.5)

    ap_sell3 = ApartmentSell(floor=4, user=User.object_list[2], rooms_count=2, area=86.98,
                             built_year=2010, region=r2, address='In Der Au 11B',
                             price_per_meter=125)

    ap_sell4 = ApartmentSell(floor=1, user=User.object_list[4], rooms_count=3, area=205.24,
                             built_year=2020, region=r2, address='In Der Au 5B',
                             price_per_meter=286)
    ap_sell5 = ApartmentSell(floor=3, user=User.object_list[3], rooms_count=1, area=95.24,
                             built_year=2015, region=r3, address='In Der Au 16B',
                             price_per_meter=96)

    print('#'*20, '\tSample Created\t', '#'*20)
