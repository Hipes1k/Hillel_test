def lake_depth(h):
    n = len(h)
    if n <= 2:
        return 0

    max_depth = max(0, max(min(max(h[:i + 1]), max(h[i:])) - h[i] for i in range(n)))

    return max_depth
