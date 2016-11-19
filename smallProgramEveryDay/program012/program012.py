wordFilter = set()
# file = open('/home/tuzhenyu/github/python_project/smallProgramEveryDay/program011/words.txt','r')
file = open('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program011/words.txt','r')
for word in file.readlines():
    wordFilter.add(word.rstrip('\n'))
wordInput = input()
for wordf in wordFilter:
    if wordf in wordInput:
        print(wordInput.replace(wordf,'*'))
    else:
        print(wordInput)
