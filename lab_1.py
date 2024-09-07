# Creating a dictionary of opnening and their closing brackets
brackets_info = {
    ")": "(",
    "]": "[",
    "}": "{"
}

# Printing error messages because it looks great
def printing_errors(string: str, position: int, text="Некорректная скобка!") -> None:
            print("Строка не существует!")
            print(string)
            print("^".rjust(position + 1))
            print(text)

# I remember, that in Python code in fucntions works a bit faster, but I don't remrember why
def check_brackets(brackets: str, brackets_info: dict, print_correctness=True, print_errors=True, accept_num=False, accept_alpha=False) -> bool: 
    import queue
    lifo = queue.LifoQueue()
    for position, bracket in enumerate(brackets):
        if bracket in brackets_info.values():
            lifo.put(bracket)
        elif bracket in brackets_info.keys():
            if (lifo.empty()) or (brackets_info[bracket] != lifo.get()):
                if print_errors: printing_errors(brackets, position)
                return False
        else:
            if (not accept_alpha) and ():
                if print_errors: printing_errors(brackets, position, text="Некорректный символ!")
                return False
            if (not accept_num) and ():
                if print_errors: printing_errors(brackets, position, text="Некорректный символ!")
                return False
    else:
        if lifo.empty():
            if print_correctness: print("Строка существует")
            return True
        else:
            if print_errors: printing_errors(brackets, brackets.rfind(lifo.get()), text="Скобка не была закрыта!")
            return False
            

# Main code
brackets = input("Пожалуйста, введите строку: ")
check_brackets(brackets, brackets_info)