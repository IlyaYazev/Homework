def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print(b, c)
    print(c)
    print()

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

list_ = [1, 'строка', True]
print_params(*list_)

list_2 = [1, 25, [1, 2, 3]]
print_params(*list_2)

values_list = ["абзац", False, 5]
values_dict = {'a': "Цифра", 'b': 90, 'c': "Правда"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["текст", 100]
print_params(*values_list_2, 42)











