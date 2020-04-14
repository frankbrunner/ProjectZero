import mysql.connector
from ProjectZero.src.rp_db_struct import *

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

    def getProjects(self, Project_id=None):
        #if no Parameter return all Projects
        #Return the Result list of tubles or None if not exist
        table="Projects"
        rows=["id","number","description"]

        if Project_id != None:
            conditions=["id"]
            values = [Project_id]
        else:
            conditions=[]
            values = []

        sql = self.sqlGenerator(table,rows,conditions,values)
        result=self.readData(sql)

        if result == False:
            return None
        return result

    def getProjectId(self, ProjectNumber):
        #if no Parameter return all Projects
        #Return the Result list of tubles or None if not exist
        obj_Projects = Projects()
        table=obj_Projects.tablename
        conditions=[obj_Projects.number]
        values = [ProjectNumber]
        rows=["id"]

        sql = self.sqlGenerator(table,rows,conditions,values)

        result=self.readData(sql)

        if result == False:
            return None
        else:
            result = result[0]
            result = result[0]
        return result

    def insertProject(self, ProjectNumber, ProjectDescription):
        #Return Codes
        #0 Project successfull insert
        #1 Project allready exist
        #2 any Failure
        table = "Projects"
        rows = ["number", "description"]
        values = [int(ProjectNumber), str(ProjectDescription)]
        select = "number"
        return (self.checkAndInsert(table,rows,values,select))


    # def deleteProject(self,ProjectNumber):
    #     #Return Codes
    #     #0 Project successfull deleted
    #     #1 any Failure
    #     table = "Projects"
    #     row = "number"
    #     value = ProjectNumber
    #     returnCode = self.recordDelete(table,row,value)
    #     return returnCode

    def getReleases(self,Testobject_id=None):
        #Return the Result tuble or None if not exist
        obj_Releases = Releases()
        table=obj_Releases.tablename
        rows= obj_Releases.rows

        if Testobject_id != None:
            conditions = ["testobject_id"]
            values = [Testobject_id]
        else:
            conditions = []
            values = []

        sql = self.sqlGenerator(table,rows,conditions,values)
        result=self.readData(sql)
        if result == False:
            return None
        return result

    def getReleaseID(self,ReleaseDescription):
        #Return ReleaseID from specific Release
        # Return Codes
        # 2 any Failure
        obj_Releases = Releases()
        table=obj_Releases.tablename
        rows= obj_Releases.rows

        if ReleaseDescription != None:
            conditions = [obj_Releases.description]
            values = [ReleaseDescription]
        else:
            pass

        sql = self.sqlGenerator(table,rows,conditions,values)
        result=self.readData(sql)
        if result == False:
            return 2
        return result

    def insertRelease(self, Year=0, Type="MDR", Description="Medium Release"):
        #Return Codes
        #0 Project successfull insert
        #1 Project allready exis
        #2 any Failure
        obj_Releases = Releases()
        table = obj_Releases.tablename
        rows = obj_Releases.rows
        values = [int(Year), str(Type),str(Description)]
        return (self.checkAndInsert(table,rows,values))

    def deleteRelease(self,row="Description",value="MDR01"):
        #Return Codes
        #0 Project successfull deleted
        #1 any Failure
        table = "Data_Releases"
        returnCode = self.recordDelete(table,row,value)
        return returnCode

    def createTestobject(self, Porject_id=0, Demand_id=0, Planning_Item_id=0, Application_id=0):
        #Return Code
        #0 Project successfull insert
        #1 Project allready exis
        #2 any Failure
        obj_Testobject = Testobject()
        table = obj_Testobject.tablename
        rows = obj_Testobject.rows
        values = [str(Porject_id), str(Demand_id),str(Planning_Item_id),str(Application_id)]
        select=obj_Testobject.project_id

        condition=obj_Testobject.project_id
        condition_value = Porject_id

        returnValue = self.checkIfExists(table,condition,condition_value)
        if returnValue==False:
            sql = self.sqlGenearatorInsert(table,rows,values)
            self.insertData(sql,values)
        else:
            return 1
        return returnValue

    def getTestobjectID(self, ProjectNumber):
        #Return the id of Testobject
        obj_Testobject = Testobject()
        obj_join = Projects()
        table= obj_Testobject.tablename
        rows= obj_Testobject.rows
        conditions=[obj_Testobject.project_id]
        conditionsValue = [ProjectNumber]

        sql = 'SELECT ' + obj_Testobject.tablename + '.id'\
              ' FROM ' + obj_Testobject.tablename + \
              ' INNER JOIN ' + obj_join.tablename +\
              ' ON ' + obj_Testobject.tablename + '.' + obj_Testobject.project_id + '=' + obj_join.tablename + '.id ' \
              'WHERE ' + obj_join.number +'="' + str(ProjectNumber) +'"';

        result=self.readData(sql)

        if result == False:
            return None
        else:
            result = result[0]
            result = result[0]
        return result

    def createDemand(self,demand,Testobject_id=0,Release_id=0,Application_id=0,Supply_id=0):
        #minimum for demnad is Application and Release
        #return values 0 insert ok 1 allready exist 2 entry criterias notok
        table = Demand()
        conditions = [table.application_id,table.release_id]
        #if an demand combination from Applicatio and Release allready exists
        conditions_value = [Application_id,Release_id]

        values = [demand,Testobject_id,Release_id,Application_id,Supply_id]

        if Application_id and Release_id:
            returnValue = self.checkAndInsert(table.tablename,table.rows,values)

        return returnValue

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
            row = obj_join.description

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
        sql = "select "
        #rows to select
        if rows:
            for item in rows:
                sql = sql + str(item)+ ","
            sql = sql[0:-1]
        else:
            return None
         #add table
        sql = sql + " from "+str(table)+" "
        x=0
        if len(conditions) > 0:
            sql = sql + " where "
            for item in conditions:
                sql = sql + " "+str(item) +"=" +str(values[x])
                sql = sql +" and"
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

    def checkAndInsert(self,table,rows,values,select="*"):
        #Return Codes
        #0 Project successfull insert
        #1 Project allready exis
        #2 any Failure
        print(table,rows,values,select)
        if self.checkIfExists(table,rows,values,select):
            #when True value is allready in db Return 1
            return 1
        else:
            sql = self.sqlGenearatorInsert(table,rows,values)
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

    def checkIfExists(self, table, conditions, values, select="*"):
        #its used the count function because its easy to to verify 0 means not exists >0 mean exists

        if type(conditions) == str:
            sql = 'SELECT Count(' + str(select) + ') FROM ' + str(table) +  ' WHERE ' + str(conditions) + ' = "' + str(values) +'"'
            print (sql)
        #Der Type wird abgefragt um festzustellen ob es sich um nur eine condition geht oder mehrere
        if type(conditions) == list:
            sql = "SELECT Count(" + str(select) + ") FROM " + str(table) + " WHERE "
            x = 0
            for item in conditions:
                sql = sql +  str(item) + ' = "' + str(values[x]) +'" and '
                x +=1
            sql = sql[0:-4]
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

    def recordDelete(self, table, row, value):
        #Return Codes
        #0 Project successful deletet
        #1 not exist or error
        sql = 'delete from ' + table + ' where ' + row + '="' + str(value)+'"'
        try:
            self.dbcursor.execute(sql)
            self.db.commit()
            return 0
        except mysql.connector.errors.ProgrammingError as error:
            return 1






