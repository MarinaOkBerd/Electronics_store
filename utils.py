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



#item1 = Item("Смартфон", 10000, 20)
#item2 = Item("Ноутбук", 20000, 5)
#print(item1.calculate_total_price())
#print(item2.apply_discount())
#Item.pay_rate = 0.8
print(Item.instantiate_from_csv())
