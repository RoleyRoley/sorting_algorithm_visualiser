# Sorting Algorithm Visualiser

import matplotlib.pyplot as plt
import numpy as np

list_to_sort = [64, 34, 25, 12, 22, 11, 90, 23, 45, 67]

plt.style.use('_mpl-gallery')

# function to show the graph of the sorted list

def show_graph(data):
    # make data
    x = np.arange(len(data))
    y = data

    # plot
    fig, ax = plt.subplots()

    # bar style
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    # set x-ticks labels
    x_labels = data

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)

    plt.show()



print("Which sortingalgorithm do you want to use?")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Selection Sort")
print("4. Merge Sort")
print("5. Quick Sort")

user_choice = input("Enter the number corresponding to your choice: ")

class SortingAlgorithm:
    def __init__(self, arr):
        self.arr = list_to_sort
    
    def bubble_sort(self):
        n = len(self.arr)
        while True:
            arr_swapped = False
            # iterating through array until the second to last index
            for i in range(len(self.arr)-1):
                # swapping values if the current value is greater than the next value
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    arr_swapped = True   
            if not arr_swapped:
                return self.arr
            

        
if user_choice == "1":
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    sorted_list = sorting_algorithm.bubble_sort()
    print("Sorted list:", sorted_list)
    show_graph(sorted_list)
   
    
