#Using cide from previous lab we can check if user input is correct in sense of correct brackets:
from lab_1 import check_brackets
from queue import LifoQueue, Queue
PRIORITY = {
   "start": 0,
    "(": 1,
    ")": 1,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
}

def tokenize(expression: str) -> list[str]:
    expression.replace(" ", "")
    if not check_brackets(expression, {")":"("}, print_correctness=False, accept_num=True):
        raise SyntaxError("")
    for sym in PRIORITY.keys():
        expression = expression.replace(str(sym), f" {sym} ")
    return expression.split()

# Using reversed Polish notation (RPN) algorithm:
def evaluate(tokens: list[str]) -> float: 
  stack = LifoQueue()
  for token in tokens: 
    if token not in "+-*/": 
      stack.put(float(token)) 
    else: 
      right = stack.get() 
      left = stack.get() 
      if token == '+': 
        stack.put(left + right) 
      elif token == '-': 
        stack.put(left - right) 
      elif token == '*': 
        stack.put(left * right) 
      elif token == '/': 
        assert right != 0
        stack.put(left / right) 
  return stack.get() 

# Converts infix notation to RPN by known algorythm
def convert(tokens: list[str]) -> list[str]:
    result = []
    temporary_stack = ["start"]
    while len(tokens):
        if tokens[0].isnumeric():
            result.append(tokens.pop(0))
            continue

        stack_item: str = temporary_stack[len(temporary_stack) - 1]
        input_item: str = tokens[0]

        if stack_item == "(" and input_item == ")":
            tokens.pop(0)
            temporary_stack.pop()
        elif stack_item == "start" and input_item == ")":
            raise SyntaxError("Incorrect expression")
        elif stack_item == "(" and not len(tokens):
            raise SyntaxError("Incorrect expression")
        else:
            if input_item == "(":
                temporary_stack.append(tokens.pop(0))
            elif PRIORITY.get(stack_item) < PRIORITY.get(input_item):
                temporary_stack.append(tokens.pop(0))
            else:
                result.append(temporary_stack.pop())
    temporary_stack.pop(0)
    temporary_stack.reverse()
    result.extend(temporary_stack)
    return result

print(evaluate(convert(tokenize(input("Please, enter the expression: ")))))