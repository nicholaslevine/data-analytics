import os
import re

def file_extensions(filename):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open (file_path, "r") as files:
        final_tuple = ([], {})
        for file in files:
            match = re.match(r".*\.([^\.]+)$", file)
            if not match:
                final_tuple[0].append(file)
            else:
                dict = final_tuple[1]
                dict[file] = dict.get(file, 0) + 1
    return final_tuple
print(file_extensions("filenames.txt"))
