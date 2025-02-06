# selection sort

def selection_sort(data_list):
    for i in range(len(data_list)-1):
        min_index = i
        for j in range(i+1, len(data_list)):
            if data_list[j] < data_list[min_index]:
                min_index = j
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]


l1 = [64, 25, 12, 22, 11]

selection_sort(l1)
print(l1)

1. Selection Sort
How It Works:

    The idea behind Selection Sort is to divide the list into two parts:
        Sorted part: Initially empty.
        Unsorted part: Initially, the entire list.
    Steps:
        Find the minimum element from the unsorted part.
        Swap it with the first unsorted element (beginning of the unsorted part).
        Move the boundary of the sorted part one element to the right and repeat the process.

Time Complexity:

    Best: O(n²)
    Average: O(n²)
    Worst: O(n²)
