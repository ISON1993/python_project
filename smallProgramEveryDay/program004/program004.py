import re
f = open('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program004/input.txt','r')
dict1 = {}
for char in f.read():
    if(char not in dict1):
        dict1[char] = 1
    else:
        dict1[char] = dict1[char]+1
print(dict1)
dict2={}
for str in f.readlines():
    for word in str.split(' '):
        if(word not in dict2):
            dict2[word] = 1
        else:
            dict2[word] = dict2[word] + 1
print(dict2)
dict3={}
for str in f.readlines():
    for word in re.split(' |  |,|\.|\\n',str):
        if(word not in dict3):
            dict3[word] = 1
        else:
            dict3[word] = dict3[word] + 1
print(dict3)
f.close()
