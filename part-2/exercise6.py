import os
import sys

def file_count(file_name):
    try:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        with open(file_path, "r") as file:
            lines_count = 0
            word_count = 0
            charSum = 0
            for line in file:
                lines_count+=1
                charSum += len(line)
                words = line.split(" ")
                wordsinline = len(words)
                word_count+=wordsinline
    except FileNotFoundError:
        return (0, 0, 0)
    return f"{lines_count}\t{word_count}\t{charSum}\t{file_name}"

def main():
    for filename in sys.argv[1:]:
        return_string = file_count(filename)
        print(return_string)
main()