"""
Counting pattern
The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use dictionries to track the count of each word indipendently
"""

counts = dict()
print("Enter a line:")
line = input("")
words = line.split()
print("Words: ", words)

print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0)+1
print("Counts: ", counts)