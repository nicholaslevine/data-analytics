import re
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "listing.txt")
with open(file_path, "r") as text:
    for line in text:
        pattern = r".*\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+([\w\.\-\_]+)$"
        match = re.match(pattern, line)
        if (match):
            print(int(match.group(1)), str(match.group(2)), int(match.group(3)), int (match.group(4)), int(match.group(5)), str(match.group(6)))
        