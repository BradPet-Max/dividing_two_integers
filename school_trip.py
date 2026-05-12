# 1.3 - school_trip()
def school_trip(n):
    """
    Takes the number of students n going on a trip.
    Taxis hold a maximum of 8 students each.
    Returns a list of tuples ("taxi n:", k) where k is the number
    of students in that taxi.
    """
    TAXI_CAPACITY = 8

    num_taxis = -(-n // TAXI_CAPACITY)  # Ceiling division
    result = []

    for i in range(1, num_taxis + 1):
        students_remaining = n - (i - 1) * TAXI_CAPACITY
        k = min(TAXI_CAPACITY, students_remaining)
        result.append((f"taxi {i}:", k))

    return result


# --- Example usage ---
print("1.3 - school_trip()")
print(school_trip(16))   # 2 full taxis of 8
print(school_trip(20))   # 2 taxis of 8, 1 taxi of 4
print(school_trip(1))    # 1 taxi with 1 student
