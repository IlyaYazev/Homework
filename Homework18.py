#Создайте новый класс Buiding
#Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
#Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
#Полученный код напишите в ответ к домашему заданию

class Building:

    def __init__(self, numberOfFlors, buildingType):
        self.numberOfFlors = numberOfFlors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFlors == other.numberOfFlors and self.buildingType == other.buildingType

dom = Building(numberOfFlors=10, buildingType= "панельный")
dom2 = Building(numberOfFlors=5, buildingType="кирпичный")
dom3 = Building(numberOfFlors=10, buildingType="панельный")

print(dom3 == dom2)
print(dom == dom3)


