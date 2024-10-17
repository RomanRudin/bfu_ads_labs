import heapq
import os

def merge_files(output_file: str, temp_files: list[str], path: str) -> None:
    heap_array = []
    temp_files = [open(temp_file, 'r', encoding="utf-8")  for temp_file in temp_files]
    with open(output_file, "w") as output:
        for i in range(len(temp_files)):
            element = temp_files[i].readline().strip()
            if element:
                heapq.heappush(heap_array, (int(element), i))

        counter = 0
        while counter < len(temp_files):
            root = heapq.heappop(heap_array)
            output.write(str(root[0]) + '\n')

            element = temp_files[root[1]].readline().strip()
            if element:
                heapq.heappush(heap_array, (int(element), root[1]))
            else:
                counter += 1

        for temp_file in temp_files:
            temp_file.close()

def create_initial_runs(input_file: str, run_size: str, path: str) -> list[str]:
    temp_files = []
    with open(input_file, 'r', encoding="utf-8") as input: 
        end_of_file = False
        temp_files_counter = 0
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        while True:
            data = []
            for _ in range(run_size):
                line = input.readline().strip()
                if not line:
                    end_of_file = True
                    break                    
                data.append(int(line))
            data.sort()

            with open(path + r'\f_' + str(temp_files_counter) + '.txt', 'w', encoding="utf-8") as output:
                temp_files.append(path + r'\f_' + str(temp_files_counter) + '.txt')
                output.write('\n'.join(str(i) for i in data))

            temp_files_counter += 1

            if end_of_file: break
    return temp_files


def external_multiphase_sort(path: str, run_size: int) -> None:
    #run_size - How many numbers will programm read in one run

    input_file = f"{path}/input.txt"
    output_file = f"{path}/output.txt"
    path += "\Temp_files_linear"

    temp_files = create_initial_runs(input_file, run_size, path)
    merge_files(output_file, temp_files, path)