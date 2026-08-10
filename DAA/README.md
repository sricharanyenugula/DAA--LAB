# Searching Algorithms in Python

This repository contains Python implementations of two fundamental searching algorithms:

* **Linear Search**
* **Binary Search**

Both programs take user input, search for a specified element, and measure the execution time of the search operation.

## 📁 Files

| File              | Description                     |
| ----------------- | ------------------------------- |
| `Linearsearch.py` | Implementation of Linear Search |
| `binarysearch.py` | Implementation of Binary Search |

---

## 🔍 Linear Search

Linear Search checks each element of the array sequentially until the required element is found or the end of the array is reached.

### Features

* Takes the number of elements as input.
* Accepts array elements from the user.
* Searches for a specified element.
* Displays the position of the element if found.
* Measures execution time in microseconds.

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | `O(1)`     |
| Average Case | `O(n)`     |
| Worst Case   | `O(n)`     |

The implementation returns the index when the element is found and `-1` when it is not found.

### Run

```bash
python Linearsearch.py
```

### Example

```text
Enter number of elements: 5
Enter elements:
10 20 30 40 50
Enter element to search: 30

Search Result:
Element found at position: 3

Time Complexity:
Best Case    : O(1)
Average Case : O(n)
Worst Case   : O(n)

Execution Time: 1.20 microseconds
```

---

## 🔎 Binary Search

Binary Search is an efficient searching algorithm that repeatedly divides the search range into two halves.

In this implementation, the input array is sorted before performing the search.

### Features

* Takes the number of elements as input.
* Accepts array elements from the user.
* Sorts the array.
* Searches for the required element using Binary Search.
* Measures execution time in microseconds.
* Displays time and space complexity.

### Time Complexity

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | `O(1)`     |
| Average Case | `O(log n)` |
| Worst Case   | `O(log n)` |

### Space Complexity

```text
O(1)
```

The program performs the Binary Search using `low`, `high`, and `mid` pointers.

### Run

```bash
python binarysearch.py
```

### Example

```text
Enter number of elements: 5
Enter elements:
50 10 40 20 30

Sorted Array:
10 20 30 40 50

Enter element to search: 30

Search Result:
Element found at position: 3

Time Complexity:
Best Case    : O(1)
Average Case : O(log n)
Worst Case   : O(log n)
Space Complexity: O(1)

Execution Time: 1.00 microseconds
```

---

## ⚖️ Linear Search vs Binary Search

| Feature              | Linear Search          | Binary Search      |
| -------------------- | ---------------------- | ------------------ |
| Searching Method     | Sequential             | Divide and Conquer |
| Array Must Be Sorted | No                     | Yes                |
| Best Case            | `O(1)`                 | `O(1)`             |
| Average Case         | `O(n)`                 | `O(log n)`         |
| Worst Case           | `O(n)`                 | `O(log n)`         |
| Space Complexity     | —                      | `O(1)`             |
| Suitable For         | Small or unsorted data | Sorted data        |

---

## 🛠️ Requirements

* Python 3.x
* No external libraries are required.

The programs use Python's built-in `time` module to measure execution time.

---

## 🚀 How to Use

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Open the project directory:

```bash
cd <repository-name>
```

3. Run either program:

```bash
python Linearsearch.py
```

or

```bash
python binarysearch.py
```

4. Enter the number of elements, array values, and the element you want to search for.

---

## 📚 Learning Objectives

This project demonstrates:

* Searching algorithms
* Time complexity analysis
* Space complexity
* User input handling in Python
* Execution-time measurement
* Comparison between Linear Search and Binary Search

## 👨‍💻 Author

**Sricharan Yenugula**


