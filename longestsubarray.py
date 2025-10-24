from collections import defaultdict

def longest_subarray_diff_at_most_one(nums):
    left = 0
    counts = defaultdict(int)
    best = 0

    for right, x in enumerate(nums):
        counts[x] += 1

        # Shrink while window invalid: more than 2 distinct or range > 1
        while len(counts) > 2 or (len(counts) >= 2 and (max(counts) - min(counts) > 1)):
            y = nums[left]
            counts[y] -= 1
            if counts[y] == 0:
                del counts[y]
            left += 1

        best = max(best, right - left + 1)

    return best

# Example
arr = [0, 1, 2, 1, 2, 3]
print(longest_subarray_diff_at_most_one(arr))  # 4 (subarray [1,2,1,2])
