# insertion sort
def insertion_sort(list):
    n = len(list)
    if n <= 1:
        return list
    for i in range(1, n):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key


list = [1, 5, 8, 7, 6, 4, 9, 3, 2, 10]
insertion_sort(list)
print(list)



a = [13,46,24,52,20,9]

n = len(a)
for i in range(n):
    j = i
    while j > 0 and a[j - 1] > a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        j -= 1
print(a)


How It Works:

    Insertion Sort works similarly to how you would sort playing cards in your hands:
        Take each element and insert it into the sorted portion of the list.
    Steps:
        Start with the second element (index 1).
        Compare it with the elements before it.
        Insert it in the correct position within the sorted portion.
        Repeat this process for every element until the list is sorted.

Time Complexity:

    Best: O(n) (when the list is already sorted)
    Average: O(n²)
    Worst: O(n²)

Space Complexity:

    O(1) (in-place sorting)
