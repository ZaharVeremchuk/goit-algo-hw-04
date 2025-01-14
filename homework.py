from timeit import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

print("Перевірка на не великому обєму дданих")
numbers = [5, 3, 8, 4, 2]
insert_sort_time = timeit(stmt='insertion_sort(lst=numbers)', globals=globals())

numbers = [5, 3, 8, 4, 2]
merge_sort_time = timeit(stmt='merge_sort(arr=numbers)', globals=globals())

numbers = [5, 3, 8, 4, 2]
python_sort_time = timeit(stmt='numbers.sort()', globals=globals())

print(f'insert_sort_time = {insert_sort_time}')
print(f'merge_sort_time = {merge_sort_time}')
print(f'numbers.sort = {python_sort_time}')


large_arr = [random.randint(1, 50) for _ in range(50)]

print("Перевірка на Великому обєму дданих")
insert_sort_time = timeit(stmt='insertion_sort(lst=large_arr)', globals=globals())

merge_sort_time = timeit(stmt='merge_sort(arr=large_arr)', globals=globals())

python_sort_time = timeit(stmt='large_arr.sort()', globals=globals())

print(f'insert_sort_time = {insert_sort_time}')
print(f'merge_sort_time = {merge_sort_time}')
print(f'large_arr.sort = {python_sort_time}')