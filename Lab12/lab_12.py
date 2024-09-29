import heapq
import os
import random

TEMP_FILES_PATH = "Lab12/temp_files/"

def merge_files(output_file, temp_files_counter):
    heap_array = []
    temp_files = [open(TEMP_FILES_PATH + str(i) + '.txt', 'r', encoding="utf-8")  for i in range(temp_files_counter)]
    with open(output_file, "w") as output:
        for i in range(temp_files_counter):
            element = temp_files[i].readline().strip()
            if element:
                heapq.heappush(heap_array, (int(element), i))

        counter = 0
        while counter < temp_files_counter:
            root = heapq.heappop(heap_array)
            output.write(str(root[0]) + '\n')

            element = temp_files[root[1]].readline().strip()
            if element:
                heapq.heappush(heap_array, (int(element), root[1]))
            else:
                counter += 1

        for i in range(temp_files_counter):
            temp_files[i].close()

def create_initial_runs(input_file, run_size) -> int:
    with open(input_file, 'r', encoding="utf-8") as input: 
        end_of_file = False
        temp_files_counter = 0
        
        if not os.path.exists(TEMP_FILES_PATH):
            os.makedirs(TEMP_FILES_PATH)
        
        while True:
            data = []
            for _ in range(run_size):
                line = input.readline().strip()
                if not line:
                    end_of_file = True
                    break                    
                data.append(int(line))
            data.sort()

            if end_of_file:
                break

            with open(TEMP_FILES_PATH + str(temp_files_counter) + '.txt', 'w', encoding="utf-8") as output:
                print(TEMP_FILES_PATH + str(temp_files_counter) + '.txt')
                output.write('\n'.join(str(i) for i in data))

            temp_files_counter += 1
    return temp_files_counter


def sort(input_file, output_file, run_size):
    temp_files_counter = create_initial_runs(input_file, run_size)
    merge_files(output_file, temp_files_counter)


def external_multiphase_sort():
    num_ways = 10
    run_size = 1000

    input_file = "Lab12/Data/input.txt"
    output_file = "Lab12/Data/output.txt"

    # Instead of testing system right now i'm using this:
    with open(input_file, 'w') as f:
        for _ in range(num_ways * run_size):
            f.write(str(random.randint(0, 10000)) + '\n')

    sort(input_file, output_file, run_size)