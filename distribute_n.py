# 1.1 - distribute_n()
def distribute_n(n, k):
    """
    Distributes integer n across a list of k elements,
    where each element is at least 1 and all elements sum to n.
    Returns None if n < k.
    """
    if n < k:
        return None

    # Start by giving every element the minimum value of 1
    result = [1] * k

    # Distribute the remainder across the elements
    remainder = n - k
    for i in range(remainder):
        result[i % k] += 1

    return result
# --- Example usage ---
print("1.1 - distribute_n()")
print(distribute_n(10, 3))   # e.g. [5, 3, 2]
print(distribute_n(5, 5))    # [1, 1, 1, 1, 1]
print(distribute_n(3, 5))    # None (n < k)
print()
