from tests import testing_sorting
from Lab4.lab_4 import comb_sort
from Lab5.lab_5 import insertion_sort
from Lab6.lab_6 import selection_sort
from Lab7.lab_7 import shell_sort
from Lab8.lab_8 import radix_sort
# from Lab9.lab_9 import heap_sort
from Lab10.lab_10 import merge_sort
from Lab11.lab_11 import quick_sort
from Lab12.lab_12 import external_merge_sort

testing_sorting(comb_sort, max_len=10000, testing_amount=20)
# testing_sorting(insertion_sort, max_len=10000, testing_amount=20)
# testing_sorting(selection_sort, max_len=10000, testing_amount=20)
testing_sorting(shell_sort, max_len=10000, testing_amount=20)
testing_sorting(radix_sort, max_len=10000, testing_amount=20)
# testing_sorting(heap_sort, max_len=10000, testing_amount=20)
testing_sorting(merge_sort, max_len=10000, testing_amount=20)
testing_sorting(quick_sort, max_len=10000, testing_amount=20)
# testing_sorting(external_merge_sort, max_len=1-000, testing_amount=20)


# from Lab2.lab_2 import *
# print(evaluate(convert(tokenize(input("Please, enter the equasion: ")))))