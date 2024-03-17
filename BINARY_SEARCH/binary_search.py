import random
import time

def naive_search(search_list, target):
    """Search through the entire list."""
    for i in range(len(search_list)):
        if search_list[i] == target:
            return i
    return -1


def binary_search(search_list, target, low = None, high = None):
    """Compare the mid value of the list to the target. If not, compare it to the target.
    mid < target: recurse the function with the upper list (from mid value to last value of the list).
    mid > target: recurse the function with the lower list (from first value to mid value of the list)."""
    # find mid value
    if low is None:
        low = 0
    if high is None:
        high = len(search_list) - 1

    # base case: no value in the list
    if high < low:
        return -1
    
    mid = (low + high) // 2

    # base case: mid value is the target
    if search_list[mid] == target:
        return mid
    elif search_list[mid] > target:
        return binary_search(search_list, target, low, mid - 1)
    else:
        return binary_search(search_list, target, mid + 1, high)
    

def run_example_list():
    """Example list."""
    list = [1, 2, 3, 6, 7, 9, 12, 59, 68, 72, 91, 101]
    target = 59
    print(binary_search(list, target))


def run_random_list():
    """Run both of the search methods with a sorted randomly-generated list."""
    length = 10000

    # generate a sorted list of random values
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # naive search time
    start = time.time()
    for target in sorted_list:
        naive_search(list(sorted_list), target)
    stop = time.time()
    print(f"Naive search: {(stop - start)/length} seconds")

    # binary search time
    start = time.time()
    for target in sorted_list:
        binary_search(list(sorted_list), target)
    stop = time.time()
    print(f"Binary search: {(stop - start)/length} seconds")


if __name__ == '__main__':
    run_random_list()