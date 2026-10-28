import csv
import random
import time


def bubble_sort(a):
    a = a[:]
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = x
    return a


ALGORITHMS = {"bubble sort": bubble_sort,
              "insertion sort": insertion_sort,
              "sorted (Python)": sorted}

with open("assets/tp2_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "algorithm", "time"])
    for n in [250, 500, 1000, 1500, 2000, 2500]:
        data = [random.randint(0, 100000) for _ in range(n)]
        for name, function in ALGORITHMS.items():
            start = time.perf_counter()
            function(data)
            duration = time.perf_counter() - start
            writer.writerow([n, name, round(duration, 6)])

print("assets/tp2_results.csv created")