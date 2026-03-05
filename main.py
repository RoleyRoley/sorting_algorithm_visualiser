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

        # Function that takes two parameters, left and right, which represent the indices of the portion of the array being sorted. 
        def merge_sort_recursive(left, right):
            nonlocal swap_counter

            # if right - left is less than or equal to 1, it means that the portion of the array being sorted has one or zero elements, which is already sorted, so we return.
            if right - left <= 1:
                return

            # Calculate the midpoint index.
            midpoint = int((left + right) / 2)

            # Recursively call merge_sort_recursive on the left and right halves of the array. This will continue to divide the array until we reach the base case of one or zero elements.
            yield from merge_sort_recursive(left, midpoint)
            yield from merge_sort_recursive(midpoint, right)

            # After the recursive calls, we have two sorted halves of the array. We then merge these halves together while keeping track of the swap count.
            lefthalf = a[left : midpoint]
            righthalf = a[midpoint : right]
            i = 0
            j = 0
            k = left

            while i < len(lefthalf) and j < len(righthalf):
                yield a, (left + i, midpoint + j), swap_counter, None
                if lefthalf[i] <= righthalf[j]:
                    a[k] = lefthalf[i]
                    i = i + 1
                else:
                    a[k] = righthalf[j]
                    j = j + 1
                swap_counter += 1
                yield a, (k,), swap_counter, None
                k = k + 1

            while i < len(lefthalf):
                a[k] = lefthalf[i]
                i = i + 1
                swap_counter += 1
                yield a, (k,), swap_counter, None
                k = k + 1

            while j < len(righthalf):
                a[k] = righthalf[j]
                j = j + 1
                swap_counter += 1
                yield a, (k,), swap_counter, None
                k = k + 1

        yield from merge_sort_recursive(0, len(a))

        end_time = time.perf_counter()
        yield a, None, swap_counter, (end_time - start_time)
        return
            
    def quick_sort(self, data):
        start_time = time.perf_counter()
        # Create copy of original array
        a = data[:]
            
        swap_counter = 0

        def partition(low, high):
            nonlocal swap_counter
            # Select rightmost element
            pivot = a[high]
            # Index of smaller element
            i = low - 1

            # Iterate through the array from low to high - 1
            for j in range(low, high):
                yield a, (j, high), swap_counter, None
                # If the current element is smaller than or equal to the pivot, we increment the index of the smaller element and swap it with the current element. This ensures that all elements less than or equal to the pivot are on the left side of the pivot.
                if a[j] <= pivot:
                    i = i + 1
                    if i != j:
                        a[i], a[j] = a[j], a[i]
                        swap_counter += 1
                        yield a, (i, j), swap_counter, None
            # After the loop, we swap the pivot element with the element at index i + 1, which places the pivot in its correct position in the sorted array.
            if i + 1 != high:
                a[i + 1], a[high] = a[high], a[i + 1]
                swap_counter += 1
                yield a, (i + 1, high), swap_counter, None

            return i + 1

        # Recursive function that takes two parameters, low and high, which represent the indices of the portion of the array being sorted.
        def quick_sort_recursive(low, high):
            if low < high:
                pivot_idx = yield from partition(low, high)
                yield from quick_sort_recursive(low, pivot_idx - 1)
                yield from quick_sort_recursive(pivot_idx + 1, high)

        yield from quick_sort_recursive(0, len(a) - 1)

        end_time = time.perf_counter()
        yield a, None, swap_counter, (end_time - start_time)
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
    
   
    
