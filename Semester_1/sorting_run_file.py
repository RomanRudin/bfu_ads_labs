from Tests.sorting_tests import testing_sorting, testing_external_sorting
from Labs.Lab4.comb_sort import comb_sort
from Labs.Lab5.insertion_sort import insertion_sort
from Labs.Lab6.selection_sort import selection_sort
from Labs.Lab7.shell_sort import shell_sort
from Labs.Lab8.radix_sort import radix_sort
from Labs.Lab9.heap_sort import heap_sort
from Labs.Lab10.merge_sort import merge_sort
from Labs.Lab11.quick_sort import quick_sort
from Labs.Lab12.external_multiphase_sort_recursive import external_multiphase_sort_recursive
from Labs.Lab12.external_multiphase_sort_ import external_multiphase_sort_linear

if __name__ == "__main__":
    # print("\nComb sort:")
    # testing_sorting(comb_sort, max_len=10000, testing_amount=20)
    # print("\nInsertion sort:")
    # testing_sorting(insertion_sort, max_len=10000, testing_amount=20)
    # print("\nSelection sort:")
    # testing_sorting(selection_sort, max_len=10000, testing_amount=20)
    # print("\nShell sort:")
    # testing_sorting(shell_sort, max_len=10000, testing_amount=20)
    # print("\nRadix sort:")
    # testing_sorting(radix_sort, max_len=100000, min_max_elem=100000, testing_amount=20)
    # print("\nHeap sort:")
    # testing_sorting(heap_sort, max_len=10000, testing_amount=20) 
    # print("\nMerge sort:")
    # testing_sorting(merge_sort, max_len=100000, min_max_elem=100000, testing_amount=20)
    # print("\nQuick sort:")
    # testing_sorting(quick_sort, max_len=10000, testing_amount=20)
    # print("\nExternal multiphase sort recursive:")
    # testing_external_sorting(external_multiphase_sort_recursive, r"\Labs\Lab12\Data", max_len=10000, min_max_elem=100000, testing_amount=200, clean_files=False, run_size=1000, multiphase_depth=2)
    print("\nExternal multiphase sort:")
    testing_external_sorting(external_multiphase_sort_linear, r"\Labs\Lab12\Data", max_len=100_000, min_max_elem=100000, testing_amount=20, clean_files=False, run_size=1000)
