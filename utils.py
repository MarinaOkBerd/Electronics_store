import csv


class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, count):
        self.__name = name
        self.price = price
        self.count = count
        Item.all.append(self)

    @property
    def name(self, name):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception("Название товара больше 10 символов.")
        else:
            self.__name = name

    def calculate_total_price(self):
        return self.price * self.count

    def apply_discount(self):
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        items = []
        with open("items.csv", "r", encoding='windows-1251') as f:
            reader = csv.DictReader(f)

            for i in reader:
                items.append(cls(i['name'], int(i['price']), int(i['quantity'])))
        return items

    @staticmethod
    def is_integer(number):
        return((type(number) == int) or (type(number) == float)) and (round(number) == number)

    def __repr__(self):
        return f"Item({self.__name}, {self.price}, {self.count}"

    def __str__(self):
        return f"{self.__name}"


class Phone(Item):
    def __init__(self, name, price, count, number_of_sim):
        super().__init__(name, price, count)
        self.number_of_sim = number_of_sim

    @staticmethod
    def test_number_of_sim(self):
        if self.number_of_sim < 0 and type(self.number_of_sim) == int:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            return self.number_of_sim

    def __add__(self, other):
        if isinstance(other, Item):
            return self.number_of_sim + other.count
        else:
            ValueError("Возможно сложение только объектов Item и Phone")


phone1 = Phone("iPhone 14", 120_000, 5, 2)
print(phone1)
#iPhone 14
print(repr(phone1))
#Phone('iPhone 14', 120000, 5, 2)
phone1.number_of_sim = 0
#ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.