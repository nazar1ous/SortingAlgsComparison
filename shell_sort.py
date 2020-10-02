def shell_sort(lst):
    comparison_n = 0
    h = 1
    # Implement Shell's idea
    while h < len(lst) / 3:
        h = h * 3 + 1
    # Because of last if expression in while,
    # and consider last expression of while in the next one

    # continue until the gap=1 (basic insertion)
    while h >= 1:
        # find the gap
        for i in range(h, len(lst)):
            j = i
            # run insertion
            temp = lst[j]
            while j >= h and temp < lst[j - h]:
                comparison_n += 1
                lst[j] = lst[j - h]

                j -= h
            # If it is last/first end of while
            comparison_n += 1
            lst[j] = temp

        h = h // 3
    return lst, comparison_n
