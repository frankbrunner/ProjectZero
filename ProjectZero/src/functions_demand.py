
from ProjectZero.src.functions_testobjects import *

class db_Demand(db_functions):
    def __init__(self, User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.structDemand = Demand()
        self.structTestobject = Testobject()
        self.releaseStruct = Releases()
        self.applicationStruct = Applications()
        self.globalFunction = db_functions("dbuser", "34df!5awe", "ProjectZero")

    def createDemand(self ,demand=0 ,Testobject_id=None ,Release_id=None ,Application_id=None ,Supply_id=0):
        # minimum for demnad is Application and Release
        #Return Code
        # return values 0 insert ok 1 allready exist 2 entry criterias notok
        if self.globalFunction.checkIfExists(self.structTestobject.tablename, "id", Testobject_id) == False or \
            self.globalFunction.checkIfExists(self.releaseStruct.tablename, "id",Release_id) == False or \
            self.globalFunction.checkIfExists(self.applicationStruct.tablename, "id", Application_id) == False:
            return 1

        #if demand allready exist exit 2
        conditions = [self.structDemand.testobject_id, self.structDemand.application_id , self.structDemand.release_id]
        # if an demand combination from Applicatio and Release allready exists
        conditions_value = [Testobject_id, Application_id ,Release_id]
        if self.globalFunction.checkIfExists(self.structDemand.tablename, conditions, conditions_value):
            return 2
        #if all condition true create demand
        values = [demand, Testobject_id, Release_id, Application_id, Supply_id]
        sql = self.globalFunction.sqlGenearatorInsert(self.structDemand.tablename, self.structDemand.rows, values)
        print (sql)
        returnCode = self.globalFunction.insertData(sql,values)
        if returnCode:
            returnCode = 0
        else:
            returnCode = 1
        print(returnCode)
        return returnCode

    def updateDemand(self,DemandId,column=None,value=None, argument=None ):
        #argument cann be
        #delete set te attribute status to 1
        #column can be demand,
        column = column
        value = value
        argument = argument

        if argument != None:
            if argument =="delete":
                returnCode = self.updateRecord(self.structDemand.tablename, "staus", 1, "id", DemandId)
        else:
            returnCode = self.updateRecord(self.structDemand.tablename, column, value, "id", DemandId)
            print("in")
        return returnCode


# Unit Test Section
demand = db_Demand("dbuser", "34df!5awe", "ProjectZero")
project = pz_Projects("dbuser", "34df!5awe", "ProjectZero")
testobject = pz_Testobject("dbuser", "34df!5awe", "ProjectZero")
applications = pz_Applications("dbuser", "34df!5awe", "ProjectZero")
releases = pz_Releases("dbuser", "34df!5awe", "ProjectZero")

class MyTestCase(unittest.TestCase):

    def test_a_createDemand(self):

        project.createProject(4856, "Test Project")
        projectID = project.getProjectId(4856)

        testobject.createTestobject(projectID)
        testobjectID = testobject.getTestobjectID(4856)

        releases.createRelease(2020,"MDR","MDR04")
        releaseID = releases.getReleaseID("MDR04")

        applications.createApplication("CRMPF")
        applications.createApplication("PEDAS")
        applicationID = applications.getApplicatioID("PEDAS")

        self.assertEqual(demand.createDemand(0,testobjectID,releaseID,applicationID), 0)
        self.assertEqual(demand.createDemand(0, testobjectID, releaseID, applicationID), 2)

    def test_b_updateDemand(self):
        self.assertEqual(demand.updateDemand(2,"demand",30),0)


if __name__ == '__main__':
    unittest.main(verbosity=2)