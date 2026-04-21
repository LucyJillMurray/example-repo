import math

numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]


# Linear Search
# This search works for small unordered lists
def linear_search(numbers, target):
    for x in range(len(numbers)):
        if numbers[x] == target:
            return x

    return -1


print(f"linear search: number 9 is at index: {linear_search(numbers, 9)}")


# Insertion sort
# Insertion sort is descending
def insertion_sort(numbers):
    sorted_list = []
    sorted_list.append(numbers[0])
    unsorted_list = numbers[1:]

    for num in unsorted_list:
        sorted_list.append(num)
        j = len(sorted_list) - 1

        while sorted_list[j] > sorted_list[j - 1] and j > 0:
            sorted_list[j], sorted_list[j - 1] = (
                sorted_list[j - 1],
                sorted_list[j],
            )
            j = j - 1

    return sorted_list


sorted = insertion_sort(numbers)
print("Insertion Sort")
print(*sorted)


"""
I chose the binary search algorithm.
This is a good use case as the list is already sorted.
It has complexity Olog(n)
This means it is fast, and doesn't need to iterate through the whole list.
"""

numbers.sort()
print("Sorted List")
print(*numbers)


def binary_search(numbers, target, left, right):
    middle = math.floor((left + right) / 2)
    if left > right:
        return -1
    elif numbers[middle] == target:
        return middle
    elif numbers[middle] < target:
        return binary_search(numbers, target, middle + 1, right)
    else:
        return binary_search(numbers, target, left, middle - 1)


number_index = binary_search(numbers, 9, 0, len(numbers) - 1)
print(f"binary search: 9 is at index: {number_index}")
