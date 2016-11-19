import re

f = open('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program015/city.txt','r')
info = re.compile(r'\[(\d+),(\d+),(\d+)\]')
for x in info.findall(f.read()):
    print(x)
