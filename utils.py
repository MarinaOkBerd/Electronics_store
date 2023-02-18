class Item:
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        Item.all.append(self)

    def calculate_total_price(self):

        return self.price * self.count

    def apply_discount(self):
        self.price *= Item.pay_rate


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())



Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)



print(Item.all)