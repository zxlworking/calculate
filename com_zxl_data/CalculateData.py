#!C:\Python27\python.exe
#coding=utf-8
from com_zxl_data.BaseData import *


class CalculateData(BaseData):
	_id = 0
	calculate_arg1 = 0
	calculate_arg2 = 0

	calculate_operator_arg = 0
	calculate_operator_str = ""

	calculate_result = 0
	input_calculate_result = ""
	is_input_calculate_result_right = 0

	calculate_date = 0

	# def __init__(self):
	# 	self.mPrintUtil.show("CalculateData init...")
