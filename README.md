# Sorting Algorithm Visualizer

An interactive browser-based visualizer for 5 classic sorting algorithms, built with pure **HTML, CSS, and JavaScript** — no libraries, no frameworks, no installation needed.

🔗 **Live Demo:** [View on GitHub Pages](https://varnika-reddy.github.io/sorting-visualizer)

---

## Algorithms Included

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

---

## Features

- **Real-time animation** of comparisons and swaps with distinct color coding
- **Live statistics** — comparison count, swap count, elapsed time updated each step
- **Adjustable array size** (10–80 elements) and **sorting speed** (1–10x)
- **Time & space complexity** displayed for the selected algorithm
- **Color legend:**
  - 🟦 Default — unsorted bar
  - 🟡 Yellow — two bars being compared
  - 🔴 Red — two bars being swapped
  - 🟣 Purple — current pivot (Quick Sort)
  - 🟢 Green — element placed in final sorted position

---

## How to Run

### Option 1 — Open directly (no setup needed)
```
Double-click index.html → opens in your browser
```

### Option 2 — GitHub Pages (live link)
1. Push `index.html` to a repo named `sorting-visualizer`
2. Go to Settings → Pages → Branch: main → Save
3. Your live link: `https://yourusername.github.io/sorting-visualizer`

---

## Project Structure

```
sorting-visualizer/
└── index.html    ← Everything: HTML + CSS + JavaScript in one file
```

This is intentionally a single-file project — no build step, no dependencies, just open and run.

---

## Why These Algorithms?

These five algorithms cover the full spectrum of sorting approaches:
- **Bubble, Selection, Insertion** — simple O(n²) algorithms, good for understanding basic sorting mechanics
- **Merge Sort** — divide-and-conquer, guaranteed O(n log n), uses extra space
- **Quick Sort** — divide-and-conquer, O(n log n) average, in-place, fastest in practice for most datasets

Visualizing them side-by-side makes the performance difference between O(n²) and O(n log n) immediately obvious.
