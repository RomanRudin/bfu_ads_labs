def check_brackets(brackets: str, ) -> bool: 
    import queue
    lifo = queue.LifoQueue()
    for position, bracket in enumerate(brackets):
        if bracket in "([{":
            lifo.put(bracket)
        elif bracket == ")":
            if (lifo.empty()) or (lifo.get() != "("):
                return False
        elif bracket == "]":
            if (lifo.empty()) or (lifo.get() != "("):
                return False
        elif bracket == "}":
            if (lifo.empty()) or (lifo.get() != "("):
                return False
        else:
            return False
    else:
        if lifo.empty():
            return True
        else:
            return False
            

# Main code
#brackets = input("Пожалуйста, введите строку: ")
#check_brackets(brackets, BRACKETS_INFO)