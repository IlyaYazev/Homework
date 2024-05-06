class Building:

    def init(self, x, y):
        self.numberOfFlors = x
        self.buildingType = y

    def eq(self, other):
        return self.numberOfFlors == other.numberOfFlors and self.buildingType == other.buildingType

Hrushevka = Building()
Leningradka = Building()

if Hrushevka == Leningradka:
    print('Дома одинаковые')
else:
    print('Дома разные')