import re
import xlwt

f = open("D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program014/student.txt",'r')
book = xlwt.Workbook(encoding = 'utf-8', style_compression=0)
sheet = book.add_sheet('student',cell_overwrite_ok = True)

info = re.compile(r'\"(\d+)\":\[\"(.*?)\",(\d+),(\d+),(\d+)\]')
line = 0
for x in info.findall(f.read()):
    for i in range(len(x)):
        sheet.write(line,i,x[i])
    line = line + 1
book.save('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program014/student.xls')
