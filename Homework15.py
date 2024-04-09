def test_function(): # Создайте новую функцию def test_function
    def inner_function(): # Создайте другую функцию внутри функции inner_function
        print("Я в области видимости функции test_function") #функция должна печатать значение "Я в области видимости функции test_function"
    inner_function() # Вызовите функцию inner_function внутри функции test_function

test_function()
#если вызываем inner_funсtion() то NameError: name 'inner_funtion' is not defined

