import mysql.connector
from src.classes.db_shema import TestObject


class DB_Functions():
    def __init__(self):
        self.host = "localhost"
        self.user = "dbuser"
        self.passwd = "34df!5awe"
        self.database = "ProjectZero"
        self.dbconnect()

    def dbconnect(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            passwd=self.passwd,
            database=self.database)
        self.dbcursor = self.db.cursor()

    def record_create(self, table, columns=[],values=[],debug=False):
        #returns 0 for not created
        #return 1 for created entry
        sql = "insert into " + table + " ("

        for item in columns:
            sql = sql + str(item)+","
        sql = sql[0:-1]+") values ("

        for value in values:
            sql = sql + "%s,"
        sql = sql[0:-1] + ")"

        if debug:
            print(sql)
        try:
            self.dbcursor.execute(sql, values)
            self.db.commit()
            return 0
        except mysql.connector.errors.ProgrammingError as error:
            print(error)
            return 1
        finally:
            self.dbcursor.close()

    def get_data_from_table(self, table_object, condition_attribute, condition_value):
        # We use the SQL Generater for easy handling
        return_value={}
        for attribute in table_object.column:
            sql = self.sqlGenerator(table_object.table_name, [attribute], [condition_attribute], [condition_value])
            #  after sql ist created handel to the read function
            result = self.readData(sql, debug=True)
            #the result coms as tubel with values as tubels so first extract and ad the value to the correct value pair
            return_value[attribute] = result[0][0]
        # result as a value pair object is given back
        return return_value

    def get_attribute_from_table(self,table_object, attribute, condition_attribute, condition_value):
        # We use the SQL Generater for easy handling
        sql = self.sqlGenerator(table_object.table_name, attribute, [condition_attribute], [condition_value])
        result = self.readData(sql, debug=False)
        return result

    def record_update(self, table, column, value, condition_attribute, condition_value):
        sql = ""
        if type(column) == str:
            sql = 'UPDATE ' + str(table) + ' ' \
                                           'SET ' + str(column) + '= "' + str(value) + '" ' \
                                                                                       'WHERE ' + str(
                condition_attribute) + ' = "' + str(condition_value) + '"'
            print(sql)
        if type(column) == list:
            x = 0
            sql = 'UPDATE ' + str(table) + ' SET '
            for item in column:
                sql = sql + str(item) + ' = "' + str(value[x]) + '",'
                x += 1
            sql = sql[0:-1]
            sql = sql + ' WHERE '
            if type(condition_attribute) == str:
                sql = sql + str(condition_attribute) + ' = "' + str(condition_value)+ '"'
            x = 0
            if type(condition_attribute) == list:
                sql = sql + str(condition_attribute) + ' =  "' + str(condition_value[x])+ '"and "'
                x += 1
            if type(condition_attribute) == list:
                sql = sql[0:-6]
        print(sql)
        try:
            self.dbcursor.execute(sql)
            self.db.commit()
            return 0
        except mysql.connector.errors.ProgrammingError as error:
            return 1

    def list_records(self,table_obj):
        # We use the SQL Generater for easy handling
        return_value = []
        sql = self.sqlGenerator(table_obj.table_name, table_obj.column)
        result = self.readData(sql, debug=False)
        return_value = [table_obj.column,result]
        return return_value

    def sqlGenerator(self, table, colums, conditions=[], values=[]):
        sql = 'select '
        # rows to select
        if type(colums) == list:
            for item in colums:
                sql = sql + str(item) + ','
            sql = sql[0:-1]

        if type(colums) == str:
            sql = sql + colums

        # add table
        sql = sql + ' from ' + str(table) + ' '
        x = 0
        if len(conditions) > 0:
            sql = sql + ' where '
            for item in conditions:
                sql = sql + ' ' + str(item) + '="' + str(values[x]) + '"'
                sql = sql + ' and'
                x += 1
            sql = sql[0:-3]

        return str(sql)

    def sqlGenearatorInsert(self, table, rows, values):
        sql = "INSERT INTO " + table + "("
        # rows to select
        if rows:
            for item in rows:
                sql = sql + str(item) + ","
            sql = sql[0:-1]
            sql = sql + ")"
        else:
            return None
        # insert vallues
        sql = sql + " VALUES ("
        for item in rows:
            sql = sql + "%s,"
        sql = sql[0:-1] + ")"

        return sql

    def checkAndInsert(self, table, columns, values, debug=False, select="*"):
        # Return Codes
        # 0 Project successfull insert
        # 1 Project allready exis
        # 2 any Failure
        if self.checkIfExists(table, columns, values, select):
            if debug == True:
                print("checkIFExist: " + str(self.checkIfExists(table, columns, values, select)))
                print("values: " + str(values))
            # when True value is allready in db Return 1
            return 1
        else:
            sql = self.sqlGenearatorInsert(table, columns, values)
            if debug == True:
                print("sql: " + str(sql))
                print("values: " + str(values))
            if self.insertData(sql, values):
                # if Return 0 recored has been created
                return 0
            else:
                return 2

    def readData(self, sql, debug=False):
        if debug:
            print("readData sql:" + str(sql))
        try:
            self.dbcursor.execute(sql)
            result = self.dbcursor.fetchall()
            return result

        except mysql.connector.errors.ProgrammingError as error:
            result = 0
        return result

    def insertData(self, sql, val):
        try:
            self.dbcursor.execute(sql, val)
            self.db.commit()
            return True
        except mysql.connector.errors.ProgrammingError as error:
            return False

    def checkIfExists(self, table, conditions, values, select="*", debug=False):
        # its used the count function because its easy to to verify 0 means not exists >0 mean exists

        if type(conditions) == str:
            sql = 'SELECT Count(' + str(select) + ') FROM ' + str(table) + ' WHERE ' + str(conditions) + ' = "' + str(
                values) + '"'
            if debug:
                print(sql)
        # Der Type wird abgefragt um festzustellen ob es sich um nur eine condition geht oder mehrere
        if type(conditions) == list:
            sql = "SELECT Count(" + str(select) + ") FROM " + str(table) + " WHERE "
            x = 0
            for item in conditions:
                sql = sql + str(item) + ' = "' + str(values[x]) + '" and '
                x += 1
            sql = sql[0:-4]
            if debug:
                print(sql)
        try:
            self.dbcursor.execute(sql)
            result = self.dbcursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False

        except mysql.connector.errors.ProgrammingError as error:
            result = False

    def tableDelete(self, tableName):
        try:
            sql = "DROP TABLE " + tableName
            self.dbcursor.execute(sql)
            return True
        except mysql.connector.errors.ProgrammingError as error:
            # table does not exist
            if error.sqlstate == "42S02":
                return error.sqlstate
            else:
                return error.msg

    def delete_record(self, table, column, value):
        # Return Codes
        # 0 Project successful deletet
        # 1 not exist or error
        sql = 'delete from ' + str(table) + ' where '
        if type(column) == str:
            sql = sql + str(column) + '="' + str(value) + '"'
        if type(column) == list:
            x = 0
            for item in column:
                sql = sql + str(item) + '="' + str(value[x]) + '" and '
                x += 1
            sql = sql[0:-4]
        print (sql)
        try:
            self.dbcursor.execute(sql)
            self.db.commit()
            return 0
        except mysql.connector.errors.ProgrammingError as error:
            return 1

    def getTableID(self, tablename, conditionColumn, conditionValue, debugMode=False):
        # function Return a list of tubles
        # Return Code 1 no value for column
        # Return Code 2 conditionCoum conditionValue match issue not the same count of values
        if type(conditionColumn) == str and type(conditionValue == str):
            sql = 'SELECT id FROM ' + tablename + ' WHERE ' + conditionColumn + '="' + conditionValue + '"'
            self.debugMode("sql", sql, debugMode)

        if type(conditionColumn) == list and type(
                conditionValue == list and len(conditionColumn) == len(conditionValue)):
            sql = 'SELECT id FROM ' + tablename + ' WHERE '
            x = 0
            for item in conditionColumn:
                sql = sql + str(item) + ' = "' + str(conditionValue[x]) + '" and '
                x += 1
            sql = sql[0:-4]
            self.debugMode("sql", sql, debugMode)
            returnValue = self.readData(sql)
            returnValue = returnValue[0]
            returnValue = returnValue[0]
        else:
            return 2
        return returnValue

    def table_create(self, tablename, rows, values=None):
        sql = "create table "
        sql = sql + str(tablename)
        """definitino of rows"""
        sql = sql + "(id int auto_increment primary key,"
        if type(rows) == str:
            sql = sql + str(rows) + ","
        else:
            x = 0
            for item in rows:
                if values == None:
                    sql = sql + str(item) + ","
                else:
                    sql = sql + str(item) + " " + str(values[x]) + ","
                    x += 1
        try:
            sql = sql + 'create_at timestamp default current_timestamp)'
            print(sql)
            self.dbcursor.execute(sql)
            print("succesfull created")
            return True
        except mysql.connector.errors.ProgrammingError as error:
            # Table allready exist
            if error.sqlstate == "42S01":
                print("Error 42S01")
                return error.sqlstate
            else:
                return error.msg
        # finally:
        #     self.dbcursor.close()

    def debugMode(self, printDescription, printValue, debugMode):
        if debugMode:
            print(str(printDescription + ": " + str(printValue)))

    # def getDemand(self, testobject_id, tableDemand_id="release"):
    #     # Return the Result tuble or None if not exist
    #     #creat an dbStruct Obect to clear dublicatesl
    #
    #     obj_Demand = Demand()
    #
    #     if tableDemand_id == "application":
    #         obj_join = Applications()
    #         tableDemand_id = obj_Demand.application_id
    #         obj_join = Applications()
    #         row = obj_join.release
    #
    #     if tableDemand_id == "release":
    #         obj_join = Releases()
    #         tableDemand_id = obj_Demand.release_id
    #         row = obj_join.release
    #
    #     sql = 'SELECT ' + obj_join.name + '.' + row +\
    #           ' FROM ' + obj_Demand.name + \
    #           ' INNER JOIN ' + obj_join.name +\
    #           ' ON ' + obj_Demand.name + '.' + tableDemand_id + '=' + obj_join.name + '.id ' \
    #           'WHERE ' + obj_Demand.release_application_id + '="' + str(testobject_id) + '"';
    #
    #     result = self.readData(sql)
    #     if result == False:
    #         return None
    #     return result
