import heapq
import os
import random

def merge_files(output_file: str, temp_files: str) -> None:
    heap_array = []
    temp_files = [open(temp_file, 'r', encoding="utf-8") for temp_file in temp_files]
    with open(output_file, "w") as output:
        for i in range(len(temp_files)):
            element = temp_files[i].readline().strip()
            if element:
                heapq.heappush(heap_array, (int(element), i))

        counter = 0
        print(temp_files)
        while counter < len(temp_files):
            print(counter, len(temp_files), heap_array)
            root = heapq.heappop(heap_array)
            output.write(str(root[0]) + '\n')

            element = temp_files[root[1]].readline().strip()
            if element:
                heapq.heappush(heap_array, (int(element), root[1]))
            else:
                counter += 1

        for temp_file in temp_files:
            temp_file.close()

def create_initial_runs(input_file: str, run_size: int, temp_path) -> int:
    temp_files = []
    with open(input_file, 'r', encoding="utf-8") as input: 
        end_of_file = False
        temp_files_counter = 0
        
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        
        while True:
            data = []
            for _ in range(run_size):
                line = input.readline().strip()
                if not line:
                    end_of_file = True
                    break                    
                data.append(int(line))

            with open(temp_path + str(temp_files_counter) + '.txt', 'w', encoding="utf-8") as output:
                temp_files.append(temp_path + str(temp_files_counter) + '.txt')
                print(data, temp_path + str(temp_files_counter) + '.txt')
                output.write('\n'.join(str(i) for i in data))

            if end_of_file:
                break

            temp_files_counter += 1
    return temp_files


def sort_chunks(temp_files: str) -> None:
    for temp_file in temp_files:
        with open(temp_file, 'r', encoding="utf-8") as input, open(temp_file, 'w', encoding="utf-8") as output:
            chunk = list(map(int, input.read().splitlines()))
            chunk.sort()
            output.write('\n'.join(str(i) for i in chunk))

def sort(input_file: str, output_file: str, run_size: int, current_depth: int, temp_dir: str, run_size_change_function) -> None:
    print( "Depth: ", current_depth)
    temp_files = create_initial_runs(input_file, run_size_change_function(run_size, current_depth), temp_dir)
    if current_depth > 1:
        for index, deeper_input_file in enumerate(temp_files):
            sort(deeper_input_file, deeper_input_file, run_size, current_depth - 1, temp_dir + f'{index}/', run_size_change_function)    
    else:
        sort_chunks(temp_files)
    merge_files(output_file, temp_files)

def external_multiphase_sort_recursive(path: str, run_size: int, multiphase_depth=3, run_size_change_function=lambda r_size, m_depth: r_size ** m_depth) -> None:
    #run_size = 1000         # How many numbers will programm read in one run
    #multiphase_depth = 3    # Depth of recursion during run of algorythm. On each run run_size will be divided by temp_files_counter ()

    print(run_size, run_size_change_function(run_size, multiphase_depth))

    input_file = f"{path}/input.txt"
    output_file = f"{path}/output.txt"

    sort(input_file, output_file, run_size, multiphase_depth, path + "/Temp_files_recursive/", run_size_change_function)