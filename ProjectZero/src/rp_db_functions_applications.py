from ProjectZero.src.rp_db_functions import *
import unittest

class rp_Applications(db_functions):
    def __init__(self,User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.obj_Applications = Applications()
        self.tableName = self.obj_Applications.tablename

    def createApplication(self, ApplicationName):
        #Return Codes
        #0 Project successfull insert
        #1 Project allready exist
        #2 any Failure
        rows = [self.obj_Applications.name]
        values = [str(ApplicationName)]
        select = self.obj_Applications.name
        return (self.checkAndInsert(self.tableName,rows,values,select))

    def getApplication(self, Application_id=None):
        #if no Parameter return all Projects
        #Return the Result list of tubles or None if not exist
        #I Id ist given the result will be a single value Application Name
        rows=self.obj_Applications.rows

        if Application_id != None:
            conditions=["id"]
            values = [Application_id]
        else:
            conditions=[]
            values = []
        sql = self.sqlGenerator(self.tableName,rows,conditions,values)
        result=self.readData(sql)

        if result == False:
            return None
        else:
            #from Tuble in List to single Value
            if Application_id != None:
                result = result[0]
                result = result[0]
        return result

    def getApplicatioID(self, ApplicationName):
        #Return ReleaseID from specific Release
        # Return Codes
        # 2 any Failure
        rows= ["id"]

        if ApplicationName != None:
            conditions = [self.obj_Applications.name]
            values = [ApplicationName]
        else:
            pass
        sql = self.sqlGenerator(self.tableName,rows,conditions,values)
        result=self.readData(sql)
        if result == False:
            return 2
        else:
            result = result[0]
            result = result[0]
        return result

    def deleteApplication(self, ApplicationName,row="name"):
        # Return Codes
        # 0 Project successfull deleted
        # 1 any Failure
        returnCode = self.recordDelete(self.tableName, row, ApplicationName)
        return returnCode


 #Unit Test Section
app = rp_Applications("dbuser", "34df!5awe", "ProjectZero")
class MyTestCase(unittest.TestCase):

    def test_a_createApp(self):
        self.assertEqual(app.createApplication("CRMPF"), 0)
        self.assertEqual(app.createApplication("PEDAS"), 0)

    def test_b_createMultiple(self):
        self.assertEqual(app.createApplication("CRMPF"), 1)

    def test_c_getApplications(self):
        listApplication = [("CRMPF",),("PEDAS",)]
        self.assertCountEqual(app.getApplication(), listApplication)

    def test_d_getApplicationID(self):
        id = app.getApplicatioID("CRMPF")
        self.assertEqual(app.getApplicatioID("CRMPF"), id)

    def test_e_getApplicationByID(self):
        id = app.getApplicatioID("CRMPF")
        self.assertEqual(app.getApplication(id), "CRMPF")

    def test_f_deleteApp(self):
        self.assertEqual(app.deleteApplication("CRMPF"), 0)
        self.assertEqual(app.deleteApplication("PEDAS"), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
