
from collections import Counter
import heapq
import time


def normalize_hashtags(hashtags):
    """Normalize hashtag text for consistent counting."""
    return [
        tag.strip().lower()
        for tag in hashtags
        if tag.strip()
    ]


def top_k_sorting(frequency, k):
    """Sort all unique hashtags by frequency, then alphabetically."""
    return sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


def top_k_heap(frequency, k):
    """Use heap-based selection to retrieve the Top K entries."""
    return heapq.nsmallest(
        k,
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )


def visualize_trending(trending):
    """Display a simple frequency bar chart."""
    print("\n=== Trending Hashtags ===")

    if not trending:
        print("No hashtags to display.")
        return

    max_count = trending[0][1]
    max_bar_width = 30

    for hashtag, count in trending:
        bar_length = max(1, round(count / max_count * max_bar_width))
        bar = "#" * bar_length
        print(f"{hashtag:15} | {bar} ({count})")


def main():
    print("=" * 45)
    print("       TRENDING HASHTAG DETECTOR")
    print("=" * 45)

    sample_hashtags = [
        "#Python", "#AI", "#Coding", "#Python",
        "#Tech", "#AI", "#Python", "#DataScience",
        "#Coding", "#AI", "#Python", "#Tech",
        "#AI", "#Coding", "#Python", "#DataScience",
        "#AI", "#Coding", "#Tech", "#DataScience"
    ]

    hashtags = normalize_hashtags(sample_hashtags)
    frequency = Counter(hashtags)

    print("\nAnalyzed hashtags:")
    print(hashtags)

    try:
        k = int(input("\nEnter Top K (number of trends): "))

        if k <= 0:
            print("K must be greater than zero.")
            return

        k = min(k, len(frequency))

        # Sorting approach
        start = time.perf_counter()
        sorting_result = top_k_sorting(frequency, k)
        sorting_time = time.perf_counter() - start

        # Heap-based approach
        start = time.perf_counter()
        heap_result = top_k_heap(frequency, k)
        heap_time = time.perf_counter() - start

        print("\n=== Sorting-Based Results ===")
        for rank, (tag, count) in enumerate(sorting_result, start=1):
            print(f"{rank}. {tag}: {count} uses")

        print("\n=== Heap-Based Results ===")
        for rank, (tag, count) in enumerate(heap_result, start=1):
            print(f"{rank}. {tag}: {count} uses")

        # Visualize the shared results
        visualize_trending(heap_result)

        print("\n=== Performance Comparison ===")
        print("Unique hashtags:", len(frequency))
        print("K:", k)
        print(f"Sorting time: {sorting_time:.8f} seconds")
        print(f"Heap time:    {heap_time:.8f} seconds")

        if sorting_result == heap_result:
            print("Verification: Both methods returned the same results.")
        else:
            print("Verification: Results differ; investigate the implementations.")

        # Larger benchmark with repeatable test data
        print("\n=== Larger Benchmark ===")
        hashtag_pool = [
            f"#trend{i}" for i in range(1000)
        ]
        large_data = [
            hashtag_pool[(i * 37 + i // 7) % len(hashtag_pool)]
            for i in range(100000)
        ]
        large_frequency = Counter(large_data)
        benchmark_k = 10

        start = time.perf_counter()
        top_k_sorting(large_frequency, benchmark_k)
        large_sort_time = time.perf_counter() - start

        start = time.perf_counter()
        top_k_heap(large_frequency, benchmark_k)
        large_heap_time = time.perf_counter() - start

        print("Total hashtag entries:", len(large_data))
        print("Unique hashtags:", len(large_frequency))
        print("Top K:", benchmark_k)
        print(f"Sorting selection: {large_sort_time:.8f} seconds")
        print(f"Heap selection:     {large_heap_time:.8f} seconds")

    except ValueError:
        print("Please enter a valid integer for K.")

    print("\nTrending analysis completed!")


if __name__ == "__main__":
    main()
