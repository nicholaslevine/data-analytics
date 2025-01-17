import os
import math 

script_dir = os.path.dirname(os.path.abspath(__file__))

def summary(file_name):
    file_path = os.path.join(script_dir, file_name)
    numbers = []  
    
    with open(file_path, "r") as nums:
        for line in nums:
            numbers.append(float(line.strip()))
    
    count = len(numbers)
    sum_nums = sum(numbers)
    avg = sum_nums / count
    
    squared_diff_sum = sum((x - avg) ** 2 for x in numbers)
    std = math.sqrt(squared_diff_sum / (count - 1))  # Using n-1 for sample standard deviation
    
    print(f"File: {file_name} Sum: {sum_nums:.6f} Avg: {avg:.6f} Stddev: {std:.6f}")

summary("example1.txt")