# На вход подаётся математическое выражение. Элементы - числа. Операции - "+ - * /".
# Также есть скобочки. Окончанием выражения служит "=".
# Программа должна вывести результат выражения
# Пример ввода:
# 2+7*(3/9)-5=
# Замечание:
# Программа также должна делать "проверку на дурака":
# нет деления на 0, все скобки стоят верно (см лаб №1) и т.п.


def calculate(expression):
    if not is_balanced_parentheses(expression):
      raise ValueError("Неправильная постановка скобок.")

    expression = expression.replace(" ", "")
    expression = expression.replace("×", "*")
    expression = expression.replace("÷", "/")

    while "(" in expression:
      start = expression.rfind("(")
      end = expression.find(")", start)
      sub_expression = expression[start+1:end]
      result = calculate(sub_expression)
      expression = expression.replace(expression[start:end+1], str(result))

    # Если выражение без ()
    result = eval(expression)
    return result


def is_balanced_parentheses(expression):
    stack = []
    for char in expression:
      if char == '(':
        stack.append(char)
      elif char == ')':
        if not stack:
          return False
        stack.pop()
    return not stack


expression = input("Введите математическое выражение (заканчивающееся знаком '='): ")

# Проверка на наличие знака "="
if not expression.endswith("="):
    raise ValueError("Выражение должно заканчиваться знаком '='.")

# Вычисление выражения
try:
    result = calculate(expression[:-1])
    print(result)
except ValueError as e:
    print(e)
