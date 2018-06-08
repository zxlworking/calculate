#!C:\Python27\python.exe
#coding=utf-8
import signal
import sys
from com_zxl_common.BaseUtil import *


class SigintUtil(BaseUtil):
	is_sigint_up = False

	def sigint_handler(self, signum, frame):
		is_sigint_up = True
		self.mPrintUtil.show("\nByeBye\n")
		sys.exit()

	def __init__(self):
		# self.mPrintUtil.show("SigintUtil init...")
		signal.signal(signal.SIGINT, self.sigint_handler)
		#signal.signal(signal.SIGHUP, self.sigint_handler)
		signal.signal(signal.SIGTERM, self.sigint_handler)