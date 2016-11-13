import os,re

L = [x for x in os.listdir('./program006') if os.path.splitext(x)[1] =='.txt']
dict = {}
word_re = re.compile(r'[\w]+')
for x in L:
    f = open('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program006/'+x,'r')
    data = f.read()
    f.close()
    words = word_re.findall(data)
    for word in words:
        if(word not in dict):
            dict[word] = 1
        else:
            dict[word] = dict[word] + 1
    print(dict)
