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

MAX_STRING_LEN: int = 50

def test(function: callable, one_arg=False, show_results=True, *tests_data) -> bool:
    if show_results:
        print(bcolors.OKBLUE + f'Testing {function.__name__} algorythm...' + bcolors.ENDC)
    for test_data in tests_data:
        input, expected_result = test_data["input"], test_data["expected_result"]
        if one_arg:
            result = function(input[0])
        else:
            result = function(*input)
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
    # for _ in range(testing_amount):
    #     test = [randint(-min_max_elem, min_max_elem) for _ in range(randint(2, max_len))]
    #     expected_result = sorted(test)
    #     start_time = time()
    #     result = function(test)
    #     end_time = time()
    #     time_stamps.append(end_time - start_time)
    #     if result != expected_result:
    #         if show_results:
    #             print(bcolors.FAIL + 'Test failed!' + bcolors.ENDC)
    #             if len(str(expected_result) + str(result)) <= MAX_STRING_LEN:
    #                 print(bcolors.FAIL + f'Expected {expected_result} but got {result}!' + bcolors.ENDC)
    #             else:
    #                 print(bcolors.FAIL + 'Check test_logs.txt for more info' + bcolors.ENDC)
    #                 with open('test_logs.txt', 'w') as file:
    #                     file.write(f'Expected \n{expected_result}\n but got \n{result}')
    #         return False
    if show_results:
        print(bcolors.OKGREEN + "Tests passed!" + bcolors.ENDC)
    return True




from Labs.Lab7.the_largest_subarray import *

def test_the_largest_subarray() -> bool:
    tests = [{
            "input": [[-1, 3, -2, 5, 3, -5, 2, 2]],
            "expected_result": [[3, -2, 5, 3], 9]
        }, {
            "input": [{-10, -20, -30, -40, -50, -60}],
            "expected_result": [[-10], -10]
        }]
    return test(the_largest_subarray, *tests)
    


from Labs.Lab8.coin_exchange import *

def test_coin_exchange() -> bool:
    tests = [{
            "input": (),
            "expected_result": ()
        }, {
            "input": (),
            "expected_result": ()
        }]
    return test(coin_exchange, *tests)



from Labs.Lab9.travelling_salesman import *

def test_travelling_salesman() -> bool:
    tests = [{
            "input": (),
            "expected_result": ()
        }, {
            "input": (),
            "expected_result": ()
        }]
    return test(travelling_salesman, *tests)



from Labs.Lab10.egg_drop import *

def test_egg_drop() -> bool:
    tests = [{
            "input": (),
            "expected_result": ()
        }, {
            "input": (),
            "expected_result": ()
        }]
    return test(egg_drop, *tests)