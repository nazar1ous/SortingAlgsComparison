import random as rd
from copy import deepcopy as dp
import sys
import time
from matplotlib import pyplot as plt
import pylab
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from merge_sort import merge_sort

sys.setrecursionlimit(3000)


def make_plot(data, experiment, name, by_comparisons_n=True):
    sorts = [selection_sort, insertion_sort, merge_sort, shell_sort]
    fig = plt.figure()

    ax = fig.add_subplot(2, 1, 1)
    ax.set_title(name, fontsize=18, fontweight='bold')
    for j in range(len(sorts)):
        # The statement denotes that we should start with power of 7
        exp_values = data[experiment][sorts[j].__name__]
        if by_comparisons_n:
            exp_data = [elem[0] for elem in exp_values]
        else:
            exp_data = [elem[1]*10**3 for elem in exp_values]

        line, = ax.plot(exp_data, lw=2, label=sorts[j].__name__)
    # change the x axes names
    labels = [item.get_text() for item in ax.get_xticklabels()]

    for i in range(len(labels)):
        labels[i] = '2^' + str(i+6)
    ax.set_xticklabels(labels)

    ax.legend(loc='upper left')
    ax.set_yscale('log')
    ax.set_xlabel('Elements number')
    if by_comparisons_n:
        ax.set_ylabel('Comparisons number')
    else:
        ax.set_ylabel('Time execution in ms')


    plt.grid()

    pylab.show()


def test_sort(sort, lst, times):
    exp_lst = dp(lst)
    total_time, comparisons = 0, 0
    for t in range(times):
        s = time.time()
        comparisons += sort(exp_lst)[1]
        total_time += time.time() - s
    return comparisons / times, total_time / times


def get_data_by_testing(sorts):
    dct_experiments_res = {}
    experiments = "abcd"
    for l in experiments:
        dct_experiments_res[l] = {}

    for power in range(7, 15):
        JNumber = 2 ** power
        main_lst = [rd.randint(1, 10**4) for i in range(JNumber)]
        in_order_lst = sorted(main_lst)
        disorder_lst = sorted(main_lst, key=lambda x: -x)
        set1 = [1, 2, 3]
        lst_from_set = [rd.choice(set1) for i in range(JNumber)]

        for sort in sorts:
            values_lst = []
            values_lst.append(test_sort(sort, main_lst, 5))
            values_lst.append(test_sort(sort, in_order_lst, 1))
            values_lst.append(test_sort(sort, disorder_lst, 1))
            values_lst.append(test_sort(sort, lst_from_set, 3))
            for i in range(len(values_lst)):
                exp = experiments[i]
                str_sort = sort.__name__
                if str_sort not in dct_experiments_res[exp]:
                    dct_experiments_res[exp][str_sort] = [values_lst[i]]
                else:
                    dct_experiments_res[exp][str_sort].append(values_lst[i])

    return dct_experiments_res


def main():
    s = time.time()
    sorts = [selection_sort, insertion_sort, merge_sort, shell_sort]
    data = get_data_by_testing(sorts)
    experiments = "abcd"
    exp_names = {}
    exp_names['a'] = "Random array"
    exp_names['b'] = "Sorted array in order"
    exp_names['c'] = "Sorted array in disorder"
    exp_names['d'] = "Array from a set {1, 2, 3}"
    for exp in experiments:
        name = exp_names[exp]

        make_plot(data, exp, name)
        make_plot(data, exp, name, False)

    print(time.time() - s)


if __name__ == "__main__":
    main()
