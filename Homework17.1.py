#1. Создайте новый класс House
#2. Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
#3. Создайте метод setNewNumberOfFloors(floors),
#который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors

class House: #1 класс
    def __init__(self): #магический метод, конструктор, дандер метод
        self.numberOfFloors = 10 #2 атрибут на уровне экземпляра класса, свойство

    def setNewNumberOfFloors(self, floors): #3 метод, (self, floors) - параметры функции/метода
         self.numberOfFloors = floors
         print(self.numberOfFloors)

home = House() # создаем экзэмпляр класса home
print(home.numberOfFloors)
home2 = House()
home.setNewNumberOfFloors(25)
print(home.numberOfFloors)
print(home2.numberOfFloors)