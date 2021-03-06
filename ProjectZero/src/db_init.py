from ProjectZero.src.db_connect import mySql
from ProjectZero.src.functions_projects import *

import mysql.connector

class InitDB():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="dbuser",
            passwd="34df!5awe"
        )
        self.mycursor = self.mydb.cursor()

    def deletDatabase(self):
        self.mycursor.execute("DROP DATABASE IF EXISTS ProjectZero")

    def createDatabase(self):
        self.mycursor.execute("CREATE DATABASE ProjectZero")

    def creatDBUser(self):
        self.mycursor.execute("CREATE USER IF NOT EXISTS'dbuser'@'localhost' IDENTIFIED BY '34df!5awe'" )

    def setPermissions(self):
        self.mycursor.execute("GRANT ALL PRIVILEGES ON  *.* TO 'dbuser'@'localhost'")

    def createTables(self):
        sql = mySql("dbuser", "34df!5awe", "ProjectZero")
        # Creat Datata Tables
        obj_Projects = Projects()
        sql.tableCreate(obj_Projects.tablename, obj_Projects.rows, obj_Projects.types)

        obj_Releases = Releases()
        print(obj_Releases.tablename, obj_Releases.column, obj_Releases.types)
        sql.tableCreate(obj_Releases.tablename, obj_Releases.column, obj_Releases.types)

        obj_Applications = Applications()
        sql.tableCreate(obj_Applications.tablename, obj_Applications.rows, obj_Applications.types)

        rows = ["Firstname varchar(250)", "Secondname varchar(250)", "Capacity float(11,1)"]
        sql.tableCreate("Data_Employee", rows)

        # Creat Mapping Tables
        obj_Testobject = Testobject()
        sql.tableCreate(obj_Testobject.tablename, obj_Testobject.rows, obj_Testobject.types)

        obj_Demand = Demand()
        sql.tableCreate(obj_Demand.tablename, obj_Demand.rows, obj_Demand.types)

        obj_Testobject_Application= Testobject_Release()
        sql.tableCreate(obj_Testobject_Application.tablename, obj_Testobject_Application.rows, obj_Testobject_Application.types)

        obj_Release_Application= Release_Application()
        sql.tableCreate(obj_Release_Application.tablename, obj_Release_Application.column, obj_Release_Application.types)
        #
        # sql.executeSql("set foreign_key_checks = 0")
        # #Initial remove alle constrains and delet tables
        # tables=["Projects",
        #         "Releases",
        #         "Applications",
        #         "Data_Employee",
        #         "Testobject",
        #         "Demand"]
        # for item in tables:
        #     sql.tableDelete(item)

init = InitDB()

if __name__ == '__main__':
    init.deletDatabase()
    init.createDatabase()
    init.creatDBUser()
    init.createTables()


