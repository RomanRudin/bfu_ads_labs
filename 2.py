#Using cide from previous lab we can check if user input is correct in sense of correct brackets:
from lab_1 import check_brackets

expression = input("Please, enter the expression: ").replace(" ", "")
if check_brackets(expression, {")":"("}, print_correctness=False, accept_num=True):
    pass
