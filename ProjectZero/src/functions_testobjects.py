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

    def createTestobject(self, ProjectNumber, Demand_id=0, Planning_Item_id=0, Application_id=0):
        #Return Code
        #0 Project successfull insert
        #1 Project allready exis
        #2 any Failure
        projectID = self.obj_Projects.getProjectId(ProjectNumber)
        rows = self.obj_Testobject.rows
        values = [str(projectID), str(Demand_id), str(Planning_Item_id), str(Application_id)]
        select=self.obj_Testobject.project_id

        condition=self.obj_Testobject.project_id
        condition_value = projectID

        returnValue = self.checkIfExists(self.tableName,condition,condition_value)
        if returnValue==False:
            sql = self.sqlGenearatorInsert(self.tableName,rows,values)
            self.insertData(sql,values)
        else:
            return 1
        return returnValue

    def getTestobject(self,id=False):
        if id == False:
            sql = 'SELECT Projects.number ' \
                  'FROM Projects ' \
                  'INNER JOIN Testobject ' \
                  'ON Projects.id = Testobject.project_id'

            result = self.readData(sql)
        if len(result) == 0:
            return [("kein Testobjekt vorhanden",)]
        else:
            return result

    def getTestobjectID(self, ProjectNumber,debug=False):
        #Return the id of Testobject
        #Return 0 if not exists
        obj_join = Projects()

        sql = 'SELECT ' + self.obj_Testobject.tablename + '.id'\
              ' FROM ' + self.obj_Testobject.tablename + \
              ' INNER JOIN ' + obj_join.tablename +\
              ' ON ' + self.obj_Testobject.tablename + '.' + self.obj_Testobject.project_id + '=' + obj_join.tablename + '.id ' \
              'WHERE ' + obj_join.number +'="' + str(ProjectNumber) +'"';
        if debug:
            print("get TestobjecktID:"+str(sql))
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

    def addRelease(self,ProjectNumber,ReleaseName,debug=False):
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

    def getAllReleases(self, ProjectNumber,debug=False):
        #Return Code 0  non application is mappet to object
        #Resoult as an list of Tubles
        testobjectID = self.getTestobjectID(ProjectNumber,True)

        sql = 'SELECT ' + self.structReleases.tablename + '.' + self.structReleases.release + \
              ' FROM ' + self.obj_Testobject_Release.tablename + \
              ' INNER JOIN ' + self.structReleases.tablename + \
              ' ON ' + self.obj_Testobject_Release.tablename + '.' + self.obj_Testobject_Release.release_id + '=' + self.structReleases.tablename + '.id ' \
               'WHERE ' + self.obj_Testobject_Release.testobject_id + '="' + str(testobjectID) + '"'

        result = self.readData(sql,debug)

        if len(result) == 0:
            return 0
        else:
            return result

    def addApplication(self,ProjectNumber, ReleaseName, ApplicationName,debug=False):
        #Return Code 0 successful
        #Return Code 1 problem
        testobjectID  = self.getTestobjectID(ProjectNumber)
        releasesID = self.obj_Releases.getReleaseID(ReleaseName)

        testobject_releaseID = self.getTableID(self.structTestobjectRelease.tablename,
                                [self.structTestobjectRelease.testobject_id,self.structTestobjectRelease.release_id],
                                [testobjectID,releasesID],debug)

        applicationID = self.obj_Applications.getApplicatioID(ApplicationName)

        column= [self.strucReleaseApplication.application_id,self.strucReleaseApplication.testobject_release_id]
        values = [applicationID,testobject_releaseID]

        returnCode=self.checkAndInsert(self.strucReleaseApplication.tablename,column,values,debug)

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
        self.assertEqual(project.createProject(9901, "Test Project"), 0)
        self.assertEqual(project.createProject(9902, "Test 1"), 0)
        self.assertEqual(project.createProject(9903, "Test 2"), 0)


        self.assertEqual(testobject.createTestobject(9901), 0)
        self.assertEqual(testobject.createTestobject(9901), 1)
        self.assertEqual(testobject.createTestobject(9902), 0)

    def test_b_getTestobjectID(self):
        self.assertGreater(testobject.getTestobjectID(9901), 0)


    def test_c_addRelease(self):
        try:
            self.assertEqual(releases.createRelease(2025, "MDR", "MDR04"), 0)
            self.assertEqual(releases.createRelease(2025, "Major", "RE20A"), 0)
        except:
            pass
        self.assertEqual(testobject.addRelease(9901,"MDR04",False),0)
        self.assertEqual(testobject.addRelease(9901, "MDR04", False), 1)
        self.assertEqual(testobject.addRelease(9901, "RE20A", False), 0)

    def test_d_getReleases(self):
        self.assertCountEqual(testobject.getAllReleases(9901),[('MDR04',), ('RE20A',)])

    def test_e_addApplications(self):
        applications.createApplication("TestApplication")
        testobject.addApplication(9901,"MDR04","TestApplication",debug=False)

    def test_f_getTestobjects(self):
        self.assertEqual(testobject.getTestobject(),[(9901,),(9902,)])

    def test_z_delete(self):
    #     self.assertEqual(testobject.removeApplication(4856, "MDR04", "PEDAS"),0)
    #     self.assertEqual(testobject.removeRelease(4856, "MDR04"), 0)
        self.assertEqual(testobject.deleteTestobject(None, 9901), 0)
        self.assertEqual(testobject.deleteTestobject(None, 9902), 0)
        self.assertEqual(project.deleteProject(9901), 0)
        self.assertEqual(project.deleteProject(9902), 0)
        self.assertEqual(project.deleteProject(9903), 0)
        self.assertEqual(releases.deleteRelease("name","MDR04"), 0)
        self.assertEqual(releases.deleteRelease("name", "RE20A"), 0)
        self.assertEqual(applications.deleteApplication("TestApplication"), 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)