#!C:\Python27\python.exe
#coding=utf-8


class CalculateDB:
    DATABASE_NAME = 'calculate_db'
    DB_NAME = 'calculate'
    TABLES = {}
    TABLES['calculate'] = (
        "CREATE TABLE IF NOT EXISTS `calculate` ("
        "  `_id` bigint(20) NOT NULL AUTO_INCREMENT,"
        "  `calculate_arg1` int(11),"
        "  `calculate_arg2` int(11),"
        "  `calculate_operator_arg` int(11),"
        "  `calculate_operator_str` varchar(1) NOT NULL,"
        "  `calculate_result` varchar(16),"
        "  `input_calculate_result` varchar(16),"
        "  `is_input_calculate_result_right` int(1) NOT NULL,"
        "  `calculate_date` bigint(20) NOT NULL,"
        "  PRIMARY KEY (`_id`)"
        ") ENGINE=InnoDB")

    INSERT_CALCULATE_SQL = ("INSERT INTO " + DB_NAME + " " "(calculate_arg1, calculate_arg2, calculate_operator_arg, "
                                                       "calculate_operator_str, "
                                                       "calculate_result, " "input_calculate_result, "
                                                       "is_input_calculate_result_right, "
                                                       "calculate_date) " 
                                                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    QUERY_CALCULATE_SQL = ("SELECT _id, calculate_arg1, calculate_arg2, calculate_operator_arg, "
                           "calculate_operator_str, calculate_result, input_calculate_result, "
                           "is_input_calculate_result_right, "
                           "calculate_date FROM " + DB_NAME +
                           " LIMIT %s , %s")
