# Sorting Algorithm Visualiser

A Python-based sorting visualisation tool that animates sorting operations using Matplotlib.

## Overview

This project visualises the execution of multiple sorting algorithms on a randomly generated integer list. It provides:

- Real-time bar-chart animation of array updates
- Highlighting of active indices during comparisons/swaps
- Operation count display (`Swaps`)
- Total execution time on completion

## Implemented Algorithms

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort

## Tech Stack

- Python
- NumPy (data generation)
- Matplotlib (rendering and animation)

## Project Structure

```
.
├── main.py
└── README.md
```

## Requirements

- Python 3.9+
- `matplotlib`
- `numpy`

Install dependencies:

```bash
pip install matplotlib numpy
```

## Running the Application

From the project root:

```bash
python main.py
```

You will be prompted to select an algorithm:

1. Bubble Sort  
2. Insertion Sort  
3. Selection Sort  
4. Merge Sort  
5. Quick Sort

After selection, a Matplotlib window opens and animates the chosen algorithm.

## Configuration

Edit values in `main.py` to adjust runtime behavior:

- `list_to_sort`: source data (currently random integers)
- `visual_speed`: animation frame interval in milliseconds

Example:

```python
list_to_sort = np.random.randint(1, 100, size=100).tolist()
visual_speed = 10
```

## Notes on Metrics

The on-screen `Swaps` value represents operation counts emitted by each algorithm implementation. Depending on the algorithm, this may reflect swaps, writes, or shift operations.

## Troubleshooting

- If no window appears, ensure your Python environment supports GUI backends for Matplotlib.
- If execution is slow, reduce input size or increase `visual_speed`.
- If dependencies are missing, reinstall with:

```bash
pip install --upgrade matplotlib numpy
```
