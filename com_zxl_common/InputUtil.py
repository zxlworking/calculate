#!/usr/bin/env python
#coding=utf-8
from com_zxl_common.BaseUtil import *
from com_zxl_common.RegularUtil import *
class InputUtil(BaseUtil):

	mRegularUtil = RegularUtil()

	# def __init__(self):
	# 	self.mPrintUtil.show("InputUtil init...")

	def get_input(self, input_message):
		input_result = raw_input(input_message)
		return input_result

	def get_calculate_range_input(self):
		input_result = raw_input("请输入计算范围(例如:0-100):")
		regular_result = self.mRegularUtil.do_regular(input_result, r"(\d+)" + "-" + "(\d+)")
		if regular_result:
			if(int(regular_result.group(1)) >= int(regular_result.group(2))):
				self.mPrintUtil.show("输入计算范围错误")
				return self.get_calculate_range_input()
			else:
				tuple_result = (regular_result.group(1), regular_result.group(2))
				return tuple_result
		else:
			self.mPrintUtil.show_input_type_error()
			return self.get_calculate_range_input()

	def get_calculate_operator_input(self):
		input_result = raw_input("请输入计算格式(1.加法 2.减法 3.乘法 4.除法 5.随机):")
		regular_result = self.mRegularUtil.do_regular(input_result, r"([1-5])")
		if regular_result:
			return regular_result.group(0)
		else:
			self.mPrintUtil.show("选择计算格式错误")
			return self.get_calculate_operator_input()
