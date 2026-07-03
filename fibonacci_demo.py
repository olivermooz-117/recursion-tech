# fibonacci_demo.py

def fibonacci(n):
    """Return the nth Fibonacci number recursively."""
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_debug(n, depth=0):
    """Debug version that prints call stack and return values."""
    indent = " " * depth
    print(f"{indent}fibonacci({n}) called")
    
    if n == 0:
        print(f"{indent}return 0")
        return 0
    elif n == 1:
        print(f"{indent}return 1")
        return 1
    
    val = fibonacci_debug(n - 1, depth + 1) + fibonacci_debug(n - 2, depth + 1)
    print(f"{indent}return {val} for fibonacci({n})")
    return val


def fibonacci_memo(n, memo=None):
    """Optimized version using memoization to avoid redundant calls."""
    if memo is None:
        memo = {}
    
    # Check if value is already computed
    if n in memo:
        return memo[n]
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Compute and store
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n):
    """Iterative version for comparison (more efficient)."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print("=" * 50)
    print("Testing Fibonacci (Recursive)")
    print("=" * 50)
    
    # Test small values
    test_values = [0, 1, 5, 7, 10]
    for n in test_values:
        result = fibonacci(n)
        print(f"fibonacci({n}) = {result}")
    
    print("\n" + "=" * 50)
    print("Testing Debug Version with n=5")
    print("=" * 50)
    fibonacci_debug(5)
    
    print("\n" + "=" * 50)
    print("Performance Comparison")
    print("=" * 50)
    
    import time
    
    n = 30
    print(f"\nComputing fibonacci({n})...")
    
    # Recursive (naive) - may take a moment
    start = time.time()
    result_naive = fibonacci(n)
    time_naive = time.time() - start
    print(f"Naive Recursive: {result_naive} (time: {time_naive:.4f}s)")
    
    # Memoized
    start = time.time()
    result_memo = fibonacci_memo(n)
    time_memo = time.time() - start
    print(f"Memoized Recursive: {result_memo} (time: {time_memo:.4f}s)")
    
    # Iterative
    start = time.time()
    result_iter = fibonacci_iterative(n)
    time_iter = time.time() - start
    print(f"Iterative: {result_iter} (time: {time_iter:.4f}s)")