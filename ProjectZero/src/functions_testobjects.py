from ProjectZero.src.functions_global import *
from ProjectZero.src.functions_applications import *
from ProjectZero.src.functions_projects import *
from ProjectZero.src.functions_releases import *

import unittest


class pz_Testobject(db_functions):
    def __init__(self, User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.obj_Testobject = Testobject()

        self.tableName = self.obj_Testobject.tablename
        self.obj_Projects = pz_Projects("dbuser", "34df!5awe", "ProjectZero")
        self.obj_Applications = pz_Applications("dbuser", "34df!5awe", "ProjectZero")
        self.obj_Releases = pz_Releases("dbuser", "34df!5awe", "ProjectZero")
        self.structApplications = Applications()
        self.structReleases = Releases()
        self.structTestobjectRelease = Testobject_Release()
        self.strucReleaseApplication = Release_Application()
        self.obj_Testobject_Release = Testobject_Release()

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

    def addRelease(self,ProjectNumber,ReleaseName,debug=0):
        #Return Code 0 successful
        #Return Code 1 problem
        testobjectID  = self.getTestobjectID(ProjectNumber)
        releaseID = self.obj_Releases.getReleaseID(ReleaseName)
        rows  = [self.obj_Testobject_Release.testobject_id,self.obj_Testobject_Release.release_id]
        values = [testobjectID, releaseID]

        returnCode =self.checkAndInsert(self.obj_Testobject_Release.tablename, self.obj_Testobject_Release.rows, values,debug)
        return returnCode

    def removeRelease(self,ProjectNumber,ReleaseName):
        # Return Code 0 successful
        # Return Code 1 problem
        testobjectID = self.getTestobjectID(ProjectNumber)
        releaseID = self.obj_Releases.getReleaseID(ReleaseName)
        values = [testobjectID, releaseID]

        returnCode = self.recordDelete(self.obj_Testobject_Release.tablename, self.obj_Testobject_Release.rows, values)
        return returnCode

    def getReleases(self,ProjectNumber):
        #Return Code 0  non application is mappet to object
        #Resoult as an list of Tubles
        testobjectID = self.getTestobjectID(ProjectNumber)

        sql = 'SELECT ' + self.structReleases.tablename + '.' + self.structReleases.name + \
              ' FROM ' + self.obj_Testobject_Release.tablename + \
              ' INNER JOIN ' + self.structReleases.tablename + \
              ' ON ' + self.obj_Testobject_Release.tablename + '.' + self.obj_Testobject_Release.release_id + '=' + self.structReleases.tablename + '.id ' \
               'WHERE ' + self.obj_Testobject_Release.testobject_id + '="' + str(testobjectID) + '"'

        result = self.readData(sql)

        if len(result) == 0:
            return 0
        else:
            return result

    def addApplication(self,ProjectNumber, ReleaseName, ApplicationName):
        #Return Code 0 successful
        #Return Code 1 problem
        testobjectID  = self.getTestobjectID(ProjectNumber)
        releasesID = self.obj_Releases.getReleaseID(ReleaseName)

        testobject_releaseID = self.getTableID(self.structTestobjectRelease.tablename,
                                [self.structTestobjectRelease.testobject_id,self.structTestobjectRelease.release_id],
                                [testobjectID,releasesID],True )

        applicationID = self.obj_Applications.getApplicatioID(ApplicationName)

        column= [self.strucReleaseApplication.application_id,self.strucReleaseApplication.testobject_release_id]
        values = [applicationID,testobject_releaseID]

        returnCode=self.checkAndInsert(self.strucReleaseApplication.tablename,column,values,True)

        return returnCode

    def removeApplication(self, ProjectNumber, ReleaseName, ApplicationName):
        # Return Code 0 successful
        # Return Code 1 problem
        testobjectID = self.getTestobjectID(ProjectNumber)
        releasesID = self.obj_Releases.getReleaseID(ReleaseName)

        testobject_releaseID = self.getTableID(self.structTestobjectRelease.tablename,
                                               [self.structTestobjectRelease.testobject_id,
                                                self.structTestobjectRelease.release_id],
                                               [testobjectID, releasesID], True)

        applicationID = self.obj_Applications.getApplicatioID(ApplicationName)

        column = [self.strucReleaseApplication.application_id, self.strucReleaseApplication.testobject_release_id]
        values = [applicationID, testobject_releaseID]

        returnCode = self.recordDelete(self.strucReleaseApplication.tablename,column,values)
        return returnCode


# Unit Test Section
testobject = pz_Testobject("dbuser", "34df!5awe", "ProjectZero")
project = pz_Projects("dbuser", "34df!5awe", "ProjectZero")
applications = pz_Applications("dbuser", "34df!5awe", "ProjectZero")
releases = pz_Releases("dbuser", "34df!5awe", "ProjectZero")

class MyTestCase(unittest.TestCase):

    def test_a_createTestobject(self):
        self.assertEqual(project.createProject(4856, "Test Project"), 0)
        projectID = project.getProjectId(4856)

        self.assertEqual(testobject.createTestobject(projectID), 0)
        self.assertEqual(testobject.createTestobject(projectID), 1)

    def test_b_getTestobjectID(self):
        self.assertGreater(testobject.getTestobjectID(4856), 0)
        self.assertEqual(testobject.getTestobjectID(4000), 0)

    def test_c_addRelease(self):
        self.assertEqual(releases.createRelease(2020, "MDR", "MDR04"), 0)
        self.assertEqual(releases.createRelease(2020, "Major", "RE20A"), 0)

        self.assertEqual(testobject.addRelease(4856,"MDR04",False),0)
        self.assertEqual(testobject.addRelease(4856, "MDR04", False), 1)
        self.assertEqual(testobject.addRelease(4856, "RE20A", False), 0)

    def test_d_getReleases(self):
        print(testobject.getReleases(4856))

    def test_e_addApplications(self):
        applications.createApplication("PEDAS")
        testobject.addApplication(4856,"MDR04","PEDAS")

    def test_z_delete(self):
        self.assertEqual(testobject.removeApplication(4856, "MDR04", "PEDAS"),0)
        self.assertEqual(testobject.removeRelease(4856, "MDR04"), 0)
        self.assertEqual(testobject.deleteTestobject(None, 4856), 0)
        self.assertEqual(project.deleteProject(4856), 0)
        self.assertEqual(releases.deleteRelease("name","MDR04"), 0)
        self.assertEqual(releases.deleteRelease("name", "RE20A"), 0)
        self.assertEqual(applications.deleteApplication("name"), 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)