def insertion_sort(lst):
    comparison_n = 0
    # [1..len] because first elem is already sorted
    for i in range(1, len(lst)):
        j = i - 1
        key = lst[i]
        # find the place for key
        while j >= 0 and lst[j] > key:
            comparison_n += 1
            lst[j + 1] = lst[j]
            j -= 1
        # because last/first comparison of while should
        # be counted too
        comparison_n += 1
        lst[j + 1] = key
    return lst, comparison_n
