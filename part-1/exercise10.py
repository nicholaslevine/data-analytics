def detect_range(numbers):
    """
    Detects ranges in a list of numbers and returns a list of either:
    - Individual numbers that aren't part of a range
    - Tuples of (start, end) for numbers that form a range (only when there are 2+ consecutive numbers)
    
    Example:
    [2,4,5,6,8] -> [2, (4,6), 8]
    """
    if not numbers:
        return []
        
    numbers = sorted(numbers)
    result = []
    start = numbers[0]
    prev = numbers[0]
    
    def add_sequence(start, end):
        if start == end:
            result.append(start)
        else:
            result.append((start, end))
    
    for num in numbers[1:]:
        if num > prev + 1:
            add_sequence(start, prev)
            start = num
        prev = num
    
    add_sequence(start, prev)
    
    return result

print(detect_range([2,7,1, 3, 20, -2, 5, 8, 3, 10, 12, 4]))