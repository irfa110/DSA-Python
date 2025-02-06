# Bubble Sort

# def bubble_sort(list):
#     for i in range(len(list)):
#         for j in range(0, len(list)-1-i):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]

def bubble_sort(list):
    for i in range(1, len(list)):
        for j in range(len(list)-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


values = [2, 5, 7, 4, 9, 8, 1]

bubble_sort(values)
print("Sorted valuses is ", values)


# modified bubble sort

def modified_bubble_sort(list):
    # flage = False
    for i in range(len(list)):
        flage = False
        for j in range(0, len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                flage = True
        if not flage:
            break


values = [2, 5, 7, 4, 9, 8, 1]

modified_bubble_sort(values)
print("Sorted valuses is ", values)



How It Works:

    Bubble Sort compares adjacent elements in the list and swaps them if they are in the wrong order.
    Steps:
        Start at the beginning of the array.
        Compare each pair of adjacent elements.
        If the pair is in the wrong order, swap them.
        After one full pass, the largest element is placed at the end.
        Repeat the process for the remaining unsorted part until no swaps are needed.

Time Complexity:

    Best: O(n) (when the list is already sorted)
    Average: O(n²)
    Worst: O(n²)

Space Complexity:

    O(1) (in-place sorting)
