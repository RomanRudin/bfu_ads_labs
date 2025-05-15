import os
import tempfile


def sort_chunk(chunk):
    return sorted(chunk)


def external_sort(input_file, block_size):
    sorted_files = []

    #Разделение входного файла на отсортированные блоки
    with open(input_file, 'r') as file:
        while True:
            chunk = []
            for _ in range(block_size):
                line = file.readline()
                if not line:
                    break
                chunk.append(int(line.strip()))

            if not chunk:
                break

            sorted_chunk = sort_chunk(chunk)

            temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
            for number in sorted_chunk:
                temp_file.write(f"{number}\n")
            temp_file.close()
            sorted_files.append(temp_file.name)

    #Слияние отсортированных блоков
    final_output_file = 'sorted_output.txt'
    with open(final_output_file, 'w') as output_file:
        file_handlers = [open(f, 'r') for f in sorted_files]
        import heapq
        min_heap = []
        for i, file_handler in enumerate(file_handlers):
            number = file_handler.readline()
            if number:
                heapq.heappush(min_heap, (int(number.strip()), i))
        while min_heap:
            smallest_number, file_index = heapq.heappop(min_heap)
            output_file.write(f"{smallest_number}\n")
            next_number = file_handlers[file_index].readline()
            if next_number:
                heapq.heappush(min_heap, (int(next_number.strip()), file_index))

    for fh in file_handlers:
        fh.close()
    for f in sorted_files:
        os.remove(f)

    print(f"Сортировка завершена. Отсортированные данные записаны в '{final_output_file}'.")


input_file = 'input.txt'
block_size = 1000  # Размер блока для сортировки


external_sort(input_file, block_size)
