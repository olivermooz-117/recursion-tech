# test_fibonacci.py
import pytest
from fibonacci_demo import fibonacci, fibonacci_memo, fibonacci_iterative

# ============================================================
# Basic Tests
# ============================================================

def test_fibonacci_base_cases():
    """Test the base cases n=0 and n=1"""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_small_values():
    """Test known Fibonacci values"""
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for n, val in enumerate(expected):
        assert fibonacci(n) == val

def test_fibonacci_five():
    """Test fibonacci(5) = 5"""
    assert fibonacci(5) == 5

def test_fibonacci_seven():
    """Test fibonacci(7) = 13"""
    assert fibonacci(7) == 13

def test_fibonacci_ten():
    """Test fibonacci(10) = 55"""
    assert fibonacci(10) == 55

# ============================================================
# Comparison Tests (all versions should match)
# ============================================================

def test_versions_match_for_small_values():
    """Memoized and iterative versions should match naive"""
    for n in range(20):
        assert fibonacci_memo(n) == fibonacci(n)
        assert fibonacci_iterative(n) == fibonacci(n)

def test_versions_match_for_larger_values():
    """Test consistency across versions for larger n"""
    for n in range(20, 30):
        assert fibonacci_memo(n) == fibonacci_iterative(n)

# ============================================================
# Performance / Edge Case Tests
# ============================================================

def test_fibonacci_negative():
    """Test negative input (should return None or raise error)"""
    # This depends on your implementation
    # If your function doesn't handle negatives, it might recurse infinitely
    with pytest.raises(RecursionError):
        fibonacci(-1)  # This will blow up the stack

def test_fibonacci_very_large_memoized():
    """Memoized can handle larger values efficiently"""
    # n=100 with memoization is fast
    result = fibonacci_memo(100)
    assert result == 354224848179261915075  # Known value

def test_fibonacci_iterative_large():
    """Iterative version handles large values without recursion limits"""
    result = fibonacci_iterative(100)
    assert result == 354224848179261915075

# ============================================================
# Parameterized Tests (more concise!)
# ============================================================

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
])
def test_fibonacci_params(n, expected):
    """Test multiple values using parameterization"""
    assert fibonacci(n) == expected

# ============================================================
# Runtime Comparison (optional, shows performance difference)
# ============================================================

def test_runtime_comparison():
    """Compare execution times (for documentation/learning)"""
    import time
    
    n = 30
    
    # Naive recursive
    start = time.time()
    fib_naive = fibonacci(n)
    time_naive = time.time() - start
    
    # Memoized
    start = time.time()
    fib_memo = fibonacci_memo(n)
    time_memo = time.time() - start
    
    # Iterative
    start = time.time()
    fib_iter = fibonacci_iterative(n)
    time_iter = time.time() - start
    
    # All should match
    assert fib_naive == fib_memo == fib_iter
    
    # Print for visibility (pytest captures this with -s flag)
    print(f"\nfibonacci({n}):")
    print(f"  Naive:     {time_naive:.4f}s")
    print(f"  Memoized:  {time_memo:.4f}s")
    print(f"  Iterative: {time_iter:.4f}s")
    
    # Memoized and iterative should be faster for n=30
    assert time_memo < time_naive
    assert time_iter < time_naive