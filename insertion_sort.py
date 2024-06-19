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
