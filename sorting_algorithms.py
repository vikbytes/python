import math
import random
import copy
from timeit import default_timer as timer

# Bubble Sort algorithm implementation
# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(array):
    n = len(array)
    while(n > 1):
        new_n = 0
        for i in range(1, n):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                new_n = i
        n = new_n
    return array

# Insertion Sort algorithm implementation
# https://en.wikipedia.org/wiki/Insertion_sort
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while (j > 0) and (array[j-1] > array[j]):
            array[j-1], array[j] = array[j], array[j-1]
            j = j - 1
    return array

# Merge Sort algorithm implementation
# https://en.wikipedia.org/wiki/Merge_sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    left = []
    right = []
    for i in range(len(array)):
        if i < (len(array)/2):
            left.append(array[i])
        else:
            right.append(array[i])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while (len(left) != 0) and (len(right) != 0):
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1::]
        else:
            result.append(right[0])
            right = right[1::]
    while (len(left) != 0):
        result.append(left[0])
        left = left[1::]
    while (len(right) != 0):
        result.append(right[0])
        right = right[1::]
    return result

# Lomuto partition scheme Quick Sort algorithm implementation
# https://en.wikipedia.org/wiki/Quicksort
def quick_sort(array):
    return quick_sort_proto(array, 0, len(array) - 1)

def quick_sort_proto(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort_proto(array, low, p-1)
        quick_sort_proto(array, p + 1, high)
    return array

def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    temp = array[i]
    array[i] = array[high]
    array[high] = temp
    return i

# Selection sort algorithm implementation
# https://en.wikipedia.org/wiki/Selection_sort
def selection_sort(array):
    for i in range(len(array)-1):
        minimum = i
        for j in range(i+1, len(array)):
            if (array[j] < array[minimum]):
                minimum = j
        if minimum != i:
            array[i], array[minimum] = array[minimum], array[i]
    return array

# Heap Sort algorithm implementation
# https://en.wikipedia.org/wiki/Heapsort
def heap_sort(array):
    heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end = end - 1
        sift_down(array, 0, end)
    return array

def i_parent(i):
    return math.floor((i-1)/2)

def i_left_child(i):
    return 2*i + 1

def heapify(array, count):
    start = i_parent(count-1)
    while start >= 0:
        sift_down(array, start, count - 1)
        start = start - 1

def sift_down(array, start, end):
    root = start
    while i_left_child(root) <= end:
        child = i_left_child(root)
        swap = root
        if array[swap] < array[child]:
            swap = child
        if (child+1 <= end) and (array[swap] < array[child+1]):
            swap = child + 1
        if swap == root:
            return
        else:
            array[root], array[swap] = array[swap], array[root]
            root = swap

# Shell Sort algorithm implementation, with Marcin Cirua's gap sequence
# https://en.wikipedia.org/wiki/Shellsort
def shell_sort(array):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i
            while((j >= gap) and (array[j-gap] > temp)):
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
    return array

# Comb Sort algorithm implementation
# https://en.wikipedia.org/wiki/Comb_sort
def comb_sort(array):
    gap = len(array)
    shrink = 1.3
    sorted = False
    while(not sorted):
        gap = math.floor(gap/shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while (i+gap) < len(array):
            if array[i] > array[i+gap]:
                array[i], array[i+gap] = array[i+gap], array[i]
                sorted = False
            i = i + 1
    return array

# Generates an array with length size of random integers between 0 and 2**16
def generate_array(size):
    array = []
    for x in range(size):
        array.append(random.randint(0, 2**31))
    return array

# Manually maintained, add new entries for any newly implemented algorithm
algorithms = [bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort, heap_sort, shell_sort, comb_sort]

# Test function to run and verify all the algorithms
def test_suite(array, sorted_array):
    for x in algorithms:
        # Make a deep copy every time as to produce a new array copy, not just a shallow copy to the argument array
        # since we modify the array each time, this is necessary to have an unsorted array for each test
        temp = copy.deepcopy(array)
        start = timer()
        if x(temp) == sorted_array:
            end = timer()
            print(f"{x} PASSED the test, and took {end-start:1.4f}s to sort the array.")
        else:
            print(f"{x} FAILED the test.")

# Generate an array with random integers to be sorted.
new_array = generate_array(4096)
# Use the built-in 'sorted' method from Python standard library to sort the new array
# in order to have a sorted array to compare the implemented algorithms with.
start = timer()
new_sorted_array = sorted(new_array)
end = timer()
print(f"The built in sorted method took {end-start:1.4f}s to sort the array.")
# Test the algorithm implementations by running the test suite.
test_suite(new_array, new_sorted_array)