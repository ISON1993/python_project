class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def  collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        html = open('D://tuzhenyu/GitHub/python_project/crawler/baidubaike/output.html','w')
        html.write("<html>")
        html.write("<body>")
        html.write("<table>")

        for data in self.datas:
            html.write("<tr>")
            html.write("<td>%s</td>/n"% data['url'])
            html.write("<td>%s</td>/n"% data['title'].encode('UTF-8'))
            # html.write("<td>%s</td>/n"% data['summary'].encode('UTF-8'))
            html.write("</tr>")

        html.write("</table>")
        html.write("</body>")
        html.write("</html>")

        html.close()
