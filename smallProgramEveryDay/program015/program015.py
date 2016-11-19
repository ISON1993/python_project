import re
import xlwt

f = open('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program015/city.txt','r')
info = re.compile('\"(\d+)\":\"(.*?)\",')
book = xlwt.Workbook(encoding='ascii',style_compression=0)
sheet = book.add_sheet('city',cell_overwrite_ok=True)

line = 0
for x in info.findall(f.read()):
    for i in range(len(x)):
        sheet.write(line,i,x[i])
    line = line + 1
book.save('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program015/city.xls')
