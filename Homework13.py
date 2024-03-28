def test(*args):
    print(*args)
test("I believe in miracles", 666, 'Пример')

def factorial (n):#Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n = n - 1)
    return  n * factorial_n_minus_1

print(factorial(50))


