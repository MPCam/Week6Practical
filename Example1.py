def safe_divide(a: float, b: float) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        return float('inf')

    