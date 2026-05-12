
# 1.2 - pie_chart()

def pie_chart(percentages):
    """
    Takes a list of real numbers (percentages) that must sum to exactly 100.
    Returns a list of tuples (p, share) where share is p as a fraction of 360.
    Returns None if the percentages do not sum to exactly 100.
    """
    if round(sum(percentages), 10) != 100:
        return None

    return [(p, (p / 100) * 360) for p in percentages]


# --- Example usage ---
print("1.2 - pie_chart()")
print(pie_chart([25, 25, 25, 25]))        # [(25, 90.0), (25, 90.0), ...]
print(pie_chart([50, 30, 20]))            # [(50, 180.0), (30, 108.0), (20, 72.0)]
print(pie_chart([40, 40, 40]))            # None (sums to 120, not 100)
print()
