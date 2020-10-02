def selection_sort(lst):
    comparison_n = 0
    # max([len-1..len-1] is (len-1)th elem
    for i in range(len(lst) - 1):
        min_elem = lst[i]
        min_id = i
        # Basically find max in [i+1..]
        for j in range(i + 1, len(lst)):
            if lst[j] < min_elem:
                min_elem = lst[j]
                min_id = j
            comparison_n += 1

        lst[i], lst[min_id] = lst[min_id], lst[i]

    return lst, comparison_n
