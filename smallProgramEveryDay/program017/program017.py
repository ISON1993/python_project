import xlwt,xlrd
import json
from lxml import etree

data = xlrd.open_workbook('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program014/student.xls')
table = data.sheets()[0]
nrows = table.nrows

Dict = {}
for i in range(nrows ):
	Arr = table.row_values(i)
	Dict[Arr[0]] = Arr[1:]
root = etree.Element("root")
child1 = etree.SubElement(root, "student")
comm = etree.Comment(u"""学生信息表 "id" : [名字, 数学, 语文, 英文]""")
child1.append(comm)
child1.text =unicode(json.dumps(Dict).decode("utf-8"))
tree = etree.ElementTree(root)
tree.write('D://tuzhenyu/GitHub/python_project/smallProgramEveryDay/program017/student.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
