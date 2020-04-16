from ProjectZero.src.ps_db_functions_global import *
from ProjectZero.src.pz_db_functions_projects import *
from ProjectZero.src.pz_db_functions_applications import *
import ProjectZero.src.rp_db_connect
import unittest


class pz_Testobject(db_functions):
    def __init__(self, User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.obj_Testobject = Testobject()

        self.tableName = self.obj_Testobject.tablename
        self.obj_Projects = pz_Projects("dbuser", "34df!5awe", "ProjectZero")
        self.obj_Applications = rp_Applications("dbuser", "34df!5awe", "ProjectZero")
        self.obj_struct_Applications = Applications()
        self.obj_Testobject_Application = Testobject_Application()

    def createTestobject(self, Porject_id=0, Demand_id=0, Planning_Item_id=0, Application_id=0):
        #Return Code
        #0 Project successfull insert
        #1 Project allready exis
        #2 any Failure
        rows = self.obj_Testobject.rows
        values = [str(Porject_id), str(Demand_id),str(Planning_Item_id),str(Application_id)]
        select=self.obj_Testobject.project_id

        condition=self.obj_Testobject.project_id
        condition_value = Porject_id

        returnValue = self.checkIfExists(self.tableName,condition,condition_value)
        if returnValue==False:
            sql = self.sqlGenearatorInsert(self.tableName,rows,values)
            self.insertData(sql,values)
        else:
            return 1
        return returnValue

    def getTestobjectID(self, ProjectNumber):
        #Return the id of Testobject
        #Return 0 if not exists
        obj_join = Projects()

        sql = 'SELECT ' + self.obj_Testobject.tablename + '.id'\
              ' FROM ' + self.obj_Testobject.tablename + \
              ' INNER JOIN ' + obj_join.tablename +\
              ' ON ' + self.obj_Testobject.tablename + '.' + self.obj_Testobject.project_id + '=' + obj_join.tablename + '.id ' \
              'WHERE ' + obj_join.number +'="' + str(ProjectNumber) +'"';

        result=self.readData(sql)

        if len(result) == 0 :
            return 0
        else:
            result = result[0]
            result = result[0]
        return result

    def deleteTestobject(self,id=None,ProjectNumber=None):
        if id != None:
            value = id
            row = "id"
        if ProjectNumber !=None:
            value = ProjectNumber
            value = self.obj_Projects.getProjectId(ProjectNumber)
            row = self.obj_Testobject.project_id
        if id and ProjectNumber == None:
            return 1
        returnCode=self.recordDelete(self.obj_Testobject.tablename,row,value)

        return returnCode

    def addApplication(self,ProjectNumber,ApplicationName):
        #Return Code 0 successful
        #Return Code 1 problem
        testobjectID  = self.getTestobjectID(ProjectNumber)
        applicationID = self.obj_Applications.getApplicatioID(ApplicationName)
        values = [testobjectID,applicationID]

        returnCode=self.checkAndInsert(self.obj_Testobject_Application.tablename,self.obj_Testobject_Application.rows,values)
        return returnCode

    def removeApplication(self,ProjectNumber,ApplicationName):
        # Return Code 0 successful
        # Return Code 1 problem
        testobjectID = self.getTestobjectID(ProjectNumber)
        applicationID = self.obj_Applications.getApplicatioID(ApplicationName)
        values = [testobjectID, applicationID]

        returnCode = self.recordDelete(self.obj_Testobject_Application.tablename,self.obj_Testobject_Application.rows,values)
        return returnCode

    def getApplications(self,ProjectNumber):

        testobjectID = self.getTestobjectID(ProjectNumber)

        sql = 'SELECT ' + self.obj_struct_Applications.tablename +'.'+ self.obj_struct_Applications.name+ \
              ' FROM ' + self.obj_Testobject_Application.tablename + \
              ' INNER JOIN ' + self.obj_struct_Applications.tablename + \
              ' ON ' + self.obj_Testobject_Application.tablename + '.' + self.obj_Testobject_Application.application_id + '=' +self.obj_struct_Applications.tablename + '.id ' \
               'WHERE ' + self.obj_Testobject_Application.testobject_id + '="' + str(testobjectID) + '"'

        result = self.readData(sql)

        if len(result) == 0:
            return 0
        else:
            return result

# Unit Test Section
testobject = pz_Testobject("dbuser", "34df!5awe", "ProjectZero")
from ProjectZero.src.pz_db_functions_projects import *
project = pz_Projects("dbuser", "34df!5awe", "ProjectZero")
applications = rp_Applications("dbuser", "34df!5awe", "ProjectZero")

class MyTestCase(unittest.TestCase):

    def test_a_createTestobject(self):
        self.assertEqual(project.createProject(4856, "Test Project"), 0)
        projectID = project.getProjectId(4856)

        self.assertEqual(testobject.createTestobject(projectID), 0)
        self.assertEqual(testobject.createTestobject(projectID), 1)

    def test_b_getTestobjectID(self):
        self.assertGreater(testobject.getTestobjectID(4856), 0)
        self.assertEqual(testobject.getTestobjectID(4000), 0)

    def test_c_addApplication(self):
        applications.createApplication("CRMPF")
        applications.createApplication("PEDAS")

        self.assertEqual(testobject.addApplication(4856, "CRMPF"), 0)
        self.assertEqual(testobject.addApplication(4856, "PEDAS"), 0)

    def test_d_getApplications(self):
        print (testobject.getApplications(4856))

    def test_e_removeApplication(self):
        self.assertEqual(testobject.removeApplication(4856, "CRMPF"), 0)
        self.assertEqual(testobject.removeApplication(4856, "PEDAS"), 0)

    def test_f_deleteTestobject(self):
        self.assertEqual(testobject.deleteTestobject(None,4856),0)

    def test_z_deleteProject(self):
        self.assertEqual(project.deleteProject(4856), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)