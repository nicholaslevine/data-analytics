import re 
def integers_in_brackets(str):
    matches = re.finditer(r"\[\s*(-?\d+)\s*\]", str)
    nums = [int(match.group(1)) for match in matches]
    return nums
print(integers_in_brackets(" afd [asd] [12] [a34] [ -43 ]tt [+12]xxx"))