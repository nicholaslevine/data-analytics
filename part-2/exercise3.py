import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "rgb.txt")

with open(file_path, "r") as rgb_file:
    
    next(rgb_file)  
    
    for line in rgb_file:
        match = re.match(r"\s*(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)", line.strip())
        if match:
            print(f"{int(match.group(1))}\t{int(match.group(2))}\t{int(match.group(3))}\t{match.group(4)}")