from typing import List


def possibleChanges(usernames: List[str]) -> List[str]:
    """
    Determine if each username can be made lexicographically smaller by swapping two characters.
    
    A username can be made smaller if there exists any pair of characters (i, j) where i < j
    and username[j] < username[i]. Swapping these characters would make the string smaller.
    
    Args:
        usernames: List of strings to check
        
    Returns:
        List of "YES" or "NO" strings indicating if each username can be made smaller
        
    Time Complexity: O(n²) where n is the length of the longest username
    Space Complexity: O(1) excluding input/output
    
    Examples:
        >>> possibleChanges(["bee", "superhero", "ace"])
        ['NO', 'YES', 'NO']
        >>> possibleChanges(["ab", "ba"])
        ['NO', 'YES']
    """
    if not usernames:
        return []
    
    results = []
    for username in usernames:
        if not username:  # Handle empty strings
            results.append("NO")
            continue
            
        # Optimized single-pass approach: find first character that can be swapped
        can_be_smaller = False
        n = len(username)
        
        # For each position i, check if there's any character after it that's smaller
        for i in range(n - 1):  # No need to check last character
            # Find the smallest character after position i
            min_char_after = min(username[i + 1:])
            if min_char_after < username[i]:
                can_be_smaller = True
                break
        
        results.append("YES" if can_be_smaller else "NO")
            
    return results

def run_tests():
    """Run comprehensive test cases to verify correctness."""
    test_cases = [
        # Basic test cases
        (["bee", "superhero", "ace"], ['NO', 'YES', 'NO']),
        (["ab", "ba"], ['NO', 'YES']),
        
        # Edge cases
        ([], []),  # Empty input
        ([""], ['NO']),  # Empty string
        (["a"], ['NO']),  # Single character
        (["aa"], ['NO']),  # Same characters
        
        # Already sorted (should be NO)
        (["abc", "def", "xyz"], ['NO', 'NO', 'NO']),
        
        # Reverse sorted (should be YES)
        (["cba", "fed", "zyx"], ['YES', 'YES', 'YES']),
        
        # Mixed cases
        (["abcd", "dcba", "abdc"], ['NO', 'YES', 'YES']),
        
        # Special characters
        (["a1b", "1ab", "ab1"], ['YES', 'NO', 'NO']),
    ]
    
    print("Running test cases...")
    all_passed = True
    
    for i, (input_data, expected) in enumerate(test_cases):
        result = possibleChanges(input_data)
        if result == expected:
            print(f"✓ Test {i + 1} passed")
        else:
            print(f"✗ Test {i + 1} failed: {input_data} -> {result}, expected {expected}")
            all_passed = False
    
    if all_passed:
        print("All tests passed! 🎉")
    else:
        print("Some tests failed! ❌")
    
    return all_passed


def benchmark_performance():
    """Benchmark the performance with different input sizes."""
    import time
    import random
    import string
    
    def generate_random_username(length):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    test_sizes = [10, 50, 100, 500, 1000]
    
    print("\nPerformance Benchmark:")
    print("Size\tTime (ms)\tPer Username (μs)")
    print("-" * 40)
    
    for size in test_sizes:
        # Generate test data
        usernames = [generate_random_username(10) for _ in range(size)]
        
        # Benchmark
        start_time = time.time()
        possibleChanges(usernames)
        end_time = time.time()
        
        total_time_ms = (end_time - start_time) * 1000
        per_username_us = (total_time_ms * 1000) / size
        
        print(f"{size}\t{total_time_ms:.2f}\t\t{per_username_us:.2f}")


if __name__ == '__main__':
    # Run tests
    run_tests()
    
    # Run performance benchmark
    benchmark_performance()
    
    # Original examples
    print("\nOriginal examples:")
    usernames_input = ["bee", "superhero", "ace"]
    output = possibleChanges(usernames_input)
    print(f"Input: {usernames_input}")
    print(f"Output: {output}")

    usernames_input_2 = ["ab", "ba"]
    output_2 = possibleChanges(usernames_input_2)
    print(f"Input: {usernames_input_2}")
    print(f"Output: {output_2}")
