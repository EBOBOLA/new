class House():
    def __init__(self, street, number):
        self.street = street
        self.number = number
    def build(self):
        print("дом на " + self.street + "номер" + self.number)
House1 = House("топ",20)
House2 = House("топ",21)
print(House2.number)