#1. Создайте новый класс House
#2. Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
#3. Создайте метод setNewNumberOfFloors(floors),
#который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors

class House: #1
    def __init__(self):
        self.numberOfFloors = 0 #2

    def setNewNumberOfFloors(self, floors): #3
         self.numberOfFloors = floors
         print(self.numberOfFloors)

New_build = House()
print(New_build.numberOfFloors)
