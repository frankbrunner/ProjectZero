import unittest
from ProjectZero.src.functions_global import *
from ProjectZero.src.db_struct import *

class pz_Releases(db_functions):
    def __init__(self, User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.obj_Releases= Releases()
        self.tableName = self.obj_Releases.tablename

    def createRelease(self, dateFrom="2020-01-30", dateTo="2020-02-30", ReleaseName="Medium Release"):
        # Return Codes
        # 0 Project successfull insert
        # 1 Project allready exis
        # 2 any Failure
        table = self.obj_Releases.tablename
        column = self.obj_Releases.column
        values = [str(dateFrom), str(dateTo), str(ReleaseName)]
        return (self.checkAndInsert(table, column, values))

    def deleteRelease(self, column="name", Name="MDR01"):
        #Return Codes
        #0 Project successfull deleted
        #1 any Failure
        table = self.obj_Releases.tablename
        value = Name
        returnCode = self.recordDelete(table, self.obj_Releases.release, value)
        return returnCode

    def getReleaseID(self, ReleaseName):
        # Return ReleaseID from specific Release
        # Return Codes
        # 2 any Failure
        table = self.obj_Releases.tablename
        rows = ["id"]

        if ReleaseName != None:
            conditions = [self.obj_Releases.release]
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


    def getReleases(self,debug=False):
        #Return the Result tuble or None if not exist
        obj_Releases = Releases()
        table=obj_Releases.tablename
        column= [obj_Releases.release]

        sql = self.sqlGenerator(table,column)
        if debug==True:
            print(sql)
        result=self.readData(sql)
        if result == False:
            return 0
        return result


# Unit Test Section
releases = pz_Releases( "dbuser", "34df!5awe", "ProjectZero")

class MyTestCase(unittest.TestCase):

    def test_a_createReleases(self):
        self.assertEqual(releases.createRelease("2020-01-30","2020-01-25","RE25A"),0)
        self.assertEqual(releases.createRelease("2020-01-30","2020-01-25","RE25A"), 1)

    def test_b_getReleaseID(self):
        self.assertGreater(releases.getReleaseID("RE25A"), 0)
        print(releases.getReleaseID("RE25A"))

    def test_c_deleteProject(self):
        self.assertEqual(releases.deleteRelease("release_name","RE25A"), 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)