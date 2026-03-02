# Sorting Algorithm Visualiser

import matplotlib.pyplot as plt
import numpy as np

list_to_sort = [64, 34, 25, 12, 22, 11, 90, 23, 45, 67]

plt.style.use('_mpl-gallery')

# make data:
x = 0.5 + np.arange(10)
y = list_to_sort

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 10), xticks=np.arange(1, 10),
       ylim=(0, 10), yticks=np.arange(1, 10))

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
            # Iterating through array until the second to last index
            for i in range(len(self.arr)-1):
                # Swapping values if the current value is greater than the next value
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    arr_swapped = True
            if not arr_swapped:
                return self.arr
                

        
if user_choice == "1":
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    sorted_list = sorting_algorithm.bubble_sort()
    print("Sorted list:", sorted_list)
    
