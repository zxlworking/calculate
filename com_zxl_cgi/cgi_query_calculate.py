#!C:\Python27\python.exe
#coding=utf-8

import cgi, cgitb

from com_zxl_common.DBUtil import *
from com_zxl_common.PrintUtil import *

mDBUtil = DBUtil()
mPrintUtil = PrintUtil()

form = cgi.FieldStorage()

page = form.getvalue("page")
count = form.getvalue("count")

result = mDBUtil.query_to_calculate(page, count)
mPrintUtil.show(result)

# print "Content-type:text/html"
# print ""
#
# print """<html>
# <body>
# <h1>Hello,Python</h1>
# <h12>Test cgi calculate</h2>
# </body>
# </html>
# """
# print "......1"

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


