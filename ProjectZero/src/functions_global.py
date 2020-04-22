import mysql.connector


class db_functions():
    def __init__(self, User, Passwd, Database):
        self.host = "localhost"
        self.user = str(User)
        self.passwd = str(Passwd)
        self.database = str(Database)
        self.dbconnect()

    def dbconnect(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user=self.user,
            passwd=self.passwd,
            database=self.database)
        self.dbcursor = self.db.cursor()

    def getDemand(self, testobject_id, tableDemand_id="release"):
        # Return the Result tuble or None if not exist
        #creat an dbStruct Obect to clear dublicatesl

        obj_Demand = Demand()

        if tableDemand_id == "application":
            obj_join = Applications()
            tableDemand_id = obj_Demand.application_id
            obj_join = Applications()
            row = obj_join.name

        if tableDemand_id == "release":
            obj_join = Releases()
            tableDemand_id = obj_Demand.release_id
            row = obj_join.name

        sql = 'SELECT ' + obj_join.tablename +'.' + row +\
              ' FROM ' + obj_Demand.tablename + \
              ' INNER JOIN ' + obj_join.tablename +\
              ' ON ' + obj_Demand.tablename + '.' + tableDemand_id + '=' + obj_join.tablename + '.id ' \
              'WHERE '+obj_Demand.testobject_id+'="'+str(testobject_id)+'"';

        result = self.readData(sql)
        if result == False:
            return None
        return result

    def sqlGenerator(self, table, rows, conditions=[],values=[]):
        sql = 'select '
        #rows to select
        if rows:
            for item in rows:
                sql = sql + str(item)+ ','
            sql = sql[0:-1]
        else:
            return None
         #add table
        sql = sql + ' from '+str(table)+' '
        x=0
        if len(conditions) > 0:
            sql = sql + ' where '
            for item in conditions:
                sql = sql + ' '+str(item) +'="' +str(values[x])+'"'
                sql = sql +' and'
                x +=1
            sql = sql[0:-3]

        return sql

    def sqlGenearatorInsert(self,table,rows,values):
        sql = "INSERT INTO "+table+"("
        #rows to select
        if rows:
            for item in rows:
                sql = sql + str(item) +","
            sql = sql[0:-1]
            sql = sql +")"
        else:
            return None
        #insert vallues
        sql = sql + " VALUES ("
        for item in rows:
            sql = sql +"%s,"
        sql = sql[0:-1]+")"

        return sql

    def checkAndInsert(self,table,rows,values,debug=False ,select="*"):
        #Return Codes
        #0 Project successfull insert
        #1 Project allready exis
        #2 any Failure
        if self.checkIfExists(table,rows,values,select):
            if debug:
                print("checkIFExist: "+str(self.checkIfExists(table,rows,values,select)))
            #when True value is allready in db Return 1
            return 1
        else:
            sql = self.sqlGenearatorInsert(table,rows,values)
            if debug:
                print("sql: "+str(sql))
            if self.insertData(sql,values):
                #if Return 0 recored has been created
                return 0
            else:
                return 2

    def readData(self, sql):
        try:
            self.dbcursor.execute(sql)
            result = self.dbcursor.fetchall()
            return result

        except mysql.connector.errors.ProgrammingError as error:
            result = False
        return result

    def insertData(self,sql,val):
        try:
            self.dbcursor.execute(sql,val)
            self.db.commit()
            return True
        except mysql.connector.errors.ProgrammingError as error:
            return False

    def checkIfExists(self, table, conditions, values, select="*",debug=False):
        #its used the count function because its easy to to verify 0 means not exists >0 mean exists

        if type(conditions) == str:
            sql = 'SELECT Count(' + str(select) + ') FROM ' + str(table) +  ' WHERE ' + str(conditions) + ' = "' + str(values) +'"'
            if debug:
                print(sql)
        #Der Type wird abgefragt um festzustellen ob es sich um nur eine condition geht oder mehrere
        if type(conditions) == list:
            sql = "SELECT Count(" + str(select) + ") FROM " + str(table) + " WHERE "
            x = 0
            for item in conditions:
                sql = sql +  str(item) + ' = "' + str(values[x]) +'" and '
                x +=1
            sql = sql[0:-4]
            if debug:
                print(sql)
        try:
            self.dbcursor.execute(sql)
            result = self.dbcursor.fetchone()
            if result[0]>0:
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

    def recordDelete(self, table, column, value):
        #Return Codes
        #0 Project successful deletet
        #1 not exist or error
        sql = 'delete from ' + str(table) + ' where '
        if type(column) == str:
            sql = sql + str(column) + '="' + str(value) + '"'
        if type(column) == list:
            x=0
            for item in column:
                sql = sql + str(item) + '="' + str(value[x])+'" and '
                x+=1
            sql = sql[0:-4]

        try:
            self.dbcursor.execute(sql)
            self.db.commit()
            return 0
        except mysql.connector.errors.ProgrammingError as error:
            return 1

    def updateRecord(self, table, column, value, condition, conditionValue):
        sql=""
        if type(condition) == str:
            sql = 'UPDATE ' + str(table) + ' ' \
                'SET ' + str(column) + '= "' + str(value) + '" ' \
                'WHERE ' + str(condition) + ' = "' + str(conditionValue) + '"'
            print (sql)
        if type(condition) == list:
            x=0
            sql = 'UPDATE ' + str(table) + ' ' \
                    'SET ' + str(column) + '= "' + str(value) + '" WHERE '
            for item in condition:
                sql = sql + str(item) + ' = "' + str(conditionValue[x]) +'" and '
                x += 1
            sql = sql[0:-4]
            print(sql)
        try:
            self.dbcursor.execute(sql)
            self.db.commit()
            return 0
        except mysql.connector.errors.ProgrammingError as error:
            return 1

    def getTableID(self, tablename, conditionColumn, conditionValue,debugMode=False):
        #function Return a list of tubles
        #Return Code 1 no value for column
        # Return Code 2 conditionCoum conditionValue match issue not the same count of values
        if type(conditionColumn) == str and type(conditionValue == str):
            sql = 'SELECT id FROM ' + tablename + ' WHERE ' + conditionColumn + '="' + conditionValue + '"'
            self.debugMode("sql",sql,debugMode)

        if type(conditionColumn) == list and type(conditionValue == list and len(conditionColumn)== len(conditionValue)):
            sql = 'SELECT id FROM ' + tablename + ' WHERE '
            x=0
            for item in conditionColumn:
                sql = sql + str(item) + ' = "' + str(conditionValue[x]) +'" and '
                x += 1
            sql = sql[0:-4]
            self.debugMode("sql", sql, debugMode)
            returnValue = self.readData(sql)
            returnValue = returnValue[0]
            returnValue = returnValue[0]
        else:
            return 2
        return returnValue


    def debugMode(self,printDescription, printValue, debugMode):
        if debugMode:
            print(str(printDescription+": "+str(printValue)))
