import re

text = "The quick brown fox jumps brown over the lazy dog"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
