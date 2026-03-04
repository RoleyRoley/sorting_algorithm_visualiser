# Sorting Algorithm Visualiser

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import time

# list_to_sort = [64, 34, 25, 12, 22, 11, 90, 23, 45, 67, 89, 34, 56, 78, 12, 34, 56, 78, 90, 23, 45, 67, 89, 34, 56, 78, 12, 34, 56, 78, 90, 23, 45, 67, 89]
list_to_sort = np.random.randint(1, 100, size=100).tolist()

plt.style.use('_mpl-gallery')

# Global variable to hold the animation reference
_ANIM_REF = None

visual_speed = 10

# Function to show the graph of the sorted list

def visualise_sort(data, steps_func, interval=visual_speed, title="Sorting Algorithm Visualisation"):
    global _ANIM_REF
    n = len(data)
    # Colors for bars
    base_color = "blue"
    highlight_color = "red"
    # Plot
    fig_width = min(16, max(8, n * 0.12))
    fig, ax = plt.subplots(figsize=(fig_width, 6))
    # Create bars for the initial data
    bars = ax.bar(range(n), data, width=1.0, color=base_color, edgecolor="none", linewidth=0)
    ax.set_xlim(-0.5, n - 0.5)
    ax.margins(x=0)
    ax.set_ylim(0, max(data) * 1.1)
    ax.set_xticks([])
    
    # Set title and info text
    title_text = ax.set_title(title)
    info_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    steps = steps_func(data)

    def update(frame):
        arr, active, swaps, elapsed = frame

        # Update bar heights
        for bar, h in zip(bars, arr):
            bar.set_height(h)
            bar.set_color(base_color)
            bar.set_alpha(0.7)

        # Highlight active bars
        if active is not None:
            for idx in active:
                # Highlight the bars being compared/swapped
                bars[idx].set_color(highlight_color)
                bars[idx].set_alpha(1.0)

        # Update text
        if elapsed is None:
            info_text.set_text(f"Swaps: {swaps}")
        else:
            info_text.set_text(f"Swaps: {swaps} | Time: {elapsed:.6f}s")

        return bars

    anim = FuncAnimation(
        fig,
        update,
        frames=steps,
        interval=interval,
        repeat=False,
        cache_frame_data=False,
    )
    _ANIM_REF = anim
    plt.show()



print("\nWhich sorting algorithm do you want to use?\n")
print(f"Number of elements to sort: {len(list_to_sort)}\n")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Selection Sort")
print("4. Merge Sort")
print("5. Quick Sort")



user_choice = input("Enter the number corresponding to your choice: ")

class SortingAlgorithm:
    def __init__(self, arr):
        self.arr = arr
    
    def bubble_sort(self, data):
        # Start timer
        start_time = time.perf_counter()
        # Create a copy of the original array to sort
        a = data[:]
        
        swap_counter = 0
        
        while True:
            
            arr_swapped = False
            # Iterating through array until the second to last index
            for i in range(len(a) - 1):
                # Yielding the current state of the array, the indices being compared, the swap count, and None for elapsed time
                yield a, (i, i + 1), swap_counter, None
                # Swapping values if the current value is greater than the next value
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    arr_swapped = True
                    swap_counter += 1
                    yield a, (i, i + 1), swap_counter, None
                    
            
            if not arr_swapped:
                # End timer
                end_time = time.perf_counter()
                # Yield the final state of the array, None for active indices, the total swap count, and the elapsed time
                yield a, None, swap_counter, (end_time - start_time)
                
                # print(f"Total swaps: {swap_counter}")
                # print(f"Bubble Sort took {end_time - start_time:.6f} seconds")
                return 
            
    def insertion_sort(self, data):
        start_time = time.perf_counter()
        # Create copy of original array
        a = data[:]
            
        swap_counter = 0
        
        # Iterating through array starting from the second element
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            # j is the index of the last element in the sorted portion of the array. We compare it with the key and shift elements to the right until we find the correct position for the key.
            while j >= 0 and a[j] > key:
                yield a, (j, j + 1), swap_counter, None
                a[j + 1] = a[j]
                swap_counter += 1
                yield a, (j, j + 1), swap_counter, None
                # Shift the index to the left
                j -= 1
            # Place the key in its correct position
            a[j + 1] = key
            yield a, (j + 1, i), swap_counter, None

        # End timer
        end_time = time.perf_counter()
        # Yield the final state of the array, None for active indices, the total swap count, and the elapsed time
        yield a, None, swap_counter, (end_time - start_time)
        
        # print(f"Total swaps: {swap_counter}")
        # print(f"Insertion Sort took {end_time - start_time:.6f} seconds")
        return
    
    def selection_sort(self, data):
        start_time = time.perf_counter()
        # Create copy of original array
        a = data[:]
        swap_counter = 0
        
        
        # Iternating through the array
        for i in range(len(a) - 1):
            min_idx = i
            # for each index after the starting index, we compare it with the current minimum index and update the minimum index if we find a smaller value. 
            for j in range(i + 1, len(a)):
                yield a, (min_idx, j), swap_counter, None
                # If index after starting index is less than starting index value, update minimum index
                if a[j] < a[min_idx]:
                    min_idx = j
            
            # if min_idx is not the same as the starting index, swap the values and update the swap counter
            if min_idx != i:
                a[i], a[min_idx] = a[min_idx], a[i]
                swap_counter += 1
                yield a, (i, min_idx), swap_counter, None
                    
       
        end_time = time.perf_counter()
        # Yield the final state of the array, None for active indices, the total swap count, and the elapsed time
        yield a, None, swap_counter, (end_time - start_time)
        return
        
                
    def merge_sort(self, data):
        start_time = time.perf_counter()
        # Create copy of original array
        a = data[:]
        swap_counter = 0
        
        if len(a) <= 1:
            return a
        
        if len(a) > 1:
            # Split array into 2 halves.
            midpoint = int(len(a) / 2)
            lefthalf = a[0 : midpoint]
            righthalf = a[midpoint :]
            
            
            
            sorted_left = self.merge_sort(lefthalf)
            sorted_right = self.merge_sort(righthalf)
            
            i = 0
            j = 0
            k = 0
            
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    a[k] = lefthalf[i]
                    i = i + 1
                else:
                    a[k] = righthalf[j]
                    j = j + 1
                k = k + 1
                    
            if lefthalf > righthalf:
                merged_list = sorted_left + sorted_right
                a = merged_list 
            else:
                merged_list = sorted_right + sorted_left
                a = merged_list
            return 
            
            
            
            
# Handling user choice.
        
if user_choice == "1":
    
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    visualise_sort(list_to_sort, sorting_algorithm.bubble_sort, interval=visual_speed, title="Bubble Sort")
    
if user_choice == "2":
    
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    visualise_sort(list_to_sort, sorting_algorithm.insertion_sort, interval=visual_speed, title="Insertion Sort")
    
if user_choice == "3":
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    visualise_sort(list_to_sort, sorting_algorithm.selection_sort, interval=visual_speed, title="Selection Sort")
    
if user_choice == "4":
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    visualise_sort(list_to_sort, sorting_algorithm.merge_sort, interval=visual_speed, title="Merge Sort")
    
if user_choice == "5":
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    visualise_sort(list_to_sort, sorting_algorithm.quick_sort, interval=visual_speed, title="Quick Sort")
    
   
    
