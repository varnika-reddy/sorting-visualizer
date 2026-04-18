import matplotlib.pyplot as plt
import random
import time

# generate random list
data = [random.randint(10, 100) for _ in range(20)]

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data)
                time.sleep(0.2)

def draw(data):
    plt.clf()
    plt.bar(range(len(data)), data)
    plt.title("Sorting Visualizer - Bubble Sort")
    plt.pause(0.01)

plt.ion()
draw(data)

bubble_sort(data)

plt.ioff()
plt.show()
