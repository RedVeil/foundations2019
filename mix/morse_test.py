'''
Let's practice using @classmethod!

Create a class method in Letter named from_string that takes a string like "dash-dot" and creates an instance with the correct pattern (['_', '.']).
''''

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, str):
        pattern = []
        lst1 = str.split("-")
        for i in lst1:
            if i =="dot" :
                pattern.append(".")
            else:
                pattern.append("_")
        return pattern
