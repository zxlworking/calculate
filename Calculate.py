#!/usr/bin/env python
#coding=utf-8

import random

from com_zxl_common.SigintUtil import *
from com_zxl_common.CalculateUtil import *
from com_zxl_common.InputUtil import *
from com_zxl_common.RegularUtil import *
from com_zxl_data.CalculateResult import *

mPrintUtil = PrintUtil()


class Calculate:
	mSigintUtil = SigintUtil()
	mCalculateUtil = CalculateUtil()
	mInputUtil = InputUtil()
	mRegularUtil = RegularUtil()

	def start(self):

		# regular_calculate_result = self.mRegularUtil.do_regular(str(2.0), r"(\d+)(.0)")
		# mPrintUtil.show("group = %s " % regular_calculate_result.group(0))
		# mPrintUtil.show("group = %s " % regular_calculate_result.group(1))
		# mPrintUtil.show("group = %s " % regular_calculate_result.group(2))

		calculate_range = self.mInputUtil.get_calculate_range_input()
		# mPrintUtil.show(calculate_range)

		calculate_operator = self.mInputUtil.get_calculate_operator_input()
		# mPrintUtil.show("calculate_operator = " + calculate_operator)

		mCalculateResult = CalculateResult()

		while True:

			self.mCalculateUtil.do_calculate(calculate_range, calculate_operator, mCalculateResult)

			if self.mSigintUtil.is_sigint_up == True:
				print "\nByeBye\n"
				break


if __name__ == "__main__":
	# mPrintUtil.show("Calculate main...")
	mCalculate = Calculate()
	mCalculate.start()

# else:
# 	mPrintUtil.show("Calculate no main...")
