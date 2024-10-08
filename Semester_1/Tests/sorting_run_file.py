from Semester_1.Tests.sorting_tests import testing_sorting, testing_external_sorting
from ..Labs.Lab4.lab_4 import comb_sort
from ..Labs.Lab5.lab_5 import insertion_sort
from ..Labs.Lab6.lab_6 import selection_sort
from ..Labs.Lab7.lab_7 import shell_sort
from ..Labs.Lab8.lab_8 import radix_sort
from ..Labs.Lab9.lab_9 import heap_sort
from ..Labs.Lab10.lab_10 import merge_sort
from ..Labs.Lab11.lab_11 import quick_sort
from ..Labs.Lab12.lab_12 import external_multiphase_sort

print("\nComb sort:")
testing_sorting(comb_sort, max_len=10000, testing_amount=20)
print("\nInsertion sort:")
testing_sorting(insertion_sort, max_len=10000, testing_amount=20)
print("\nSelection sort:")
testing_sorting(selection_sort, max_len=10000, testing_amount=20)
print("\nShell sort:")
testing_sorting(shell_sort, max_len=10000, testing_amount=20)
print("\nRadix sort:")
testing_sorting(radix_sort, max_len=10000, testing_amount=20)
print("\nHeap sort:")
testing_sorting(heap_sort, max_len=10000, testing_amount=20) 
print("\nMerge sort:")
testing_sorting(merge_sort, max_len=10000, testing_amount=20)
print("\nQuick sort:")
testing_sorting(quick_sort, max_len=10000, testing_amount=20)
print("\nExternal multiphase sort:")
testing_external_sorting(external_multiphase_sort(), "../Labs/Lab12/Data", max_len=10000, testing_amount=20)