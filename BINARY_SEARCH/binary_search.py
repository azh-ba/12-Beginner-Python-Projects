import random
import time

def naive_search(search_list, target):
    for i in range(len(search_list)):
        if search_list[i] == target:
            return i
    return -1


def binary_search(search_list, target):
    # find mid value
    list_length = len(search_list)
    half_length = list_length // 2

    # base case: no value in the list
    if list_length < half_length:
        return -1

    # base case: mid value is the target
    if search_list[half_length] == target:
        return half_length
    elif search_list[half_length] > target:
        return binary_search(search_list[0:(half_length - 1)], target)
    else:
        return binary_search(search_list[(half_length + 1):list_length], target)
    

def run_random_list():
    length = 10000

    # generate a list of random values
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    print(sorted_list)

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
    list = [1, 2, 3, 6, 7, 9, 12, 59, 68, 72, 91, 101]
    target = 59
    print(binary_search(list, target))