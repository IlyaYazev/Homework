def test():
    a = 100
    b = 200
    print(a, b)
test()

def test2 (a = "I learn", b = "Python", c = "Three weeks"):    #I learn, Python, Three weeks
    print(a, b, c)
test2()

def test3 (Имя, возраст):
    print(f"Имя: {Имя}")
    print(f"Возраст: {возраст}")
test3("Петр", 40)

def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
        print(f"sum = {result}")

sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
