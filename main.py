from sample import create_samples
from advertisment import ApartmentRent, ApartmentSell


class Handler:

    ADVERTISMENT_TYPES = {
        1: ApartmentSell
    }

    SWITCHES = {
        'r': 'get_report',
        's': 'show_all'
    }

    def get_report(self):
        for adv in self.ADVERTISMENT_TYPES.values():
            print(adv, adv.manager.count())

    def show_all(self):
        for adv in self.ADVERTISMENT_TYPES.values():
            for obj in adv.object_list:
                print(obj.show_detail)

    def run(self):
        print('Hello Worlddd!!!!')
        for key in self.SWITCHES:
            print(f"Press {key} for {self.SWITCHES[key]}.")
        user_input = input('Enter your choice: ')
        switch = self.SWITCHES.get(user_input, None)
        if switch is None:
            print('Invalid Input.')
            self.run()
        choice = getattr(self, switch, None)
        choice()
        self.run()


if __name__ == '__main__':
    create_samples()

    handler = Handler()
    handler.run()
