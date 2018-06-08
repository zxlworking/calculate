#!C:\Python27\python.exe
#coding=utf-8
import mysql.connector
import json
from mysql.connector import errorcode
from com_zxl_common.BaseUtil import *
from com_zxl_db.CalculateDB import *
from com_zxl_data.CalculateData import *


class DBUtil(BaseUtil):
    def __init__(self):
        global cnx
        global cursor
        try:
            cnx = mysql.connector.connect(user='zxl', password='root', host='118.25.178.69', database=CalculateDB.DATABASE_NAME)
            cursor = cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.mPrintUtil.show("Something is wrong with your user name or password")
                exit(1)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                self.mPrintUtil.show("Database does not exist")
                cnx = mysql.connector.connect(user='zxl', password='root', host='118.25.178.69')
                cursor = cnx.cursor()
                self.__create_database()
                self.__create_table()
            else:
                self.mPrintUtil.show(err)
                exit(1)
        else:
            self.__create_table()
            self.mPrintUtil.show("DBUtil init finish")

    def __create_database(self):
        try:
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(CalculateDB.DATABASE_NAME))
            cnx.database = CalculateDB.DATABASE_NAME
            self.mPrintUtil.show("Create database finish")
        except mysql.connector.Error as err:
            self.mPrintUtil.show("Failed creating database: {}".format(err))
            exit(1)

    def __create_table(self):
        for name, ddl in CalculateDB.TABLES.iteritems():
            try:
                self.mPrintUtil.show("Creating table {}: ".format(name),)
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    self.mPrintUtil.show("already exists.")
                else:
                    self.mPrintUtil.show(err.msg)
                    exit(1)
            else:
                self.mPrintUtil.show("OK")

    def insert_to_calculate(self, mCalculateData):
        data_calculate = (mCalculateData.calculate_arg1,
                          mCalculateData.calculate_arg2,
                          mCalculateData.calculate_operator_arg,
                          mCalculateData.calculate_operator_str,
                          mCalculateData.calculate_result,
                          mCalculateData.input_calculate_result,
                          mCalculateData.is_input_calculate_result_right,
                          mCalculateData.calculate_date)
        cursor.execute(CalculateDB.INSERT_CALCULATE_SQL, data_calculate)
        cnx.commit()

    def query_to_calculate(self, page, count):
        if page is None or count is None:
            #self.mPrintUtil.show("query_to_calculate...no param page = %s,count = %s" % (page, count))
            return
        query_param = (str(int(page) * int(count)), str(count))
        ######
        #self.mPrintUtil.show(query_param)
        ######
        cursor.execute(CalculateDB.QUERY_CALCULATE_SQL % query_param)
        result_element_list = []
        for (_id, calculate_arg1, calculate_arg2, calculate_operator_arg, calculate_operator_str, calculate_result,
             input_calculate_result, is_input_calculate_result_right, calculate_date) in cursor:
            #print("{} {} {} {} {} {} {} {} {} ".format(_id, calculate_arg1, calculate_arg2, calculate_operator_arg,
                                                         # calculate_operator_str, calculate_result,
                                                         # input_calculate_result, is_input_calculate_result_right,
                                                         # calculate_date))
            result_element = {"_id": _id, "calculate_arg1": calculate_arg1, "calculate_arg2": calculate_arg2,
                              "calculate_operator_arg": calculate_operator_arg,
                              "calculate_operator_str": calculate_operator_str,
                              "calculate_result": calculate_result, "input_calculate_result": input_calculate_result,
                              "is_input_calculate_result_right": is_input_calculate_result_right,
                              "calculate_date": calculate_date}
            result_element_list.append(result_element)
        result = {"result": result_element_list}
        return json.dumps(result)

    def query_to_calculate_total_count(self):
        cursor.execute(CalculateDB.QUERY_CALCULATE_TOTAL_COUNT_SQL)
        for(total_count, ) in cursor:
            return total_count

    def close_db(self):
        cursor.close()
        cnx.close()
