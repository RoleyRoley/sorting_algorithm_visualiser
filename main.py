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



print("Which sorting algorithm do you want to use?")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Selection Sort")
print("4. Merge Sort")
print("5. Quick Sort")
print(len(list_to_sort))


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
            
            

        
if user_choice == "1":
    
    sorting_algorithm = SortingAlgorithm(list_to_sort)
    visualise_sort(list_to_sort, sorting_algorithm.bubble_sort, interval=visual_speed, title="Bubble Sort")
   
    
