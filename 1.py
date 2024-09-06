import queue

# Creating a dictionary of opnening and their closing brackets
brackets_info = {
    ")": "(",
    "]": "[",
    "}": "{"
}

# Printing error messages because it looks great
def print_errors(string: str, position: int, text="Некорректная скобка!") -> None:
            print("Строка не существует!")
            print(string)
            print("^".rjust(position + 1))
            print(text)

# I remember, that in Python code in fucntions works a bit faster, but I don't remrember why
def check_brackets(brackets: str) -> None: 
    lifo = queue.LifoQueue()
    for position, bracket in enumerate(brackets):
        if bracket in brackets_info.values():
            lifo.put(bracket)
        elif bracket in brackets_info.keys():
            if (lifo.empty()) or (brackets_info[bracket] != lifo.get()):
                print_errors(brackets, position)
                break
        else:
            print_errors(brackets, position, text="Некорректный символ!")
            break
    else:
        if lifo.empty():
            print("Строка существует")
        else:
            print_errors(brackets, brackets.rfind(lifo.get()), text="Скобка не была закрыта!")
            

# Main code
brackets = input("Пожалуйста, введите строку: ")
check_brackets(brackets)