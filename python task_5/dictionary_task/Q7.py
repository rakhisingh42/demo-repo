#Create a function that takes a list of words and groups them in to a dictionary based on the length of each word.
def group_words(words):
    groups = {}
    for word in words :
        length = len(word)
        if length in groups :
            groups[length].append(word)
        else :
            groups[length] = [word]
    return groups

words = ["apple", "banana", "dog", "cat", "elephant", "table", "chair"]
result = group_words(words)
print(result)