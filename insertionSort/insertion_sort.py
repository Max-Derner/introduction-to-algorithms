from time import perf_counter_ns
from random import randint


def sort(unsorted_nums: list[int]) -> list[int]:
    print(f"Sorting {len(unsorted_nums)} items...", end='')
    start = perf_counter_ns()
    sorted_nums = unsorted_nums.copy()
    for i in range(1, len(sorted_nums)):
        unum = sorted_nums[i]
        j = i - 1
        while j >= 0 and sorted_nums[j] > unum:
            sorted_nums[j+1] = sorted_nums[j]
            j -= 1
        sorted_nums[j+1] = unum

    # Display time taken
    time_delta = perf_counter_ns() - start
    millisecs, nanosecs = divmod(time_delta, 1_000_000)
    secs, millisecs = divmod(millisecs, 1_000)
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    readable_time = (
        ""
        + f"{hours}hrs " if hours else ""
        + f"{mins}mins " if mins else ""
        + f"{secs}secs " if secs else ""
        + f"{millisecs}ms" if millisecs else ""
        + f"{nanosecs}ns" if nanosecs and not millisecs else ""
    )
    print(f"took {readable_time} -- number of seconds: {time_delta//1_000_000}")
    return sorted_nums


def main():
    unsorted = []
    for _ in range(1000):
        unsorted.extend(
            [randint(0, 32_000) for _ in range(1000)]
        )
        sort(unsorted)


if __name__ == "__main__":
    main()
