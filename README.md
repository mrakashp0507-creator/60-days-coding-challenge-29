# Day 29 – Frequency Analysis: Trending Hashtag Detector

## Overview
A Python program that analyzes hashtag frequency and identifies the Top K most frequently used hashtags. It compares sorting-based and heap-based selection algorithms and visualizes trending results using a text-based bar chart.

## Features
- Count hashtag occurrences using `collections.Counter`.
- Normalize hashtag text to avoid case-sensitive duplicates.
- Find Top K hashtags using sorting.
- Find Top K hashtags using heap-based selection.
- Compare execution times with `time.perf_counter()`.
- Display a text-based trending chart.
- Verify that both approaches return the same ranking.

## Example
**Input:** `K = 3`

**Expected Top 3:**
- `#ai` — 5 uses
- `#python` — 5 uses
- `#coding` — 4 uses

Hashtags with equal frequency are ranked alphabetically.

## Algorithms

### 1. Sorting-Based Approach
Sorts all unique hashtags by frequency and selects the first K entries.

- Time complexity: O(m log m)
- Additional result space: O(m)

### 2. Heap-Based Approach
Uses Python's `heapq.nsmallest()` to select the Top K entries without requiring a complete sorted ranking.

- Typical time complexity: O(m log K) when K is much smaller than m
- Selection space: depends on K and the implementation; `heapq.nsmallest()` uses a heap-based selection strategy for small K.

Here, m represents the number of unique hashtags.

Frequency counting takes O(n) average time, where n is the number of input hashtags.

## Performance Analysis
The program benchmarks both selection methods and also tests a larger dataset containing 100,000 hashtag entries. Actual execution times depend on the computer and Python environment.

## How to Run
1. Install Python 3.
2. Open the project folder in VS Code.
3. Create `day29_trending_hashtags.py`.
4. Run:

```bash
python day29_trending_hashtags.py
```

5. Enter the required value of K.

## Real-World Applications
- Social media trending pages
- Popular video and music discovery
- Product recommendation systems
- Search analytics
- Frequently occurring events and keywords

## Learning Outcomes
Learned frequency counting, sorting, heap-based selection, benchmarking, complexity analysis, and result visualization.

**Note:** This is a local prototype using sample data, not a live social media feed.
