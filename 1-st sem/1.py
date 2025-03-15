# На вход подаётся строка, состоящая из скобок.
# Программа должна определить правильность введённого скобочного выражения.
# Программа должна работать на русском языке: "Введите строку",
# "Строка не существует", "Строка существует" и т.п.
# Пример входа:
# ()[({}())]

def is_valid_expression(s):
    valid_brackets = set('()[]{}')

    if not all(char in valid_brackets for char in s):
        return False, False

    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in brackets.values():  # Если это открывающая скобка
            stack.append(char)
        elif char in brackets.keys():  # Если это закрывающая скобка
            if not stack or stack.pop() != brackets[char]:
                return True, False  # Строка существует, но не правильна
    return not stack, True  # Если стек пуст, значит скобки правильны


input_string = input("Введите строку: ")
if input_string:
    is_valid, is_only_brackets = is_valid_expression(input_string)
    if is_only_brackets:
        if is_valid:
            print("Строка существует и правильна.")
        else:
            print("Строка существует, но неверна.")
    else:
        print("Строка существует, но содержит неверные символы.")
else:
    print("Строка не существует.")
