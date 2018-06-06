#!/usr/bin/env python
#coding=utf-8
import random
import sys
from com_zxl_data.CalculateData import *
from com_zxl_common.InputUtil import *
from com_zxl_common.RegularUtil import *
class CalculateUtil(BaseUtil):

	mInputUtil = InputUtil()
	mRegularUtil = RegularUtil()

	# def __init__(self):
	# 	self.mPrintUtil.show("CalculateUtil init...")

	def do_calculate(self, calculate_range, calculate_operator, mCalculateResult):
		calculate_operator = int(calculate_operator)
		# self.mPrintUtil.show("do_calculate::calculate_operator = %s " % calculate_operator)
		mCalculateData = CalculateData()

		mCalculateData.calculate_arg1 = self.__get_random_int(calculate_range)
		mCalculateData.calculate_arg2 = self.__get_random_int(calculate_range)
		mCalculateData.calculate_operator_arg = calculate_operator
		# self.mPrintUtil.show("calculate_arg1 = %d" % calculate_arg1 + " calculate_arg2 = %d" % calculate_arg2)

		if calculate_operator == 1:
			self.__do_addition_calculate(mCalculateData)
		elif calculate_operator == 2:
			self.__do_subtraction_calculate(mCalculateData)
		elif calculate_operator == 3:
			self.__do_multiplucation_calculate(mCalculateData)
		elif calculate_operator == 4:
			self.__do_division_calculate(mCalculateData)
		else:
			return self.do_calculate(calculate_range, self.__get_random_int((1, 4)), mCalculateResult)

		self.__check_calculate_result(mCalculateData, mCalculateResult)
		return mCalculateResult

	def __get_random_int(self, tuple_int):
		return random.randint(int(tuple_int[0]), int(tuple_int[1]))

	def __do_addition_calculate(self, mCalculateData):
		mCalculateData.calculate_operator_str = "+"
		mCalculateData.calculate_result = mCalculateData.calculate_arg1 + mCalculateData.calculate_arg2

	def __do_subtraction_calculate(self, mCalculateData):
		mCalculateData.calculate_operator_str = "-"
		if mCalculateData.calculate_arg1 < mCalculateData.calculate_arg2:
			temp = mCalculateData.calculate_arg1
			mCalculateData.calculate_arg1 = mCalculateData.calculate_arg2
			mCalculateData.calculate_arg2 = temp
		mCalculateData.calculate_result = mCalculateData.calculate_arg1 - mCalculateData.calculate_arg2

	def __do_multiplucation_calculate(self, mCalculateData):
		mCalculateData.calculate_operator_str = "×"
		mCalculateData.calculate_result = mCalculateData.calculate_arg1 * mCalculateData.calculate_arg2

	def __do_division_calculate(self, mCalculateData):
		mCalculateData.calculate_operator_str = "÷"
		if mCalculateData.calculate_arg2 == 0:
			temp = mCalculateData.calculate_arg1
			mCalculateData.calculate_arg1 = mCalculateData.calculate_arg2
			mCalculateData.calculate_arg2 = temp
		mCalculateData.calculate_result = round(float(mCalculateData.calculate_arg1) / float(mCalculateData.calculate_arg2), 2)

	def __check_calculate_result(self, mCalculateData, mCalculateResult):
		input_content = self.mInputUtil.get_input("请计算 %d " % mCalculateData.calculate_arg1 + mCalculateData.calculate_operator_str + " %d" % mCalculateData.calculate_arg2 + " : ")

		if input_content == 'r':
			accuracy_value = 0
			if mCalculateResult.total_count > 0:
				accuracy_value = float(mCalculateResult.right_count) / float(mCalculateResult.total_count) * 100

			self.mPrintUtil.show("\n")
			self.mPrintUtil.show("\033[4;37mtotal   : \033[1;36m%d" % mCalculateResult.total_count + "\033[0m\033[0m")
			self.mPrintUtil.show("invalid : \033[1;33m%d" % mCalculateResult.invalid_count + "\033[0m")
			self.mPrintUtil.show("right   : \033[1;32m%d" % mCalculateResult.right_count + "\033[0m")
			self.mPrintUtil.show("error   : \033[1;31m%d" % mCalculateResult.error_count + "\033[0m")
			self.mPrintUtil.show("\033[1;46maccuracy: %.2f" % (accuracy_value) + "%" + "\033[0m")
			# self.mPrintUtil.show("\033[1;46mCalculateData size: %d" % (len(mCalculateResult.mCalculateResultList)) + "\033[0m")
			self.mPrintUtil.show("\n")

			self.__check_calculate_result(mCalculateData, mCalculateResult)
		elif input_content == 'q':
			self.mPrintUtil.show("\nByeBye\n")
			sys.exit()
		elif not self.mRegularUtil.do_regular(input_content, r"(\d+)(.\d+)*"):
			self.mPrintUtil.show("你的计算结果格式错误\n")
			mCalculateResult.invalid_count += 1
			self.__check_calculate_result(mCalculateData, mCalculateResult)
		else:
			regular_calculate_result = self.mRegularUtil.do_regular(str(mCalculateData.calculate_result), r"(\d+)(.0)")
			if regular_calculate_result:
				if len(regular_calculate_result.group()) == 3:
					self.mPrintUtil.show("正确结果为 : %d" % int(mCalculateData.calculate_result))
				else:
					self.mPrintUtil.show("正确结果为 : %s" % mCalculateData.calculate_result)
			else:
				self.mPrintUtil.show("正确结果为 : %s" % mCalculateData.calculate_result)

			if mCalculateData.calculate_result - float(input_content) == 0:
				self.mPrintUtil.show("你的计算结果正确 \n")
				mCalculateResult.right_count += 1
				mCalculateData.is_input_calculate_result_right = True
			else:
				self.mPrintUtil.show("你的计算结果错误 \n")
				mCalculateResult.error_count += 1
				mCalculateData.is_input_calculate_result_right = False

			mCalculateData.input_calculate_result = input_content
			mCalculateResult.total_count += 1
			mCalculateResult.mCalculateResultList.append(mCalculateData)
