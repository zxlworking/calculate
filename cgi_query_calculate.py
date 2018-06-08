#!C:\Python27\python.exe
#coding=utf-8

import cgi, cgitb
import json
import sys
import time
from com_zxl_common.DBUtil import *
from com_zxl_common.PrintUtil import *

reload(sys)
sys.setdefaultencoding("utf8")

form = cgi.FieldStorage()

page = form.getvalue("page")
count = form.getvalue("count")

mDBUtil = DBUtil()
mPrintUtil = PrintUtil()

if page is None or count is None:
    page = 0
    count = 10

total_count = mDBUtil.query_to_calculate_total_count()
total_count = total_count / count + 1

result = mDBUtil.query_to_calculate(page, count)
#print "result-->%s" + result
if not result is None:

    to_show_data_str = ""
    for json_element_result in json.loads(result)['result']:
        check_result = "正确" if json_element_result["is_input_calculate_result_right"] == 1 else "错误"
        to_show_data_str = to_show_data_str + \
                           "<tr><td><center>%s</center></td>" % json_element_result["_id"] + \
                           "<td><center>%s</center></td>" % json_element_result["calculate_arg1"] + \
                           "<td><center>%s</center></td>" % json_element_result["calculate_operator_str"] + \
                           "<td><center>%s</center></td>" % json_element_result["calculate_arg2"] + \
                           "<td><center>%s</center></td>" % json_element_result["calculate_result"] + \
                           "<td><center>%s</center></td>" % json_element_result["input_calculate_result"] + \
                           "<td><center>%s</center></td>" % check_result + \
                           "<td><center>%s</center></td></tr>" % (time.strftime("%Y-%m-%d %H:%M:%S",  time.localtime(json_element_result["calculate_date"])))

    print "Content-type:text/html"
    print ""

    print """
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>test title</title>
        </head>
        <body>
            <form>
                <table border="1">
                    <tr>
                        <td width="10%"><center>编号</center></td>
                        <td width="10%"><center>参数1</center></td>
                        <td width="10%"><center>操作符</center></td>
                        <td width="10%"><center>参数2</center></td>
                        <td width="10%"><center>结果</center></td>
                        <td width="10%"><center>输入值</center></td>
                        <td width="10%"><center>是否正确</center></td>
                        <td width="30%"><center>时间</center></td>
                    </tr>         
                    """ + \
                      to_show_data_str + \
                    """
                    <tr>
                        <td><button>上一页</button></td>
                    """ + \
                        "<td><center>%s/%s<input id=\"current_page\" type=\"hidden\" value=\"%s\" hide=true/></center></td>" % ((int(page) + 1), total_count, page) + \
                    """
                        <td><button>下一页</button></td>
                    </tr>
                </table>
            </form>
        </body>
    </html>
    """






# if __name__ == "__main__":
# 	print "Content-type:text/html"
# 	print ""
#
# 	print """<html>
# 	<body>
# 	<h1>Hello,Python</h1>
# 	<h12>Test cgi</h2>
# 	</body>
# 	</html>
# 	"""
#     print "......"
# else:
#     import cgi, cgitb
#
#     from com_zxl_common.DBUtil import *
#     from com_zxl_common.PrintUtil import *
#
#     mDBUtil = DBUtil()
#     mPrintUtil = PrintUtil()
#
#     form = cgi.FieldStorage()
#
#     page = form.getvalue("page")
#     count = form.getvalue("count")
#
#     result = mDBUtil.query_to_calculate(page, count)
#     mPrintUtil.show(result)


