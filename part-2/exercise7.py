class Prepend:
    def __init__(self, str):
        self.string = str
    def write(self, text):
        print(self.string + text)
p = Prepend("+++ ")
p.write("Hello")