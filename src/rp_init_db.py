import unittest
import xlrd
from src.dbconnect import mySql
from Ressourcenplanning.src.rp_db_struct import *




sql = mySql("dbuser","34df!5awe","Ressourcenplanning")

class MyTestCase(unittest.TestCase):

    def test_createTableApplications(self):

        sql.executeSql("set foreign_key_checks = 0")
        #Initial remove alle constrains and delet tables
        tables=["Projects",
                "Releases",
                "Applications",
                "Data_Employee",
                "Testobject",
                "Demand"]
        for item in tables:
            sql.tableDelete(item)


        #Creat Datata Tables
        obj_Projects=Projects()
        self.assertTrue(sql.tableCreate(obj_Projects.tablename,obj_Projects.rows,obj_Projects.types))

        obj_Releases = Releases()
        self.assertTrue(sql.tableCreate(obj_Releases.tablename, obj_Releases.rows,obj_Releases.types))

        obj_Applications = Applications()
        self.assertTrue(sql.tableCreate(obj_Applications.tablename, obj_Applications.rows,obj_Applications.types))

        rows = ["Firstname varchar(250)","Secondname varchar(250)","Capacity float(11,1)"]
        self.assertTrue(sql.tableCreate("Data_Employee", rows))

        #Creat Mapping Tables
        obj_Testobject = Testobject()
        self.assertTrue(sql.tableCreate(obj_Testobject.tablename,obj_Testobject.rows,obj_Testobject.types))

        obj_Demand = Demand()
        self.assertTrue(sql.tableCreate(obj_Demand.tablename, obj_Demand.rows, obj_Demand.types))


        #Creat Relations

        # string = "alter table SuperEntity add fforeign key(Projects_id) References Projects(id)," \
        #          "add foreign key(Releases_id) References SuperEntity_Releases(id)"
        # sql.executeSql(string)
        #
        # string = "alter table SuperEntity_Releases add foreign key(SuperEntity_id) References SuperEntity(id)," \
        #          "add foreign key(Releases_id) References Releases(id)"
        # sql.executeSql(string)


        # sql.recordCreate("Projects", [["Number", "4589"], ["Name", "MusterProject"]])
        #
        # sql.recordCreate("Releases", [["Year", "2020"], ["Type", "MDR"],["Description", "MDR04"]])
        # sql.recordCreate("Releases", [["Year", "2020"], ["Type", "Major"], ["Description", "RE01"]])
        # sql.recordCreate("Releases", [["Year", "2020"], ["Type", "Major"], ["Description", "RE02"]])
        # sql.recordCreate("Releases", [["Year", "2020"], ["Type", "Major"], ["Description", "RE03"]])
        #
        # sql.recordCreate("SuperEntity", [["Projects_id", "1"], ["Releases_id", "1"]])
        #
        # sql.recordCreate("SuperEntity_Releases", [["SuperEntity_id", "1"], ["Releases_id", "1"]])
        # sql.recordCreate("SuperEntity_Releases", [["SuperEntity_id", "1"], ["Releases_id", "2"]])
        # sql.recordCreate("SuperEntity_Releases", [["SuperEntity_id", "1"], ["Releases_id", "3"]])
        # sql.recordCreate("SuperEntity_Releases", [["SuperEntity_id", "2"], ["Releases_id", "4"]])
        #
        # #data load
        # localTemp = "//home/douy/eclipse-workspace/BelegeSortieren/temp/"
        # workbook = xlrd.open_workbook(localTemp+'import_namen.xlsx')
        # workbook = workbook.sheet_by_name("Tabelle1")
        # print (workbook.cell_value(0,0))


if __name__ == '__main__':
    unittest.main(verbosity=2)
