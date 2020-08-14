from src.classes.db_functions import DB_Functions
import src.classes.db_shema as db_structur
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
        sql = DB_Functions()
        table_obj = db_structur.Team()
        sql.table_create(table_obj.table_name, table_obj.column, table_obj.types)

        table_obj = db_structur.User()
        sql.table_create(table_obj.table_name, table_obj.column, table_obj.types)

        obj_Applications = db_structur.Application()
        print(obj_Applications.table_name, obj_Applications.column, obj_Applications.types)
        sql.table_create(obj_Applications.table_name, obj_Applications.column, obj_Applications.types)

        obj_Releases = db_structur.Releases()
        # print(obj_Releases.name, obj_Releases.column, obj_Releases.types)
        sql.table_create(obj_Releases.table_name, obj_Releases.column, obj_Releases.types)

        obj_Project_Releases = db_structur.Project_Releases()
        sql.table_create(obj_Project_Releases.name, obj_Project_Releases.column, obj_Project_Releases.types)

        obj_Project_Applications = db_structur.Project_Applications()
        sql.table_create(obj_Project_Applications.name, obj_Project_Applications.column, obj_Project_Applications.types)


        #obj_Projects = db_structur.Projects()
        #print(obj_Projects.name, obj_Projects.column, obj_Projects.types)
        #sql.table_create(obj_Projects.name, obj_Projects.column, obj_Projects.types)







        # Creat Mapping Tables
        obj_Testobject = db_structur.TestObject()

        sql.table_create(obj_Testobject.name, obj_Testobject.column, obj_Testobject.types)


        # rows = ["Firstname varchar(250)", "Secondname varchar(250)", "Capacity float(11,1)"]
        # sql.("Data_Employee", rows)


        # obj_Demand = db_structur.Demand()
        # sql.table_create(obj_Demand.name, obj_Demand.column, obj_Demand.types)
        #

        # obj_Release_Application=db_structur.Release_Application()
        # sql.table_create(obj_Release_Application.name, obj_Release_Application.column, obj_Release_Application.types)
        # #
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
    #init.deletDatabase()
    #init.createDatabase()
    #init.creatDBUser()
    init.createTables()


