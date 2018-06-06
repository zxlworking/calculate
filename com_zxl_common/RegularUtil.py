#!/usr/bin/env python
#coding=utf-8
import re
from com_zxl_common.BaseUtil import *
class RegularUtil(BaseUtil):
	# def __init__(self):
	# 	self.mPrintUtil.show("RegularUtil init...")
	def do_regular(self, content, regular_str):
		pattern = re.compile(regular_str)
		regular_result = pattern.match(content)
		# regular_result = re.match(regular_str, content)
		return regular_result