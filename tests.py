from time import time
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

PREMADE_TESTS = [
    [i for i in range(100)],
    [i for i in range(100, 0, -1)],
    [1 for _ in range(100)],
]
MAX_STRING_LEN = 20

# Simple timer decorator
def timer(func) -> callable:
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

# Automatic tester for sorting algorythms
def testing_sorting(function: callable, show_results=True, testing_amount=10000, max_len=100, min_max_elem=100) -> bool:
    if show_results:
        print(bcolors.OKBLUE + "Testing sorting algorythms..." + bcolors.ENDC)
    time_stamps = []
    for test in PREMADE_TESTS:
        expected_result = sorted(test)
        start_time = time()
        result = function(test)
        end_time = time()
        time_stamps.append(end_time - start_time)
        if result != expected_result:
            if show_results:
                print(bcolors.FAIL + 'Test failed!' + bcolors.ENDC)
                if len(str(expected_result) + str(result)) <= MAX_STRING_LEN:
                    print(bcolors.FAIL + f'Expected {expected_result} but got {result}!' + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + 'Check test_logs.txt for more info' + bcolors.ENDC)
                    with open('test_logs.txt', 'w') as file:
                        file.write(f'Expected \n{expected_result}\n but got \n{result}')
            return False
    if show_results:
        print(bcolors.OKGREEN + "Premade tests passed!" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Running random tests!" + bcolors.ENDC)
    for _ in range(testing_amount):
        test = [randint(-min_max_elem, min_max_elem) for _ in range(randint(2, max_len))]
        expected_result = sorted(test)
        start_time = time()
        result = function(test)
        end_time = time()
        time_stamps.append(end_time - start_time)
        if result != expected_result:
            if show_results:
                print(bcolors.FAIL + 'Test failed!' + bcolors.ENDC)
                if len(str(expected_result) + str(result)) <= MAX_STRING_LEN:
                    print(bcolors.FAIL + f'Expected {expected_result} but got {result}!' + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + 'Check test_logs.txt for more info' + bcolors.ENDC)
                    with open('test_logs.txt', 'w') as file:
                        file.write(f'Expected \n{expected_result}\n but got \n{result}')
            return False
    if show_results:
        print(bcolors.OKGREEN + "Tests passed!" + bcolors.ENDC)
        print(bcolors.OKBLUE + f"Average time: {sum(time_stamps) / len(time_stamps)} seconds" + bcolors.ENDC)
    return True