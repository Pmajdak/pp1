import re

def f(name):
    words = re.findall(r'\b\w', name)
    return "".join(words)