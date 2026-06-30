import random
import time
import pandas as pd
import numpy as np
import bubblesort
import mergeSortAlgo
import countingSort
import insertionSort
import quickSort

import matplotlib.pyplot as plt


def benchmarking(algorithms, sizes, runs):
    elapsed_times = []
    input_size = []
    trials = []
    sort_names = []

    for sort_algo in algorithms:
        print(f"running {sort_algo}")
        for size in sizes:
            for run in range(runs):
                x = [random.randint(0, 100) for i in range(size)]
                algorithm = algorithms[sort_algo]
                start_time = time.time()
                algorithm(x)
                end_time = time.time()
                time_elapsed = (end_time - start_time) * 1000
                elapsed_times.append(time_elapsed)
                trials.append(run + 1)
                input_size.append(size)
                sort_names.append(sort_algo)

    df = pd.DataFrame({
        "Sort": sort_names,
        "Size": input_size,
        "Times": elapsed_times,
        "trialNo": trials
    })
    return df


def mean_sorts(df):
    return df.groupby(['Sort', 'Size'])['Times'].mean().round(3).unstack()


def plot_averages(df2):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.rcParams["figure.figsize"] = (16, 8)
    sns.set(style="darkgrid")
    df2.T.plot(lw=2, colormap='jet', marker='.', markersize=10,
               title='Benchmarking sorting algorithms - average Times ')
    plt.ylabel("Running time (milliseconds)")
    plt.xlabel("Input Size")
    plt.savefig('plot100.png', bbox_inches='tight')


def export_results(times, means):
    times.to_csv('xxxAverages' + '100' + '.csv')


if __name__ == "__main__":
    algorithms = {
        "Bubblesort": bubblesort.bubbleSort,
        "insertionSort": insertionSort.insertionSort,
        "mergeSort": mergeSortAlgo.merge_sort,
        "quickSort": quickSort.quickSort,
        "CountingSort": countingSort.count_sort,
    }
    sizeN = [100, 250, 500, 750, 1000, 1250, 2500]

    results = benchmarking(algorithms, sizeN, 5)
    print("The running time for each of the 5 sorting algorithms have been measured 5 times and the averages for each algorithm and each input size are as follows \n")
    df2 = mean_sorts(results)
    print(df2)
    plot_averages(df2)
    export_results(results, df2)
