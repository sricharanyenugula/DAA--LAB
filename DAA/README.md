# Max Heap Sort in Python

## 📌 Description

This project implements the **Heap Sort algorithm using a Max Heap** in Python.

The program:

* Accepts the number of elements from the user.
* Accepts array elements as input.
* Builds a Max Heap.
* Sorts the elements using Heap Sort.
* Measures the actual execution time.
* Displays the sorted array.
* Displays the time and space complexity.

## 🛠️ Requirements

* Python 3.x
* No external libraries are required.

The program only uses Python's built-in `time` module for measuring execution time.

## 🚀 How to Run

1. Save the file as:

```text
heapsort.py
```

2. Open a terminal or command prompt.

3. Run:

```bash
python heapsort.py
```

4. Enter the number of elements and the elements when prompted.

## 💻 Example

```text
Enter number of elements: 5

Enter 5 elements:
Element 1: 45
Element 2: 12
Element 3: 89
Element 4: 23
Element 5: 7

Original Array: [45, 12, 89, 23, 7]

Sorted Array: [7, 12, 23, 45, 89]

----- COMPLEXITY ANALYSIS -----
Best Case Time Complexity    : O(n log n)
Average Case Time Complexity : O(n log n)
Worst Case Time Complexity   : O(n log n)
Space Complexity             : O(log n)

Actual Execution Time: ... seconds
```

## 🔍 Algorithm

### 1. Build Max Heap

The input array is converted into a Max Heap. The `heapify()` function compares a node with its left and right children and places the largest value at the root of that subtree.

### 2. Heap Sort

After creating the Max Heap:

* The largest element is present at the root.
* The root element is swapped with the last element.
* The heap size is reduced.
* `heapify()` is called again.
* This process continues until the array is sorted.

## ⏱️ Complexity Analysis

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n log n)      |
| Average Case | O(n log n)      |
| Worst Case   | O(n log n)      |

**Space Complexity:** O(log n)

The program also calculates the actual execution time using `time.perf_counter()`.

## 📂 Project Structure

```text
Heap-Sort/
│
├── heapsort.py
└── README.md
```

## 🎯 Key Features

* Max Heap implementation
* User input support
* In-place sorting
* Execution-time measurement
* Complexity analysis
* Simple and easy-to-understand Python implementation

## 👨‍💻 Author

**Sricharan Yenugula**

## 📄 License

This project is intended for educational and academic purposes.
