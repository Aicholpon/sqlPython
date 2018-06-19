def find_most_common(a):
    wordDict = {}
    for line in lines:
        wordList = lines.split()
    for word in wordList:
        if word in wordDict: 
            wordDict[word] += 1
        else: 
            wordDict[word] = 1
    return wordDict
