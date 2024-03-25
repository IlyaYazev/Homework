def print_params(a, b, c):
    print (a, b, c)
    print (b, c)
    print(c)
    print()

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











