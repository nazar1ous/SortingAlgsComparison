def merge_sort(lst, cache=[0], depth=0):
    # If it is first recursion, comparison_n = 0
    # I do not consider comparison of depth, because it wasn't important in the algorithm
    if depth == 0:
        cache = [0]
    # Basics of recursion
    if len(lst) > 1:
        comparison_n = 0
        # Idea of divide and conquer
        mid = len(lst) // 2
        left, right = lst[:mid], lst[mid:]
        merge_sort(left, cache, 1)
        merge_sort(right, cache, 1)

        # idea of merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
                k += 1
            else:
                lst[k] = right[j]
                j += 1
                k += 1
            comparison_n += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        cache[0] += comparison_n
        return lst, cache[0]


if __name__ == "__main__":
    # Test whether idea with cache works
    lst1 = [2,3 ,5, -1, 20, 4]
    print(merge_sort(lst1)[1])
    lst2 = [1, 2]
    print(merge_sort(lst2)[1])