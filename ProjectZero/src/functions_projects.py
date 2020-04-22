import unittest
from ProjectZero.src.functions_global import *
from ProjectZero.src.db_struct import *

class pz_Projects(db_functions):
    def __init__(self, User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.obj_Projects= Projects()
        self.tableName = self.obj_Projects.tablename

    def createProject(self, ProjectNumber, ProjectDescription):
        #Return Codes
        #0 Project successfull insert
        #1 Project allready exist
        #2 any Failure
        debug = False
        rows = self.obj_Projects.rows
        values = [int(ProjectNumber), str(ProjectDescription)]
        select = self.obj_Projects.number
        return (self.checkAndInsert(self.obj_Projects.tablename,rows,values,debug,select))

    def getProjects(self, Project_id=None):
        #if no Parameter return all Projects
        #Return the Result list of tubles or None if not exist

        rows=self.obj_Projects.rows

        if Project_id != None:
            conditions=["id"]
            values = [Project_id]
        else:
            conditions=[]
            values = []

        sql = self.sqlGenerator(self.obj_Projects.tablename,rows,conditions,values)
        result=self.readData(sql)

        if result == False:
            return None
        return result

    def getProjectId(self, ProjectNumber):
        #Return the Project id
        #Return 0 if not exists
        conditions=[self.obj_Projects.number]
        values = [ProjectNumber]
        rows=["id"]

        sql = self.sqlGenerator(self.obj_Projects.tablename,rows,conditions,values)

        result=self.readData(sql)

        if result == False:
            return 0
        else:
            result = result[0]
            result = result[0]
        return result

    def deleteProject(self,ProjectNumber):
        #Return Codes
        #0 Project successfull deleted
        #1 any Failure
        row = self.obj_Projects.number
        value = ProjectNumber
        returnCode = self.recordDelete(self.obj_Projects.tablename,row,value)
        return returnCode


# Unit Test Section
app = pz_Projects( "dbuser", "34df!5awe", "ProjectZero")

class MyTestCase(unittest.TestCase):

    def test_a_createProject(self):
        self.assertEqual(app.createProject(4856,"Test Project"),0)
        self.assertEqual(app.createProject(4856, "Test Project"), 1)

    def test_b_createProjet(self):
        self.assertEqual(app.createProject(4888, "Test Project"), 0)

    def test_c_getProjects(self):
        list = [(4856,"Test Project"),(4888,"Test Project")]
        self.assertCountEqual(app.getProjects(),list)

    def test_d_getProjectsID(self):
        self.assertGreater(app.getProjectId(4856),0)

    def test_e_deleteProjects(self):
        self.assertEqual(app.deleteProject(4856),0)
        self.assertEqual(app.deleteProject(4888),0)

if __name__ == '__main__':
    unittest.main(verbosity=2)