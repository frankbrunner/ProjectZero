import unittest
from ProjectZero.src.functions_global import *
from ProjectZero.src.db_struct import *

class pz_Releases(db_functions):
    def __init__(self, User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.obj_Releases= Releases()
        self.tableName = self.obj_Releases.tablename

    def createRelease(self, Year=0, Type="MDR", Name="Medium Release"):
        # Return Codes
        # 0 Project successfull insert
        # 1 Project allready exis
        # 2 any Failure
        table = self.obj_Releases.tablename
        rows = self.obj_Releases.rows
        values = [int(Year), str(Type), str(Name)]
        return (self.checkAndInsert(table, rows, values))

    def deleteRelease(self, column="name", Name="MDR01"):
        #Return Codes
        #0 Project successfull deleted
        #1 any Failure
        table = self.obj_Releases.tablename
        value = Name
        returnCode = self.recordDelete(table, self.obj_Releases.name, value)
        return returnCode

    def getReleaseID(self, ReleaseName):
        # Return ReleaseID from specific Release
        # Return Codes
        # 2 any Failure
        table = self.obj_Releases.tablename
        rows = ["id"]

        if ReleaseName != None:
            conditions = [self.obj_Releases.name]
            values = [ReleaseName]
        else:
            pass
        sql = self.sqlGenerator(table, rows, conditions, values)
        result = self.readData(sql)
        if result == False:
            return 2
        else:
            result = result[0]
            result = result[0]
        return result

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


# Unit Test Section
releases = pz_Releases( "dbuser", "34df!5awe", "ProjectZero")

class MyTestCase(unittest.TestCase):

    def test_a_createReleases(self):
        self.assertEqual(releases.createRelease(2020,"MDR","MDR04"),0)
        self.assertEqual(releases.createRelease(2020, "MDR", "MDR04"), 1)

    def test_b_getReleaseID(self):
        self.assertGreater(releases.getReleaseID("MDR04"), 0)
        print(releases.getReleaseID("MDR04"))

    def test_c_deleteProject(self):
        self.assertEqual(releases.deleteRelease("Description","MDR04"), 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)